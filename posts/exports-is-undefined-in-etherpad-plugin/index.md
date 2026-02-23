---
title: "exports is undefined in Etherpad plugin"
date: 2013-01-31
tags: 
  - "etherpad"
---

Add the below to the top of your file. \[code\] if(typeof exports == 'undefined'){ var exports = this\['mymodule'\] = {}; } \[/code\]
