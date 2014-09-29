# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "ubuntu/trusty64"

  # Define machines
  config.vm.define "alpha"
  config.vm.define "beta", autostart: false
  config.vm.define "gamma", autostart: false
  config.vm.define "delta", autostart: false

  # Run ansible playbooks for defined groups
  config.vm.provision "ansible" do |ansible|
    ansible.verbose = "vvv"
    ansible.groups = {
      "db" => ["alpha"],
      "mda" => ["gamma", "delta"],
      "mta" => ["beta"]
    }
    ansible.playbook = "playbook.yml"
  end
end
