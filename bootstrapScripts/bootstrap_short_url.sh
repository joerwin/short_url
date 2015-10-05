apt-get update -y
apt-get install nginx -y
update-rc.d nginx defaults
cp /vagrant/configs/short_url /etc/nginx/sites-available/short_url
ln -s /etc/nginx/sites-available/short_url /etc/nginx/sites-enabled/short_url
unlink /etc/nginx/sites-enabled/default 
service nginx reload
