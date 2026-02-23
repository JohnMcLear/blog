---
title: "Kodi Play/Pause with an NFC Ring and USB NFC Device"
date: 2015-09-14
categories: 
  - "nfc"
  - "nfc-ring"
---

<iframe width="560" height="315" src="https://www.youtube.com/embed/Ma5-ujah1tg" frameborder="0" allowfullscreen></iframe>

In this example I use a keyduino but you can use any Arduino device that has the PN532 or NFC module loaded on. The Arduino has to just push out the ID of the Ring (or tag) via Serial print. This arrives at ttyACM0 and we then parse it and do some xbmc events..

\[code\] var fs = require('fs'); var inp = fs.createReadStream("/dev/ttyACM0"); inp.setEncoding('utf8'); var inptext = ""; var XBMCEventClient = require('xbmc-event-client').XBMCEventClient; var xbmc = new XBMCEventClient('node.js app');

xbmc.connect(function(errors, bytes) { inp.on('data', function (data) { console.log(data); // inptext += data;

if (errors.length){ throw errors\[0\]; }

if(data.indexOf("yourringUIDhere") !== -1){ xbmc.notification('Resuming playback', 'Resuming playback'); xbmc.keyPress('space'); };

}); }); \[/code\]
