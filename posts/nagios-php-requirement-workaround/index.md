---
title: "Nagios PHP requirement workaround"
date: 2010-04-27
tags: 
  - "nagios"
  - "php"
  - "programming"
---

\[caption id="" align="alignright" width="180" caption="Image via Wikipedia"\]\[/caption\]

Nagios is server monitoring software used by many schools worldwide, we use it to monitor all of our services/sites.  Here is a conversation from IRC that discusses if Nagios requires PHP or not.

> 16:47\] <mischko> Nagios now requires PHP?
> 
> \[16:48\] <keith4> "requires" is a strong word
> 
> \[16:49\] <LzrdKing> apparently, it depends on your distro, too
> 
> \[16:49\] <mischko> compiling from source version 3.2.1 no longer includes a few html files but php instead.
> 
> \[16:49\] <keith4> he must be talking about building from source
> 
> \[16:50\] <keith4> right. then... sure, it requires php
> 
> \[16:50\] <mischko> Is there a way to do 3.2.1 without php?
> 
> \[16:51\] <keith4> what distro?
> 
> \[16:52\] <mischko> compiled apache on rhel4
> 
> \[16:52\] <keith4> why not use the RPMs?
> 
> \[16:52\] <mischko> need newer version of apache than is available via rpm in our environment.
> 
> \[16:55\] <mischko> The only thing it seems to be needed for is the access to cgi\_base\_url config.
> 
> \[16:56\] <Valcor> mischko: pretty much
> 
> \[16:57\] <mischko> wow. I'm surprised they put in a PHP requirement for \_that\_ alone.
> 
> \[16:59\] <LzrdKing> keith4: didn't you say debian doesn't have the php requirement?
> 
> \[17:06\] <dnsmichi|home> the php requirement only is for the update checker, nothing else
> 
> \[17:06\] <dnsmichi|home> which is rather useless when using a package
> 
> \[17:08\] <mischko> dnsmichi, It's also used in a few other places. I'm editing it all out.
> 
> \[17:09\] <dnsmichi|home> well ok then hf :)
> 
> \[17:10\] <mischko> that was easy. Let's hope they don't increase use of PHP in the future.
> 
> 14:12\] <dnsmichi> CapnDan: try a debian package - they remove php
> 
> \[14:12\] <dnsmichi> http://git.debian.org/?p=pkg-nagios/pkg-nagios3.git;a=blob;f=debian/patches/55\_remove\_php.dpatch;h=e8ff8255deed83f5287e17669782c06843792663;hb=HEAD
> 
> \[14:12\] <dnsmichi> :)
> 
> 14:13\] <CapnDan> dnsmichi: eh, I'm installing on Solaris.
> 
> \[14:14\] <dnsmichi> well then you might consider the patch on the git repo
> 
> \[14:14\] <CapnDan> I will take a look at it, thanks!

![Reblog this post [with Zemanta]](images/reblog_e.png)
