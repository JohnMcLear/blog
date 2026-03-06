---
title: "Etherpad Lite .doc/.pdf import/export"
date: 2011-11-22
categories: 
  - "etherpad"
---

So you have installed etherpad lite and you want to add support for importing and export pdf and .doc files?   It's easy.

Drop to shell and type



```
apt-get install abiword
```



Next open up your settings.json and change: 

```
"abiword" : null,
```

 to 

```
"abiword" : "/usr/bin/abiword",
```



[See this as a main reference document](https://github.com/Pita/etherpad-lite/wiki/How-to-enable-importing-and-exporting-different-file-formats-in-Ubuntu-or-OpenSuse-or-SLES-with-AbiWord)
