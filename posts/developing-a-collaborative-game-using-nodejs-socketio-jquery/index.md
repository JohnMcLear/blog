---
title: "Developing a collaborative game using NodeJS, SocketIO & jQuery"
date: 2011-03-03
categories: 
  - "developer"
  - "developing"
  - "ict"
---

[Quick link to the game I made](https://mclear.co.uk/2011/04/06/introducing-catch-a-multiplayer-html-game/)

You may remember a few months ago I did an article on [Real time mouse activity using NodeJS and Socket](https://mclear.co.uk/2011/01/30/real-time-mouse-activity-w-nodejs-sockets/), well I wanted to extend that functionality into some sort of game. It was obvious from the demo I made that people enjoyed interacting with each others cursors and I quite enjoyed working on it.

Today was our second day working on the game and our [UI design](http://en.wikipedia.org/wiki/User_interface_design "User interface design") is pretty much done and so are 2 of the 3 minigames designs. The mechanics are coming along with a few cretins as we have to wrestle with [Internet Explorer](http://www.microsoft.com/windows/internet-explorer/default.aspx "Internet Explorer")'s(8+9b) interesting interpretation of how Socket should perform. Firefox and [Chrome](http://www.google.com/chrome "Google Chrome") have been a dream to work with the [jQuery](http://jquery.com/ "JQuery") implementation of the animations and the scoreboard have gone pretty smoothly..

We're doing about 10 hours a day on it at the moment however the days only feel 6 hours or so long as it is a labour of love and is a nice change from the mundane [PHP](http://www.php.net/ "PHP") bugs I usually deal with.  The work we are doing is one of the small steps needed to move away from Abobe [Flash based](http://www.adobe.com/products/flash/flashpro/ "Adobe Flash") games.

We're hoping to demo one of the mini games to the LeedsJS folks on the 9th of March so if you want to see then come along! By the 9th of March I will expect about 100 hours or so in total has been spent on the game and you wont be able to tell as nearly all of the work is done on the server/back end as we are writing mechanisms that mean the game can operate as leanly as possible on both desktop browser and mobile browsers.

Here are our goals for the project:

1. Scalability
2. Completion in time for some competition thingy in April
3. Any browser on any device that supports socket
4. Hopefully flash fall back on non-socket supporting devices.
5. Push all code as Open Source  under [Apache license](http://en.wikipedia.org/wiki/Apache_License "Apache License") in Summer.

Quick thanks to John at [Brightbox](http://brightbox.co.uk) for providing the hosting for the project :) We're using their very [BETA](http://en.wikipedia.org/wiki/Software_release_life_cycle "Software release life cycle") vm hosting service which I don't know much about but it is _super fast_ and is speeding up our development somewhat.

[![Enhanced by Zemanta](images/zemified_e.png)](http://www.zemanta.com/ "Enhanced by Zemanta")
