# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.hostname = "norman"
  config.vm.network "forwarded_port", guest:142, host:1420
  config.vm.network "forwarded_port", guest:8000, host:8000
  config.vm.define "norman"
  config.vm.synced_folder "../web", "/srv/www/mailgenic/", create: true
  config.vm.provision "ansible" do |ansible|
    ansible.verbose = "vv"
    ansible.playbook = "playbook.yml"
  end
end
