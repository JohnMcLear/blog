---
title: "Etherpad Lite Java Client"
date: 2012-01-02
categories: 
  - "features"
---

[A Java client for Etherpad Lite’s HTTP JSON API.](https://github.com/jhollinger/java-etherpad-lite)

Example:

EPLiteClient api = new EPLiteClient(“http://etherpad.mysite.com”, “FJ7jksalksdfj83jsdflkj”);  
HashMap pad = api.getText(“my\_pad”);  
String pad = pad.get(“text”).toString();

[Report Post As Inappropriate](http://etherpad.org?moderation_action=report_form&object_type=post&object_id=548&width=250&height=300 "Report Post As Inappropriate")
