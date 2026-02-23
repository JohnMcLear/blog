---
title: "How to install mod_rpaf Varnish Wordpress Ubuntu"
date: 2011-09-09
categories: 
  - "varnish"
  - "wordpress"
---

And the geekiest title of the week goes to me...

Add this line to your varnish VCL in sub\_recv: \[code\]set req.http.X-Forwarded-For = client.ip;\[/code\]

Grab mod\_rpaf: \[code\]wget http://ftp.debian.org/debian/pool/main/liba/libapache2-mod-rpaf/libapache2-mod-rpaf\_0.6-7\_amd64.deb\[/code\]

Install mod\_rpaf \[code\]dpkg -i libapache2-mod-rpaf\_0.6-1\_amd64.deb\[/code\]

Enable mod\_rpaf: \[code\]a2enmod rpaf\[/code\]

Your rpaf config (/etc/apache2/mods-enabled/rpaf.conf) should look awesome like this: \[code\] <IfModule mod\_rpaf.c> RPAFenable On RPAFsethostname On RPAFproxy\_ips 123.123.123.123 10.0.0.2 127.0.0.1 RPAFheader HTTP\_X\_FORWARDED\_FOR </IfModule> \[/code\] Note: RPAFproxy\_ips is the ips of your varnish cache servers. Varnish is awesome.

Reload varnish and Apache the cool way. \[code\] /etc/init.d/varnish reload /etc/init.d/apache reload \[/code\]

Test it by looking at your remote\_addr variable: \[php\] print\_r($\_SERVER); \[/php\]
