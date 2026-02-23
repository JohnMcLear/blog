---
title: "Wordpress Varnish Cache Config / VCL"
date: 2011-10-05
categories: 
  - "ict"
  - "varnish"
  - "wordpress"
---

Note: [I am now providing VCLs in separate branches on github as the Varnish VCL syntax has changed](https://github.com/johnmclear/Wordpress-Varnish-VCL).

[Thanks to scoof for documenting the Varnish VCL changes.](https://www.varnish-cache.org/docs/trunk/installation/upgrade.html)

## What is this for non-technical folks?

Wordpress sucks at delivering the same content over and over again, actually, I should rephrase that, wordpress rocks 99% of the time but if you serve a page over and over again it will quickly exhaust your servers resource which will mean wordpress will go slow.  Varnish Cache speeds up Wordpress by serving pages from memory instead of doinmagicg a bunch of hard work.

## Why should I use this VCL?

I have done a number of different VCLs that can be used with varnish and wordpress but this is the final revision for now. It is designed for Varnish 2 but should work on 3 with no to very little modifications, I have tweaked this VCL over a few years and I'm finally happy with it.

Features:

- Supports multiple back-ends
- Supports round-robin
- Supports Purging using the [Varnish Wordpress plugin](http://wordpress.org/extend/plugins/wordpress-varnish/ "Wordpress Varnish Plugin")
- Supports logged in users
- Supports password protected pages
- Supports Mobile devices
- Provides long client side caching
- Forwards the correct client IP to the web daemon.
- Doesn't cache 404s, 503, 500 etc.
- Doesn't cache wp-admin, login, preview, signup
- Caches static objects such as images
- Supports Multisite
- Includes debug/log messages.
- Really clean code, proper tabbing etc.

## Requirements

[Varnish](https://www.varnish-cache.org/), [Wordpress](http://wordpress.org), The [Varnish Wordpress plugin](http://wordpress.org/extend/plugins/wordpress-varnish/ "Wordpress Varnish Plugin") installed and working, [mod\_rpaf](http://stderr.net/apache/rpaf/) installed in apache or an nginx equivalent.

## Why have I made this?

I was going to make a VCL generator but then I remembered most people will use this VCL as a point of reference and I'm lazy, let's face it, being lazy is the biggest factor in me backing out of making a generator. The varnish configs I have done before have been overly verbose for what they did and rewriting them and cleaning them up means this config is much easier to understand and modify. Adding logging means that you can easily use [varnishlog to debug](https://mclear.co.uk/2011/04/25/varnishlog-cheat-sheet/ "Varnishlog Cheat sheet") any problems you have.

## What isn't included?

I didn't include Custom error messages in this VCL.  It's not because I'm lazy, it's because custom error messages put a lot of cruft into the VCL and if you want custom error messages you should see this article.

## Let me at it!

[Varnish v3](https://github.com/johnmclear/Wordpress-Varnish-VCL/tree/Varnish3) [Varnish v3.03](https://github.com/johnmclear/Wordpress-Varnish-VCL/blob/Varnish303/default.vcl) **Which version of Varnish am I running?** \[code\]varnishd -V\[/code\]

## What do I need to change?

Search and replace myFirstServer and mySecondServer with your server names adding new backends where required. Make sure new backends are added to the round-robin cluster and the purge list.

Once you are happy with your VCL save it in as /etc/varnish/default.vcl (remember to make a backup of your original file) and restart Varnish.  Any problems try to debug yourself but if you are stuck just give me a shout, I will be happy to help!
