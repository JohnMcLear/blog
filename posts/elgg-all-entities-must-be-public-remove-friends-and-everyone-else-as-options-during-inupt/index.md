---
title: "Elgg - All entities must be public - Remove friends and everyone else as options during inupt"
date: 2009-06-21
categories: 
  - "access"
  - "allplugin"
  - "elgg"
  - "friends"
  - "primary-school-teaching"
  - "public"
  - "site-access"
---

Wow possibly the worst topic ever for one of my posts :P

  

This is relevant if

  

a) You use Elgg

b) You want all users to only be able to post as public

c) You have the allpublic elgg plugin

  

If not you won't be interested..

  

Basically, the array that holds the values takes 0,1,2 then you drop out 0,1 (this is default behavior in the allpublic plugin).

  

For some weird reason this leaves behind "Friends" as an option, this is not desirable behavior and the fix is to remove -2 ( I know wth were they thinking) from the array. Use this line of code in the allplugin access.php:

  

unset($vars\['options'\]\[-2\]);

  

Put that with the rest of the unset's in the plugin.

  

Full file path will be mod/allpublic/views/default/input

  

As another note, if -2 isn't right for you just echo out the $key value from the array like..

  

{$option . $key} then you will get the name of the option and the key/id.
