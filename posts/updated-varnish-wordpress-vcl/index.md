---
title: "Updated Varnish Wordpress VCL"
date: 2011-02-27
categories: 
  - "developer"
  - "ict"
  - "varnish"
  - "wordpress"
---

## [THIS VARNISH CONFIG HAS BEEN UPDATED AND IS AVAILABLE HERE](https://mclear.co.uk/2011/10/05/wordpress-varnish-cache-config-vcl/ "Wordpress Varnish VCL")

I have been tweaking a varnish vcl config for Wordpress for quite some time and I wanted to share it..  Thanks to everyone(especially DocWilco)  in #varnish on Linpro IRC for helping

**Features:**

1. Load balancing
2. Probing
3. Does not cache wp-admin
4. Puts all uploads/content requests onto one server
5. Purging
6. Long timeout for file uploads
7. XML RPC support
8. Custom 404 and 500 message
9. Forwards user IP address for comments

First of all.. Let's define some backends..

\[code\] // BACKEND CONFIGS backend server1 { .host = "server1.example.com"; .port = "8080"; .probe = { .url = "/"; .interval = 5s; .timeout = 1 s; .window = 5; .threshold = 3; } // we include time outs so uploads don't time out .connect\_timeout = 600s; .first\_byte\_timeout = 600s; .between\_bytes\_timeout = 600s; }

backend server2 { .host = "server2.example.com; .port = "8080"; .probe = { .url = "/"; .interval = 5s; .timeout = 1 s; .window = 5; .threshold = 3; } // we include time outs so uploads don't time out .connect\_timeout = 600s; .first\_byte\_timeout = 600s; .between\_bytes\_timeout = 600s; }

// define round-robin for backends director cluster round-robin { {.backend = server1;} {.backend = server2;} }

// set the servers wordpress can purge from acl purge { "server1.example.com"; "server2.example.com"; }

sub vcl\_fetch { if (req.http.host ~ "ourdomain.com" || req.http.host ~ "ourotherdomain.com" // don't cache wp-admin ever cause that's not cool && req.url !~ "wp-admin") { // we cache these domains for 8 hours unless they are purged. set beresp.ttl = 8h; set beresp.grace = 600s; // don't cache 404 or 500 errors if (beresp.status == 404 || beresp.status >= 500) { set beresp.ttl = 0s; } } // tell all of the files to use server1 if (req.url ~ "files") {set req.backend = server;set beresp.ttl = 8h;} }

sub vcl\_recv { // Purge Wordpress requests for purge if (req.request == "PURGE") { if (!client.ip ~ purge) { error 405 "Not allowed."; } purge("req.url == " req.url " && req.http.host == " req.http.host); error 200 "Purged."; }

// forward the client IP so comments show up properly set req.http.X-Forwarded-For = client.ip;

// let server2 handle all feeds if (req.url ~ "/feed/") {set req.backend = server2;}

// server1 must handle file uploads if (req.url ~ "media-upload.php" || req.url ~ "file.php" || req.url ~ "async-upload.php") {set req.backend = server1;return(pass);}

// server1 can serve all files. if (req.url ~ "/files/") {set req.backend = server1;}

// do not cache xmlrpc.php if (req.url ~ "xmlrpc.php") {return(pass);}

// strip cookies from xmlrpc if (req.request == "GET" && req.url ~ "xmlrpc.php") remove req.http.cookie;return(pass);}

// caching these files is fine if (req.http.Accept-Encoding) { if (req.url ~ "\\.(jpg|png|gif|gz|tgz|bz2|lzma|tbz)(\\?.\*|)$") { remove req.http.Accept-Encoding; } elsif (req.http.Accept-Encoding ~ "gzip") { set req.http.Accept-Encoding = "gzip"; } elsif (req.http.Accept-Encoding ~ "deflate") { set req.http.Accept-Encoding = "deflate"; } else { remove req.http.Accept-Encoding; } }

// Remove cookies and query string for real static files if (req.url ~ "^/\[^?\]+\\.(jpeg|jpg|png|gif|ico|js|css|txt|gz|zip|lzma|bz2|tgz|tbz|html|htm)(\\?.\*|)$") { unset req.http.cookie; set req.url = regsub(req.url, "\\?.\*$", ""); }

// Remove cookies from front page if (req.url ~ "^/$") { unset req.http.cookie; }

// if the request is for our domain and not for wp-admin then load balance it to a server that is responding or send it to server1 if (req.http.host ~ "ourdomain.com" || req.http.host ~ "ourotherdomain.com" && req.url !~ "wp-admin") { set req.http.X-Forwarded-For = client.ip; set req.backend = cluster; } else { set req.http.X-Forwarded-For = client.ip; set req.backend = server1; }

// Custom error message sub vcl\_error { if(obj.status == 404) { set obj.ttl = 0s; set obj.http.Content-Type = "text/html; charset=utf-8"; synthetic {" <!--?xml version="1.0" encoding="utf-8"?-->

"} obj.status " " obj.response {" </pre> <div style="background-color: white;"><center> <img src="http://whatever.com/heavyload.jpg" alt="" width="600px" /></center> <h1>This page is unavailable</h1> If you are seeing this page, either maintenance is being performed or you are trying to access a file that doesn't exist. Please <a href="http://whatever.com/contact.html">contact us</a> if you believe this is an error <h2>Error "} obj.status " " obj.response {"</h2> "} obj.response {" on server "} req.backend {" <address><a href="http://whatever.com/">Us.</a></address></div> <pre> "}; return (deliver); error 404 "Not found"; } else { set obj.http.Content-Type = "text/html; charset=utf-8"; synthetic {" <!--?xml version="1.0" encoding="utf-8"?--> "} obj.status " " obj.response {"

</pre> <div style="background-color: white;"><center> <img src="http://whatever.com/heavyload.jpg" alt="" width="600px" /></center> <h1>This website is unavailable</h1> If you are seeing this page, either maintenance is being performed or something really bad has happened. Try returning in a few minutes. If you still see this error in a few minutes please <a href="http://whatever.com/contact.html">contact us</a> <h2>Error "} obj.status " " obj.response {"</h2> "} obj.response {" on server "} req.backend {" <address><a href="http://whatever.com/">Us.</a></address></div> <pre> "}; return (deliver); } } \[/code\]
