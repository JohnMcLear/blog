---
title: "How long did it take to connect to socket io?"
date: 2012-09-18
categories: 
  - "analytics"
  - "google"
  - "nodejs"
---

Send the duration(in ms) a client waited to connect to a Socket IO instance off to Google Analytics . I use this on [PrimaryWall](http://primarywall.com) to make sure it's not taking schools a long time to connect to walls. If I start to see this number getting bigger I know something is going wrong so I have an alert set if the average gets above 1000ms.

This code sends the ms it took from when the document was ready to when the socket was ready.

\[code\] $(document).ready(function () { var socketConnectDuration = 0; setInterval ( socketConnectDurationIncrease, 100 ); // Start a timer socket.on('connect', function () { \_gaq.push(\['\_trackEvent', 'Connection duration', 'Connection duration', socketConnectDuration\]); // Send the length of time to GA .... } }

function socketConnectDurationIncrease(){ socketConnectDuration = socketConnectDuration + 100; } \[/code\]
