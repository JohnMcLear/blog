---
title: "Installing the NRPE client, daemon and nagios plugins on debian"
date: 2010-01-18
categories: 
  - "guide"
  - "install"
  - "nagios"
  - "nrpe"
  - "open-source"
---

We assuming have already configured nrpe on your nagios box and you are sudo'd/root  
  
Steps:  
  
adduser nagios (set the password)  
cd /home/nagios  
wget http://prdownloads.sourceforge.net/sourceforge/nagios/nrpe-2.12.tar.gz  
_\* If this step fails visit http://www.nagios.org/download/addons for the latest URL_  
  
tar -zxvf nrpe-2.8.tar.gz  
cd nrpe-2.12  
apt-get install gcc gawk openssl  
apt-get install make  
apt-get install libssl-dev  
apt-get install nagios-plugins  
./configure  
make all  
make install-plugin  
make install-daemon  
make install-daemon-config  
echo "only\_from = 0.0.0.1" >> /usr/local/nagios/etc/nrpe.cfg  
_\* Remember to replace 0.0.0.1 with your the IP address of your nagios server_  
  
cp init-script.debian /etc/init.d/nrpe  
chmod 700 /etc/init.d/nrpe  
/etc/init.d/nrpe start  
  
_You may want to make this script run on start up_  
update-rc.d nrpe defaults
