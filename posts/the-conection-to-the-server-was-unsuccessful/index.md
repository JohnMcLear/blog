---
title: "The conection to the server was unsuccessful"
date: 2013-05-21
categories: 
  - "cordova"
---

The application Error 

```
The conection to the server was unsuccessful (file://android\_asset/www/index.html)
```



Was caused by a script being inaccessible during the page load..

For me changing: 

```
<script src="http://oldplace:8080/target/target-script-min.js"></script>
```



To 

```
<script src="http://newplace:8080/target/target-script-min.js"></script>
```



Fixed it
