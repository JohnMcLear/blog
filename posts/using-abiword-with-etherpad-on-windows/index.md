---
title: "Using Abiword with Etherpad on Windows"
date: 2011-12-04
categories: 
  - "etherpad"
---

Step 1. [Download and install Abiword for Windows](http://www.abisource.com/download/)

Step 2. [Download and install Notepad++](http://notepad-plus-plus.org/download/)

Step 3. [Download and extract Etherpad](http://etherpad.org/etherpad-lite-win.zip)

Step 4. Enter the Etherpad folder, right click settings.json - Edit the file in Notepad++

Step 5. Find the line 

```
abiword : null
```



Step 6. Change this line to: 

```
"abiword" : "C:\\\\Program Files (x86)\\\\AbiWord\\\\bin\\\\AbiWord.exe"
```



Step 7. Run Etherpad.
