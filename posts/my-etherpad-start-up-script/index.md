---
title: "My Etherpad start up script"
date: 2010-01-20
categories: 
  - "etherpad"
---

I like my etherpad to run in a screen so I can jump in and out:

I know it's messy but it's all I have. I recommend not using this on a box running anything other than etherpad.  I paste this to /etc/init.d/etherpad and chmod it

\[bash\]

/etc/init.d/nrpe start

killall java -9

killall soffice.bin

/usr/bin/soffice -headless -nofirststartwizard -accept="socket,host=localhost,port=8100;urp;StarOffice.Service" &

cd /usr/local/etherpad/trunk/etherpad

screen bin/run-local.sh

\[/bash\]
