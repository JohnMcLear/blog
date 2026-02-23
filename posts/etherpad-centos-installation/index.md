---
title: "Etherpad CentOS installation"
date: 2010-03-09
categories: 
  - "centos"
  - "etherpad"
---

[![](images/etherpadsnap.png)](http://4.bp.blogspot.com/_NislCXjnul0/S5aAuQoComI/AAAAAAAACtw/z7xtBkgpL-w/s1600-h/etherpadsnap.png)

Nuba has written a fantastic guide for installing Etherpad onto CentOS - I recommend you follow that before reading this.

My problem is that the JAR wouldn't compile on my box.

I ran into a problem, my box wouldn't let me use fsc (Fast Scala Compiler) so I had to change the fsc references to use scalac(Scala Compiler) then I could compile the JAR.  I also had to use JAR instead of FastJAR

This isn't a guide as such, just an overview of how I fixed the problems I had.
