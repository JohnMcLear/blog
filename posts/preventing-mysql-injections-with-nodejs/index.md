---
title: "Preventing MySQL Injections with NodeJS"
date: 2011-03-22
categories: 
  - "nodejs"
---

The [node-mysql](https://github.com/felixge/node-mysql) module has an [escape function](https://github.com/felixge/node-mysql/blob/master/Readme.md):

> **client.escape(val)** Escapes a single val for use inside of a sql string.
