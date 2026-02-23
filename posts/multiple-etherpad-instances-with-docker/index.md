---
title: "Multiple Etherpad instances on one host with Docker"
date: 2015-04-24
categories: 
  - "etherpad"
---

These Docker CLI commands will bring up multiple containers / instances on one host..

\[code\] sudo docker run -d -e MYSQL\_ROOT\_PASSWORD=password --name ep\_mysql mysql sudo docker run -d --link=ep\_mysql:mysql -p 9001:9001 tvelocity/etherpad-lite

sudo docker run -d -e MYSQL\_ROOT\_PASSWORD=password --name ep\_mysql2 mysql sudo docker run -d --link=ep\_mysql2:mysql -p 9002:9001 tvelocity/etherpad-lite \[/code\]

This will bring up two unique Etherpad instances on ports 9001 and 9002. Each instance will have it's own MySQL database.
