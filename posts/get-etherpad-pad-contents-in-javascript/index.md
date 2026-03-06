---
title: "Get Etherpad Pad contents in Javascript"
date: 2012-12-17
categories: 
  - "etherpad"
  - "javascript"
  - "jquery"
tags: 
  - "etherpad"
---



```
function getElementByIdInFrames(id, base) { var el; if(el = base.document.getElementById(id)) { return el; }

for(var i = 0, len = base.frames.length; i < len; i++) { if(el = getElementByIdInFrames(id, base.frames\[i\])) { return el; } } } getElementByIdInFrames("innerdocbody", window).innerHTML;
```



This means you can also do... 

```
getElementByIdInFrames("innerdocbody", window).innerHTML = "Superducky";
```



And if you want to use jQuery a one liner will sort you out..



```
console.log($('iframe\[name="ace\_outer"\]').contents().find('iframe').contents().find("#innerdocbody"));
```



**NOTE: Due to a change in the jQuery API a . after iframe was removed -- 10/02/2013**

Means you can do..



```
$('iframe\[name="ace\_outer"\]').contents().find('iframe').contents().find("#innerdocbody").html("Superducky");
```



Thanks to Mark Fisher for the jQuery example
