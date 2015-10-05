Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  
  instanceSize = "t2.micro"
  isPublic = true
  zone = "a"
  subnet = "YOUR SUBNET ID"

  #We can build multiples as desired
  (1..1).each do |i|
    config.vm.define "shortUrl-#{i}" do |config|
      hostname = "shortUrl-#{i}"
      config_aws(config, hostname, zone, subnet, instanceSize, isPublic)
      
      config.vm.synced_folder ".", "/vagrant", 
      type: "rsync",
      rsync_exclude: ["machines.d", "VagrantFile"]

      config.vm.provision :shell, :path => "bootstrapScripts/set_hostname.sh", :args => hostname
      config.vm.provision :shell, :path => "bootstrapScripts/bootstrap_short_url.sh"
      
      #My latest builds can be pulled from joerwin/short_url
      config.vm.provision "docker" do |d| 
        d.pull_images "YOUR DOCKER HUB IMAGE"
        d.run "YOUR DOCKER HUB IMAGE", args: "-p 8080:8080" 
      end

    end #end of service
  end
end
                    
