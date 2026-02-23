---
title: "Upgrading Etherpad if you installed with Git"
date: 2012-09-03
categories: 
  - "etherpad"
---

\[code\] /etc/init.d/etherpad-lite stop git pull /etc/init.d/etherpad-lite start \[/code\]

If you installed from the tar ball then grab the latest tar and extract it over your current install.

**Make sure you always back up your dirty.db if you use that.**

As far as database migrations we are hoping that the current schema wont need any modifications, if so we will try to handle this with upgrade scripts that will run automatically.
