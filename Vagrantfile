# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.hostname = "pad"

  config.vm.provider "virtualbox" do |v, override|
    v.gui = false
    v.customize ["modifyvm", :id, "--memory", 1024]
    v.customize ["modifyvm", :id, "--cpus", 1]
  end

  config.vm.network :forwarded_port, guest: 9001, host: 9001

  $script = <<SCRIPT
sudo apt-get update && \
sudo apt-get install --yes gzip git-core curl python libssl-dev pkg-config build-essential

wget -O node.tar.gz http://nodejs.org/dist/v0.10.35/node-v0.10.35.tar.gz && \
tar zxf node.tar.gz && cd node-v* && \
./configure && make && sudo make install

sudo su -c "useradd etherpad -s /bin/bash -m" && \
sudo mkdir /opt/etherpad && chown etherpad:etherpad /opt/etherpad && \
sudo su etherpad -c "git clone https://github.com/ether/etherpad-lite.git /opt/etherpad"
SCRIPT

  config.vm.provision "shell", inline: $script
end
