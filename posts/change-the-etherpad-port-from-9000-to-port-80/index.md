---
title: "Change the etherpad port from 9000 to port 80"
date: 2009-12-20
categories: 
  - "etherpad"
  - "google"
  - "port"
---

edit etherpad/etc/etherpad.localdev-default.properties

\# replace

listen = 9000

\# with

listen = 80

  

\# Restart etherpad

bin/run-local.sh
