---
title: "Securing Etherpad admin with a password"
date: 2009-12-22
categories: 
  - "etherpad"
---

Etherpad is insecure by default.

  

To secure etherpad edit

  

/usr/local/etherpad/trunk/etherpad/etc/etherpad.localdev-default.properties

  

Add the line (if it doesn't already exist - it exists by default)

  

etherpad.adminPass = password

  

Replace password with your password

  

Edit the line

  

etherpad.isProduction = false

  

To read

  

etherpad.isProduction = true

  

Save the file and restart etherpad.
