---
title: "npm install ReferenceError: console is not defined"
date: 2011-01-29
categories: 
  - "developer"
  - "developing"
  - "ict"
  - "javascript"
  - "nodejs"
---

Trying to install [npm](http://npmjs.org/) with: \[bash\]curl http://npmjs.org/install.sh | sh\[/bash\]

Returns: \[code\]ReferenceError: console is not defined:\[/code\]

Cause: NodeJS not properly installed.

Solution: Goto [NodeJS download](http://nodejs.org/#download) and get the latest tar package and install it yourself. Usual install procedure: \[bash\] tar -zxvf node-whatever.tar.gz cd node-whatever ./configure make make install \[/bash\]

Now try again and it should work :)
