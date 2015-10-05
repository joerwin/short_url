hostname=$@

echo $hostname > /etc/hostname
echo "127.0.0.1 $hostname" >> /etc/hosts
hostname -F /etc/hostname
