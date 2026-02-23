---
title: "Title:  Fixing pro domain login for Etherpad installations running on XX YY ZZ type hosting IE prodomain.etherpad.mydomain.com"
date: 2010-03-25
---

Overview:

This is a partial fix to the problem that etherpad assumes to be installed on a domain of the form x.y

This patch makes it work for an z.x.y domain, probably breaking it for x.y domains (but I don't know javascript enough to be sure - parts\[2\] will be undefined though)

To make it properly we should check how many elements there are into parts\[\]. Until this is done this is a mere workaround.

Modified code:  (pro\_utils.js) - Usually found in /usr/local/etherpad/trunk/etherpad/src/etherpad/pro

Lines 47 - 54 should be modified to read:

function getRequestSuperdomain() {

var parts = request.domain.split('.');

parts.reverse();

if (parts\[0\] == ".") {

parts.shift();

}

return \[parts\[2\], parts\[1\], parts\[0\]\].join('.');

}

Google group discussion talking (without presenting a solution) of this problem is at this link:

http://groups.google.com/group/etherpad-open-source-

discuss/browse\_thread/thread/a8c5ceda3186845d/abebff9b8d737428?#abebff9b8d737428

**Overview:**

This is a partial fix to the problem that etherpad assumes to be installed on a domain of the form x.y

This patch makes it work for an z.x.y domain, probably breaking it for x.y domains (but I don't know javascript enough to be sure - parts\[2\] will be undefined though)

To make it properly we should check how many elements there are into parts\[\]. Until this is done this is a mere workaround.

**Modified code:** (pro\_utils.js) - Usually found in /usr/local/etherpad/trunk/etherpad/src/etherpad/pro

Lines 47 - 54 should be modified to read:

\[javascript\]

function getRequestSuperdomain() {

var parts = request.domain.split('.');

parts.reverse();

if (parts\[0\] == ".") {

parts.shift();

}

return \[parts\[2\], parts\[1\], parts\[0\]\].join('.');

}

\[/javascript\]

[Google group discussion talking (without presenting a solution) of this problem](http://groups.google.com/group/etherpad-open-source-discuss/browse_thread/thread/a8c5ceda3186845d/abebff9b8d737428?#abebff9b8d737428)
