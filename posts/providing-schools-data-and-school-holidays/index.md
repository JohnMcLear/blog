---
title: "Providing schools data and school holidays"
date: 2012-03-15
categories: 
  - "my-school-holidays"
---

[You know that website that provides school holidays](http://myschoolholidays.com)? Well I have to make that work.. Delivering the holiday dates to you is really easy, no drama there. We use a bunch of technologies to solve the problem of handling lots of requests per day.

# Building a database of all of the schools in the world

This really requires a separate post but I will touch on it lightly here.. We use a number of data sources to build our database, all of the data sources have an automated tool which extracts them, compares the data to our stored data then updates our database. Our database is rather large, we use sources such as edubase for UK, US, RU but things are very different for our Chinese brothers.. We have to call up the district offices and ask them to send us a list of schools, worst case scenario is they give us a list over the phone. We also use some open data maps to get some rough data. Finally we use web mining to "detect new schools", this gives our database an organic life and allows it to grow without any government input. By combining all of this data into one source we have a huge data set that we can begin mining from. We have been able to solve the problem of schools changing name/closing by using some clever insight analytics and by looking at search patterns for certain school names.. [Here you can see a school that has either closed or renamed](http://www.google.com/insights/search/#q=dixons%20ctc%2Cdixons%20city%20academy&cmpt=q), blue showing the old name, red showing the new.. When you correlate the lat/long you can calculate that it has been renamed.. Simples!

# Mining

Get out your hard hat and your birdy... We're going web mining... We rolled our own web mining platform, this took a lot of my time up, I have no idea why I did it this way because using tools such as rapidminer would have probably been quicker but that's life.. Our mining platform is a product of 2 years hard work to press, it's job is to go out onto the internet, find a school, find relevant data and store it. So for example, we go out onto the web, find a school and store the holiday dates as a "data dump", this data dump is just a copy of the page in whatever format it is stored in. We use naive bayesian filters to cluster the data into different categories and basically go from there.. We wont be releasing our mining platform publicly, it's not worth releasing because it's so application specific..

# Language support

MSH now supports most languages and is now classed as a global service. We used mygengo to gather translations and then we need PHP strings to render them based on the users URL IE de.myschoolholidays.com gets German results. It couldn't be more simple. The hardest part was crafting the initial language file and finding a good partner to work with.

# Cloudflare

Another recent new addition is cloudflare. Cloudflare sits in front of our varnish stack and provides us with the ability to compress Javascript, cache requests etc. One thing Cloudflare sucks at is providing round robin so it actually reduces our ability to provide high availability. Cloudflare's always online feature sucks pretty bad too. Despite these things it does reduce page load times and takes ~20% load away from our cluster, this is a good thing, hopefully they will resolve their current issues (I have 4 bugs filed with them) and we can move forward.

# Removing images

Our other task to increase page load speeds is to remove all images. We did this by replacing images with icons using a typography set. This sped up page load more than you would have thought, it's pretty impressive!

# Google Web fonts

Is a blight.. Y u need 150KB? So my trick w/ Google web fonts was instead of using the usual item in the head I load it in with javascript at the bottom of the page, this stops the on ready event from being blocked and means the user can use the page early on...

# Potential company changes

We are in discussions about sharding MSH out of it's current parent company PT. We have a bunch of reasons for this, the biggest one is that the two companies don't match up, the skill sets required to deliver the MSH service is completely different required to deliver day to day PT services.

# Outsourcing

Most of our workers on MSH are not based in the UK, we use a number of remote worker platforms to help us find the right employees. We actually require quite a lot of manpower to do "initial country learns", this is the process of learning about the structure of a country, how their holidays / councils / districts are layed out and also the language/social nuances.

So there you have it, a huge update and a lot of information about how we go about getting our data, it's resource intensive and it's a pretty big job as there are ~50k holiday sets each year each containing ~200k points of data.

Anyway if you get a sec please [check out our performance](http://myschoolholidays.com) and let us know what you think.
