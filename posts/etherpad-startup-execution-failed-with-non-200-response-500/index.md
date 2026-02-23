---
title: "Etherpad Startup execution failed with non-200 response: 500"
date: 2010-06-29
categories: 
  - "etherpad"
tags: 
  - "mysql"
---

Etherpad won't start and errors with output

> Etherpad Startup execution failed with non-200 response: 500

**Cause:**

Etherpad can't talk to MySql

**Things to check:**

1\. Your /etc/hosts

2\. Your MySQL conf under networking - /etc/mysql/my.cnf

3\. Your MySQL conf  bind-address - /etc/mysql/my.cnf

4\. The etherpad.SQL\_JDBC\_URL value in /usr/share/etherpad/etherpad/etc/etherpad.local.properties

Make sure these are correct then restart mysql.  Don't assume that connecting with mysql -uroot -ppassword etherpad is a good test.

[![Enhanced by Zemanta](images/zemified_e.png)](http://www.zemanta.com/ "Enhanced by Zemanta")
