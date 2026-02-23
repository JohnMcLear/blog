---
title: "Configuring DNS CNAME records for Google Apps Education Edition"
date: 2009-11-24
categories: 
  - "apps"
  - "google"
  - "ict"
  - "primary"
  - "primary-email"
  - "primary-school-email"
  - "primary-school-ict"
  - "school-email"
---

**What am I doing any why?**

A DNS entry is required so teachers and pupils can access your Google Apps. A DNS entry is basically a lookup record for your domain that will allow users to type in the URL [http://docs.yourdomain.com](http://docs.yourdomain.com/) and access their Google Apps.

**Sounds good, let’s get started!**

Find out who manages your domain or if you already know log into your Control Panel. If you don’t know then visit [http://whois.domaintools.com/](http://whois.domaintools.com/) and type your domain in. If the previous website didn’t work for your domain try [http://www.nominet.org.uk/](http://www.nominet.org.uk/) using the whois box on the right to type your domain name into. Your domain name will need to be in the format yourdomain.com NOT [http://yourdomain.com](http://yourdomain.com/). Your domain control panel will be provided by the Domain Registrar

Once you have logged into your Domain Control Panel you will need to create some DNS records. This varies on different providers, but it is the same procedure throughout.

Instructions for DNS record changes (Email this to your DNS provider if you wish that they complete this step).

1. Create a CNAME record called “sites” that points to ghs.google.com
2. Create a CNAME record called “docs” that points to ghs.google.com
3. Create a CNAME record called “chat” that points to ghs.google.com

Any of the above can be skipped if you don’t want to use the corresponding item.

If you chose to use GMail you can add a CNAME called mail, you will also need to configure MX accounts, this task will vary from school to school, again we recommend schools use [Primary Email](http://primaryemail.co.uk).

**[Continue to Registering Google Apps Education Edition](https://mclear.co.uk/2009/11/24/registering-google-apps-education-edition-for-your-primary-school/)** **[à](https://mclear.co.uk/2009/11/24/registering-google-apps-education-edition-for-your-primary-school/)**
