from string import Template
from collections import namedtuple

from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver


INSTANCE_SIZE='t2.micro'
COREOS_AMI='ami-1db04f59'
AWS_ACCESS_KEY='AKIAJSOLMV5QAYVF3PWQ'
AWS_SECRET_KEY='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'
SUBNET_ID='subnet-f37abaaa'
AZ_ID='us-west-1a'
VPC_ID = 'vpc-a6b513c3'
ETCD_DISCOVERY_TOKEN='ccce5e28548840aa2ae99d092e96bf8b'

USER_DATA_TEMPLATE = Template("""#cloud-config
coreos:
  update:
    reboot-strategy: off
  etcd2:
    discovery: https://discovery.etcd.io/${etcd_discovery_token}
    advertise-client-urls: http://$$private_ipv4:2379,http://$$private_ipv4:4001
    initial-advertise-peer-urls: http://$$private_ipv4:2380
    listen-client-urls: http://0.0.0.0:2379,http://0.0.0.0:4001
    listen-peer-urls: http://$$private_ipv4:2380,http://$$private_ipv4:7001
  units:
    - name: etcd2.service
      command: start
    - name: fleet.service
      command: start
    - name: format-influxdb.service
      runtime: true
      command: start
      content: |
        [Unit]
        Description=Wipe /dev/xvdb if not formatted yet
        [Service]
        Type=oneshot
        RemainAfterExit=yes
        ExecStart=/bin/bash -c '(/usr/sbin/blkid -t TYPE=btrfs | grep /dev/xvdb) || (/usr/sbin/wipefs -fa /dev/xvdb && /usr/sbin/mkfs.btrfs -f /dev/xvdb)'
    - name: format-grafana.service
      runtime: true
      command: start
      content: |
        [Unit]
        Description=Wipe /dev/xvdc if not formatted yet
        [Service]
        Type=oneshot
        RemainAfterExit=yes
        ExecStart=/bin/bash -c '(/usr/sbin/blkid -t TYPE=btrfs | grep /dev/xvdc) || (/usr/sbin/wipefs -fa /dev/xvdc && /usr/sbin/mkfs.btrfs -f /dev/xvdc)'
    - name: data-influxdb.mount
      command: start
      content: |
        Requires=format-influxdb.service
        After=format-influxdb.service
        [Mount]
        What=/dev/xvdb
        Where=/data/influxdb
        Type=btrfs
    - name: data-grafana.mount
      command: start
      content: |
        Requires=format-grafana.service
        After=format-grafana.service
        [Mount]
        What=/dev/xvdc
        Where=/data/grafana
        Type=btrfs
  fleet:
    metadata: ${influxdb_volume}=/data/influxdb, ${grafana_volume}=/data/grafana""")

cls = get_driver(Provider.EC2_US_WEST)
driver = cls(AWS_ACCESS_KEY, AWS_SECRET_KEY, region=AZ_ID)

availability_zones = driver.ex_list_availability_zones()
default_az = [az for az in availability_zones if az.name == AZ_ID][0]

subnets = driver.ex_list_subnets()
default_subnet = [s for s in subnets if s.id == SUBNET_ID][0]

sizes = driver.list_sizes()
size = [s for s in sizes if s.id == INSTANCE_SIZE][0]
image = driver.get_image(COREOS_AMI)

def create_ssd(size, name):
    NodeLocation = namedtuple('Location', ['availability_zone'])
    location = NodeLocation(default_az)
    return driver.create_volume(size=size, name=name,
                                ex_volume_type='gp2', location=location)

influxdb_volume = create_ssd(size=20, name='influxdb')
grafana_volume = create_ssd(size=1, name='grafana')

elastic_ip = driver.ex_allocate_address(domain=VPC_ID)

user_data = USER_DATA_TEMPLATE.substitute(
        etcd_discovery_token=ETCD_DISCOVERY_TOKEN,
        influxdb_volume=influxdb_volume.id,
        grafana_volume=grafana_volume.id
)

node = driver.create_node(name='test', image=image, size=size,
        ex_keyname='lukas',
        ex_userdata=user_data,
        ex_security_group_ids=['sg-60a53f05', 'sg-3458c251', 'sg-055bc160'],
        ex_subnet=default_subnet
)
driver.wait_until_running(nodes=[node])

influxdb_volume.attach(node, device='/dev/sdb')
grafana_volume.attach(node, device='/dev/sdc')
driver.ex_associate_address_with_node(node, elastic_ip)
