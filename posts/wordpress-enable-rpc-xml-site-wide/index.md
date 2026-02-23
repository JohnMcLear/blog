---
title: "Wordpress enable RPC XML site wide."
date: 2010-07-03
---

Create a plugin in wordpress and paste in:

add\_filter( 'pre\_option\_enable\_xmlrpc', create\_function('$a', 'return true;') );

OR

[Download & install this plugin](http://primaryschoolict.com/rpcxml.zip)
