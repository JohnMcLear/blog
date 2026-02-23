---
title: "Setting your own Title name in Etherpad Lite"
date: 2012-02-18
categories: 
  - "etherpad"
---

Replacing the title in Etherpad Lite with Your own title is just a little command.

Open up custom/pad.js

Edit customStart to read..

\[code\] customStart(){ document.title= "Your Title Here" } \[/code\]

To change the title for the start page just do the same in index.js
