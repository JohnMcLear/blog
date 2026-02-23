---
title: "Etherpad email is not working"
date: 2009-12-21
categories: 
  - "email"
  - "etherpad"
---

If you have problems with emails not coming from your etherpad deployment try adding the line

  

smtpServer = localhost:25

  

to

  

/usr/local/etherpad/trunk/etherpad/etc/etherpad.localdev-default.properties

  

and restarting the etherpad daemon

  

\# then

  

telnet localhost 25

  

if you get a Connect message then good times, if not, install an MTA such as postfix. By default my box had exim4 on so I did

  

apt-get remove exim4

  

\# then

  

apt-get install postfix

  

Cause I prefer postfix :)
