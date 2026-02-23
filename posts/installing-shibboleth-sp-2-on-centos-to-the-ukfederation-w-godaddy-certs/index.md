---
title: "Installing Shibboleth SP 2 on CentOS to the ukfederation w/ Godaddy certs"
date: 2009-10-26
categories: 
  - "cent-os"
  - "centos"
  - "shibboleth"
  - "sp"
---

Internet 2 give some "creative" [documentation](https://spaces.internet2.edu/display/SHIB2/NativeSPLinuxRPMInstall) for this procedure so I thought I'd write some that are easier to follow:

**_Part 0. Planning. (2 hours)_**

1. Download CentOS Netimage boot CD from [http://centos.org](http://centos.org/)
2. Receive approval from the [UK federation](http://www.ukfederation.org.uk/content/Documents/UKFederationHelpdesk) for your service.
3. Purchase a cheep [Godaddy](http://godaddy.com/) Cert or have one ready for your service. _Be aware that you will be getting 1 SSL cert to secure your resource and another SSL cert (a self signed one) to talk to the UK federation. Do not get these certificates confused!_
4. Create the appropriate DNS records to point to the IP of your resource and the IP of your SP. IE shib.yourdomain.com (your resource) should resolve to the IP of the apache server and sp.yourdomain.com (service provider) should resolve to the same IP.

**_Part 1. Install (2 hours)_**

First things first. Install Cent OS. You don't need a gui or anything fancy, just a web server. Do all the blow as a root user.

**Set the your hostname in /etc/sysconfig/network & /etc/hosts** to match the FQDN of your SP ie sp.yourdomain.com

Install ntp date and set the date (you might want to add a cron job for this):

**yum install ntp.i386**

**ntpdate pool.ntp.org**

**NOTE: BELOW IS NOW DEFUNCT AND YOU SHOULD [USE THE DOCUMENTATION HERE](https://mclear.co.uk/2009/11/07/installing-shibboleth-sp-2-3-on-centos/) - although still complete the SELINUX section**

**cd /root/**

curl -O http://shibboleth.internet2.edu/downloads/shibboleth/cppsp/2.2.1/RPMS/i386/RHE/5/log4shib-1.0.3-1.1.i386.rpm \\

\-O http://shibboleth.internet2.edu/downloads/shibboleth/cppsp/2.2.1/RPMS/i386/RHE/5/xerces-c-3.0.1-5.1.i386.rpm \\

\-O http://shibboleth.internet2.edu/downloads/shibboleth/cppsp/2.2.1/RPMS/i386/RHE/5/xml-security-c-1.5.1-3.2.i386.rpm \\

\-O http://shibboleth.internet2.edu/downloads/shibboleth/cppsp/2.2.1/RPMS/i386/RHE/5/xmltooling-1.2.2-1.i386.rpm \\

\-O http://shibboleth.internet2.edu/downloads/shibboleth/cppsp/2.2.1/RPMS/i386/RHE/5/opensaml-2.2.1-1.i386.rpm \\

\-O http://shibboleth.internet2.edu/downloads/shibboleth/cppsp/2.2.1/RPMS/i386/RHE/5/shibboleth-2.2.1-2.i386.rpm

The above will put the files you need in /root

**Edit /etc/yum.conf** (use vi or nano) copy the gpgcheck command and then comment it out to read #gpgcheck=yes, **set gpgcheck=no** below the commented line.

**yum -y install ntp**

**/usr/sbin/ntpdate pool.ntp.org**

**yum localinstall xerces-c-3.0.1-5.1.i386.rpm**

**yum -y install unixODBC.i386**

rpm -ivh log4shib-1.0.3-1.1.i386.rpm

rpm -ivh xml-security-c-1.5.1-3.2.i386.rpm

rpm -ivh xmltooling-1.2.2-1.i386.rpm

rpm -ivh opensaml-2.2.1-1.i386.rpm

rpm -ivh shibboleth-2.2.1-2.i386.rpm

The above will install the packages. Your shibboleth config will live in /etc/shibboleth

**Edit /etc/selinux/config**

> Comment out SELINUX=enforcing
> 
> Type in SELINUX=disabled

**setenforce 0**

Warning: This will disable some security options, it can be left enabled but tweeks will need to be made to the socket restrictions later on. Can someone please document this better?

Or instead of doing above you can use system-config-securitylevel-tui to disable and restart selinux

**/usr/sbin/shibd -v**

Will return the version of shibboleth installed. If it does then:

[Continue to Part 2 (Configuring Shibboleth)](https://mclear.co.uk/2009/10/27/configuring-shibboleth-sp-2-on-centos-to-the-ukfederation-w-godaddy-certs/)
