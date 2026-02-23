---
title: "Etherpad with Active Directory (LDAP/AD)"
date: 2010-02-03
categories: 
  - "ad"
  - "etherpad"
  - "ldap"
  - "shibboleth"
  - "single-sign-on"
  - "sso"
---

So you want to host your own Etherpad deployment and you want to tie it into your schools AD/LDAP/Active directory? Below are the basic instructions for how to accomplish this. [Alternatively you can pay us to do it.](http://primaryt.co.uk/contact.html)

  

**Get the patch**

lynx https://gist.github.com/10061b4b213619816db5

  

**Get the etherpad source (warning- may take some time- go make a cuppa tea)**

hg clone https://etherpad.googlecode.com/hg/ etherpad

  

**Go to the etherpad folder**

cd etherpad

  

**Extract the patch**

tar -xvz --strip-components=1 -f ../gist10061b4b213619816db5-e60df95e16c09700b4cf07cd87b9732dd7b15ace.tar.gz

  

**Apply the patch**

patch -p1 < ldap\_support.patch  

  

**Set your superdomain**

nano trunk/etherpad/src/etherpad/globals.js

_add yourdomain.whatever to the SUPERDOMAINS_

  

**Edit pro\_accounts.js**

nano trunk/etherpad/src/etherpad/pro/pro\_accounts.js

  

**Change directory**

cd trunk/etherpad

  

**Add the useLdapconf to the config**

echo "etherpad.useLdapConfiguration = ./etc/json.config" >> etc/etherpad.localdev-default.properties

  

**Edit json.config**

nano etc/json.config

  

_Paste in (you need the {}'s):_

_{_

_"url" : "ldap://localhost:10389",_

_"principal" : "uid\=admin,ou\=system",_

_"password" : "secret",_

_"rootPath" : "ou\=users,ou\=system",_

_"userClass" : "person",_

_"nameAttribute" : "displayname",_

_"ldapSuffix" : "@ldap"_

_}_

  

_Replacing the above with your settings._

  

**Build your etherpad**

bin/rebuildjar.sh

  

**Test your etherpad**

bin/run-local.sh

  

**Browse to http://yourdomain.com:9000/ep/pro-account/sign-in**

  

**Type in your email address (of the user in ldap) and password**

  

Fin! Credit to Elliot Kroo and Marcio Starke - discussed further in [this google group](http://groups.google.com/group/etherpad-open-source-discuss/browse_thread/thread/b0907ca86976f913).

  

Shibboleth integration coming mid 2010 (if anyone wants to fund this please [get in touch](http://primaryt.co.uk/contact.html)!)
