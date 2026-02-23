---
title: "Etherpad minimum requirements (Memory / RAM)"
date: 2010-02-24
categories: 
  - "etherpad"
---

[](http://4.bp.blogspot.com/_NislCXjnul0/S4VVYGV4NXI/AAAAAAAACrc/OGcsGSrsbxQ/s1600-h/memory_corsair%5B1%5D.gif)**Minimum:** 2 GB (It will run on 1 Gig but do you really want to allocate a JVM to use ALL of your ram?)

**Recommended:** 4GB+ Depending on # of pads & concurrent connections.

**I would recommend not running a production Etherpad service on a Virtual PC / VPS** or any thing that will interfere with Java accessing the machines memory.  You may struggle to build on a VPS depending on your providers swap memory space settings.

Just a quick one, worth posting cause it's not well documented.
