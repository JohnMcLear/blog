---
title: "Script to get an email when a new property in your area is registered on Gumtree"
date: 2012-04-17
categories: 
  - "developer"
  - "developing"
---

This script will send you an email when a new property in your area comes up on twitter.. Replace shoreditch with the area you want and add in some email addresses. You will also want to modify the price.. at current it's set to a minimum price of £150 per week.

It was written to solve a problem where we would be out looking for flats/apartments and we needed to be one of the first people to respond. This script gave us the edge that meant we could secure a good property in the limited window of time we had.

You need to be familiar with NodeJS to use this. Execute it as a cron job or however you want.. It will store results to a database called db.db

The code was written by [@pitapoison](http://twitter.com/pitapoison) - He is an awesome developer, you should follow him. We literally made this over a cup of tea and a bowl of pasta, it took 15 minutes and saved many hours.

I think it's interesting to see the approach we used to solving a housing problem, something that affects everyone yet so few will take the time to create a piece of software that gives them the edge.

\[javascript\] var request = require("request"); var parser = require("xml2json"); var db = require("dirty")("db.db"); var nodemailer = require("nodemailer"); var transport = nodemailer.createTransport("Sendmail");

db.on('load', function() { request('http://www.gumtree.com/rssfeed/single-room-flatshare/shoreditch', function (err, response, body) { if(err){ throw err; } var json = JSON.parse(parser.toJson(body)); var items = json.rss.channel.item; items.forEach(function(item){ try { var title = item.title; var price = /(\[0-9\]+)pw$/.exec(title)\[1\]; var content = item\["content:encoded"\].replace(/\\&\\#\[0-9\]+;/g," "); var link = item.link; if(price < 150){ return; } if(db.get(link) === true){ return; } db.set(link, true); var emails = \["person1@example.com", "person2@example.com"\]; emails.forEach(function(email){ var mailOptions = { from: "gumtreebot@example.com", to: email, subject: "GUMTREE: " + title, text: link + "\\n\\n\\n" + content } transport.sendMail(mailOptions); }); } catch(e){ console.error(e.stack || e); } }); }); }); \[/javascript\]
