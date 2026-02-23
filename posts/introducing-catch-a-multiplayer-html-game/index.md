---
title: "Introducing Catch - A multiplayer html game"
date: 2011-04-06
categories: 
  - "developer"
  - "developing"
---

Today I'm introducing catch, a game we have been developing for the last month or so as a side project. Catch is like Tag or Tig or whatever you called it in the playground. Basically someone is "it" and you're job is to avoid that person.. Avoiding the person gives you points.. Could it be any simpler?

Let's get a few things out of the way: It isn't much of a game.. I mean you can win but we haven't introduced many other game mechanics. The code isn't optimized, we wrote it to learn about socket messaging so once we had learned enough we moved onto a proper project and rushed the game out of the door. You can embed the game and play against other visitors on your blog/whatever. The game doesn't require flash. Embed probably doesn't work in IE. The game is built on NodeJS, Socket.IO, jQuery/Javascript. We don't have any databases, we're too lazy. We host the game but [we released it open source](https://github.com/Pita/CatchGame) so go ahead and host your own and/or break/play with the game!

Technical accomplishments: Slowest user render (see game.html) Latency detection and sorting (see game.html) Connectivity type detection and advice (see browser.js) Strange UI scoreboard based on pixels per points (see game.html)

Here is the game.. Hosted by brightbox.

<iframe src="http://game.mclear.co.uk:8002/static/animate.html" width="550" height="400"></iframe>
