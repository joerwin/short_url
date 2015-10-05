# -*- mode: ruby -*-
# vi: set ft=ruby :

$access_key_id = "YOUR AWS KEY"
$secret_access_key = "YOUR AWS SECRET"
VAGRANTFILE_API_VERSION = "2"

################################################################################
# Machine definitions
################################################################################
load_path = File.expand_path File.dirname(__FILE__) + "/machines.d/*.rb" 
Dir[load_path].each {|file| require file}
################################################################################
#Helping methods
################################################################################ 


def config_aws(config, hostname, zone, subnet_id, instance_type, isPublic)
  config.vm.box = "dummy"
  config.vm.box_url = "https://github.com/mitchellh/vagrant-aws/raw/master/dummy.box"

  config.vm.provider :aws do |aws, override|
    aws.region = 'us-east-1'
    aws.access_key_id = $access_key_id
    aws.secret_access_key = $secret_access_key
    aws.keypair_name = 'YOUR KEYPAIR NAME'
    aws.instance_type = instance_type
    aws.ami = 'ami-df38e6b4' #Base ubuntu 14.04.2 AMI
    aws.subnet_id = subnet_id
    aws.security_groups = ['YOUR', 'LIST', 'OF', 'SECUTRITY', 'GROUPS'] #Ensure to allow http in on port 80
    override.ssh.username= 'ubuntu'
    override.ssh.pty = false
    override.ssh.private_key_path = 'YOUR PATH TO AWS PRIVATE KEY'
    aws.tags = {Name: hostname}
    aws.associate_public_ip = isPublic
  end
end
