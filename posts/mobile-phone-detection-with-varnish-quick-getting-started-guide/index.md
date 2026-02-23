---
title: "Mobile phone detection with Varnish - Quick getting started guide"
date: 2011-04-17
categories: 
  - "developer"
  - "developing"
  - "ict"
  - "mobile"
  - "varnish"
---

This is a quick reference guide, for a [proper understanding of what you are doing use this guide](http://www.enrise.com/2011/02/mobile-device-detection-with-wurfl-and-varnish/). [This solution is easier to implement and has less of a cpu overhead.](http://www.mobiledrupal.com/content/mobile-device-detection-varnish-0)

\[code\] yum install libxml2-devel #OR apt-get intall libxml2-dev wget https://gist.github.com/raw/805710/9f34a18e528c20eff1c92672c6f1856ed849f5ea/wurfl.c wget https://gist.github.com/raw/805710/b9272d8a1d32d29034574c88b81fc79eb050e21b/wurfl.h gcc -c -o wurfl.o wurfl.c -I/usr/include/libxml2 -fPIC gcc -shared -Wl,-soname,libwurfl.so.1 -o libwurfl.so.1.0.1 wurfl.o -lxml2 wget http://downloads.sourceforge.net/project/wurfl/WURFL/latest/wurfl-latest.zip unzip wurfl-latest.zip mv wurfl.xml /etc/wurfl.xml cp libwurfl.so /usr/lib ln -s /usr/lib/libwurfl.so /usr/lib64/libwurfl.so \[/code\]

Edit your /etc/varnish/mobile.vcl using [this as a guide](https://gist.github.com/raw/805710/c414644257e76eb3a7b0b2f3574d93cf7cf9d462/default.vcl)

\[code\] /etc/init.d/varnish stop /usr/sbin/varnishd -s malloc,32M -a 0.0.0.0:80 -f /etc/varnish/mobile.vcl -p 'cc\_command=exec cc -fpic -shared -Wl,-x -lwurfl -o %o %s' \[/code\]

Test by looking in your server heads.. IE in PHP.. print\_r ($\_SERVER);
