# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "ubuntu/trusty64"

  # Define machines
  config.vm.define "elephant"
  config.vm.define "norman", autostart: false
  config.vm.define "mercury"
  config.vm.define "hermes", autostart: false

  # Run ansible playbooks for defined groups
  config.vm.provision "ansible" do |ansible|
    ansible.verbose = "vv"
    ansible.groups = {
      "db" => ["elephant"],
      "mda" => ["mercury", "hermes"],
      "mta" => ["norman"]
    }
    ansible.playbook = "playbook.yml"
  end
end
