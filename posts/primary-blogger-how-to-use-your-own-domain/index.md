---
title: "Primary Blogger - How to use your own domain"
date: 2009-11-28
categories: 
  - "blog"
  - "blogging"
  - "domain"
  - "ict"
  - "primary-blogger"
  - "primary-school"
  - "website"
---

So you want to move your current website to primary blogger or use a domain you own.

An Example of this is [http://www.wilsdenprimary.co.uk](http://www.wilsdenprimary.co.uk/)

You can do this for free by accessing your DNS control panel and creating a new A record for your domain.

Note: Having 2 entries means if one fails the visitor will automatically try the next. It also means we can load balance (Which is nice because PrimaryBlogger is huge).

Add entries called www that point to 94.136.53.6, 217.199.169.145 & 109.107.35.108 (Or modify your existing A record to point to these).

If you need assistance with this step please get in touch with [Primary Technology](http://primaryt.co.uk/contact.html).

Once you have set your DNS then log into your Primary Blogger Dashboard by visiting your blog and clicking Site Admin.

1. Click Tools
2. Click Domain Mapping
3. Under add a new domain type in your domain name.
4. Click OK
5. Wait 24 hours.

You may want to [let us know](http://primaryt.co.uk/contact.html) if you are going to do this.. Why? I hear you ask.. Well we have some clever caching in place that speeds up websites based on their hostname and if your hostname is not included it may mean your PrimaryBlogger blog does some weird things..
