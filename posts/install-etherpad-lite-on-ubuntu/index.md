---
title: "Install Etherpad Lite on Ubuntu and Debian"
date: 2011-08-01
categories: 
  - "etherpad"
  - "guide"
  - "install"
  - "installations"
---

## [UPDATE: These docs are now out of date, you should use the official install documents provided by the Etherpad Foundation.](https://github.com/ether/etherpad-lite/blob/master/README.md#linux)

<iframe width="600" height="400" src="http://www.youtube.com/embed/swnR9EAhf2Q" frameborder="0" allowfullscreen></iframe>

Installing Etherpad Lite on Debian/Ubuntu clean.

Part 1 - Installing prerequisites \[code\] apt-get install build-essential python libssl-dev git-core git libsqlite3-dev gzip curl # you will be prompted to press Y \[/code\]

Part 2 - Installing nodeJS and NPM \[code\] mkdir ~/local cd ~/local wget http://nodejs.org/dist/v0.6.12/node-v0.6.12.tar.gz tar -zxvf node-v0.6.11.tar.gz cd node-v0.6.11 ./configure --prefix=$HOME/local/node make make install echo 'export PATH=$HOME/local/node/bin:$PATH' >> ~/.profile echo 'export NODE\_PATH=$HOME/local/node:$HOME/local/node/lib/node\_modules' >> ~/.profile source ~/.profile \[/code\]

Part 3 - Installing Etherpad Lite and running it \[code\] git clone git://github.com/Pita/etherpad-lite.git etherpad-lite/bin/run.sh # You will be prompted to type Etherpad Lite rocks my socks. \[/code\]

**You are now finished installing and Etherpad Lite should be running, you should be able to access it on http://localhost:9001**

Only if you have an old version of Debian (Lenny) or Ubuntu then you will need to install sqllite from backports. To do open /etc/apt/sources.list and add:

\[code\] deb http://backports.debian.org/debian-backports lenny-backports main \[/code\]

Save and close the file then type \[code\] apt-get update apt-get -t lenny-backports install libsqlite3-dev \[/code\]

You may need to rebuild your modules if you have an error, to do this do an rm -Rf node\_modules and run the startup script (run.sh) again!

[Want to run Etherpad Lite as a service? Follow this guide](https://github.com/Pita/etherpad-lite/wiki/How-to-deploy-Etherpad-Lite-as-a-service "Etherpad Lite as a Service"). Make sure you do a chown -R etherpad-lite on the etherpad-lite folder if you have run it as root or any other user before hand..
