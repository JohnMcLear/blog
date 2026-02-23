---
title: "Etherpad Nginx Config"
date: 2010-08-11
categories: 
  - "etherpad"
  - "ict"
---

**Paste to /etc/nginx/proxy.conf**

\# proxy.conf proxy\_redirect off; proxy\_set\_header Host $host; proxy\_set\_header X-Real-IP $remote\_addr; proxy\_set\_header X-Forwarded-For $proxy\_add\_x\_forwarded\_for; client\_max\_body\_size 10m; client\_body\_buffer\_size 128k; proxy\_connect\_timeout 90; proxy\_send\_timeout 90; proxy\_read\_timeout 90; proxy\_buffer\_size 4k; proxy\_buffers 4 32k; proxy\_busy\_buffers\_size 64k; proxy\_temp\_file\_write\_size 64k;

**Paste to /etc/nginx/sites-enabled/mysite**

server { listen %Replace\_with\_your\_adapters\_IP%:80; server\_name mydomain.com; access\_log /var/log/nginx/mydomain.com.access.log; error\_log /var/log/nginx/mydomain.com.error.log; location / { proxy\_pass http://localhost:9000/; include /etc/nginx/proxy.conf; } }

**Restart nginx**

/etc/init.d/nginx restart
