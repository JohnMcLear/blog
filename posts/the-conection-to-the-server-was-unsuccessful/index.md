---
title: "The conection to the server was unsuccessful"
date: 2013-05-21
categories: 
  - "cordova"
---

The application Error \[code\] The conection to the server was unsuccessful (file://android\_asset/www/index.html) \[/code\]

Was caused by a script being inaccessible during the page load..

For me changing: \[code\] <script src="http://oldplace:8080/target/target-script-min.js"></script> \[/code\]

To \[code\] <script src="http://newplace:8080/target/target-script-min.js"></script> \[/code\]

Fixed it
