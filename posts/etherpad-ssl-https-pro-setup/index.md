---
title: "Etherpad SSL Https pro setup"
date: 2009-12-21
categories: 
  - "etherpad"
  - "primarypad"
  - "pro"
---

Don't wanna use SSL / https for etherpad? Fine.

Edit trunk/etherpad/src/etherpad/pro/pro\_accounts.js

Replace 'https://', httpsHost(pro\_utils.getFullProHost()), '/ep/account/sign-in?',

with

'http://', httpHost(pro\_utils.getFullProHost()), '/ep/account/sign-in?',

Edit /usr/local/etherpad/trunk/etherpad/src/etherpad/control/pro/pro\_main\_control.js

Replace

evalExpDate: licensing.getLicense().expiresDate,

with

// evalExpDate: licensing.getLicense().expiresDate,

See my [other etherpad blog posts](https://mclear.co.uk/?s=etherpad) for other help in getting pro working
