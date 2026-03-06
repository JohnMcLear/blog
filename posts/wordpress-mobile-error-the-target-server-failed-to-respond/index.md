---
title: "Wordpress mobile error: \"the target server failed to respond\""
date: 2011-05-01
categories: 
  - "varnish"
  - "wordpress"
  - "wordpress-multi-user"
  - "wpmu"
---

When joining a new mobile device to wordpress it looks like the first request is a GET request.

My Varnish config only included support for POST requests to xmlrpc.php

I updated my config to read:



```
// set backend, pipe, strip cookies from xmlrpc if (req.request == "POST" && req.url ~ "xmlrpc.php") {remove req.http.cookie;set req.backend = mainserver;return(pipe);} if (req.request == "GET" && req.url ~ "xmlrpc.php") {remove req.http.cookie;set req.backend = mainserver;return(pipe);}
```



and it sorted it! Huraa
