---
title: "getusermedia screenshot wrong size"
date: 2013-07-12
categories: 
  - "javascript"
---

The drawImage API is really poorly documented and has a confusing way of handling arguments. Because of this sometimes if you capture a screenshot from your webcam the capture / snapshot will be drawn with the wrong dimensions. To solve this you will need to redraw your canvas to the same size as your video input on capture and also specify the width/height on capture.

This tripped me up for a few minutes so I figured it was worth documenting..

\[html\] <!DOCTYPE html> <body style="margin:0;padding:0;font-family:Arial"> <video id="video" autoplay width=100%></video> <img id="snapshot" src=""> <canvas id="canvas" style="display:none;"></canvas>

<script type="text/javascript"> var $ = function(id){return document.getElementById(id)}; // lazy dev is lazy var localMediaStream = null; var video = $('video'); // video stream var canvas = $('canvas'); // invisible canvas var snapshot = $('snapshot'); // output image var ctx = canvas.getContext('2d');

// Start Video Stream navigator.getUserMedia({video: true}, function(stream) { video.src = window.URL.createObjectURL(stream); localMediaStream = stream; }, function(){ alert("Enable and Allow your camera"); });

function snapshot() { if (localMediaStream) { canvas.width = video.offsetWidth; // update the canvas width and height canvas.height = video.offsetHeight; ctx.drawImage(video, 0, 0, video.offsetWidth, video.offsetHeight); // draw the captured content onto a canvas snapshot.src = canvas.toDataURL('image/png'); video.style.display = "none"; } } </script> </body> </html>

\[/html\]

To test go to your development console and type "snapshot()"
