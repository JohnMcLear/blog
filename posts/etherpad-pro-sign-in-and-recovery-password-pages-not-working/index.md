---
title: "Etherpad Pro Sign In and Recovery password pages not working"
date: 2009-12-21
categories: 
  - "etherpad"
---

Edit /usr/local/etherpad/trunk/etherpad/src/templates/main/pro\_signup\_body.ejs

Replace

Existing Users: Sign in here (and all the surrounding html)

with

Existing Users: Visit your pad URL to sign in: (ie http://yourpad.yourhosturl.com)
