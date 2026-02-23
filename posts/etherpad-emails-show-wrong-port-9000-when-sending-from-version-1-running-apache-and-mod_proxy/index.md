---
title: "Etherpad emails show wrong port (9000) when sending from version 1 running apache and mod_proxy"
date: 2010-05-06
categories: 
  - "etherpad"
---

Etherpad emails may show as port 9000 if you are using mod\_proxy(apache) in front of etherpad.

If this is a problem simply edit:

/usr/share/etherpad/etherpad/etc/etherpad.local.properties replacing hidePorts = false with hidePorts = true
