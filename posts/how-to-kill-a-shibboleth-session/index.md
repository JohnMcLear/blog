---
title: "How to kill a shibboleth session"
date: 2009-11-11
categories: 
  - "shibboleth"
---

**

Kill an SP session with a HTML redirect:

**

<meta http-equiv="REFRESH" content="0;url=https://shib.example.org/Shibboleth.sso/Logout">

Kill an SP session by visiting a URL:

https://shib.example.org/Shibboleth.sso/Logout

  

****

Kill an IDP session:

**

Single Log off is not fully supported in Shibboleth, it is recommended you redirect a user to a page requesting they close their browser window.

  

**Note:** Don't forget to replace example.org with your domain

**
