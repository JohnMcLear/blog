---
title: "ThreeJS is tricky, but awesome."
date: 2014-09-12
categories: 
  - "blender"
  - "nfc"
  - "nfc-ring"
  - "threejs"
---

Over the past few months I have been using [ThreeJS](http://threejs.org/) to create a 3D model of the [NFC Ring](http://nfcring.com).

ThreeJS from Wikipedia:

> **Three.js** is a lightweight [cross-browser](http://en.wikipedia.org/wiki/Cross-browser "Cross-browser") [JavaScript library](http://en.wikipedia.org/wiki/JavaScript_library "JavaScript library")/[API](http://en.wikipedia.org/wiki/API "API") used to create and display animated [3D computer graphics](http://en.wikipedia.org/wiki/3D_graphics "3D graphics") on a [Web browser](http://en.wikipedia.org/wiki/Web_browser "Web browser"). Three.js scripts may be used in conjunction with the [HTML5](http://en.wikipedia.org/wiki/HTML5 "HTML5") [canvas element](http://en.wikipedia.org/wiki/Canvas_element "Canvas element"), [SVG](http://en.wikipedia.org/wiki/SVG "SVG") or [WebGL](http://en.wikipedia.org/wiki/WebGL "WebGL").

The ThreeJS community is actually really helpful, I'm not saying other communities aren't helpful or useful I just found that the ThreeJS community did a lot more to help get me started.  There are also quite a few demostration videos online that can be used as reference material.

The real power of ThreeJS comes when you mix it with the power of Blender.

Blender from Wikipedia:

> **Blender** is a professional [free and open-source](http://en.wikipedia.org/wiki/Free_and_open_source_software "Free and open source software") [3D computer graphics software product](http://en.wikipedia.org/wiki/3D_computer_graphics_software "3D computer graphics software") used for creating animated films, visual effects, art, 3D printed models, interactive 3D applications and video games. Blender's features include [3D modeling](http://en.wikipedia.org/wiki/3D_modeling "3D modeling"), [UV unwrapping](http://en.wikipedia.org/wiki/UV_mapping "UV mapping"), [texturing](http://en.wikipedia.org/wiki/Texture_mapping "Texture mapping"), [raster graphics editing](http://en.wikipedia.org/wiki/Raster_graphics_editor "Raster graphics editor"), [rigging and skinning](http://en.wikipedia.org/wiki/Skeletal_animation "Skeletal animation"), [fluid and smoke simulation](http://en.wikipedia.org/wiki/Fluid_simulation "Fluid simulation"), [particle](http://en.wikipedia.org/wiki/Particle_system "Particle system") simulation, [soft body](http://en.wikipedia.org/wiki/Soft_body_dynamics "Soft body dynamics") simulation, [sculpting](http://en.wikipedia.org/wiki/Digital_sculpting "Digital sculpting"), [animating](http://en.wikipedia.org/wiki/Computer_animation "Computer animation"), [match moving](http://en.wikipedia.org/wiki/Match_moving "Match moving"), [camera tracking](http://en.wikipedia.org/wiki/Camera_tracking "Camera tracking"), [rendering](http://en.wikipedia.org/wiki/Rendering_%28computer_graphics%29 "Rendering (computer graphics)"), [video editing](http://en.wikipedia.org/wiki/Video_editing_software "Video editing software") and [compositing](http://en.wikipedia.org/wiki/Compositing "Compositing"). Alongside the modeling features it also has an integrated [game engine](http://en.wikipedia.org/wiki/Game_Blender "Game Blender").

At first I was completely stuck, the video tutorials were out of date and the documentation far too fuzzy, finally I met someone on IRC who did the type of task I was trying to to accomplish every day as his day job.  Things fell into place quickly, so quickly I thought it would be worthwhile putting together a video showing how easy the process is to model an object and export it as something that can be used in ThreeJS:

<iframe width="560" height="315" src="//www.youtube.com/embed/8mlh_zSUTus?list=UUdbzIfrpmzGCJ2j1LjqW9Gw" frameborder="0" allowfullscreen></iframe>

Canvas is pretty much a no-go for the work I'm doing, it's nice to have the fallback options there but Canvas just doesn't have the features I need to display a ring in all of it's glory.  With that in mind if a user wants to see the ring and doesn't have WebGL supported they are shown a message how best to upgrade their browser.

Finally we should note both three.js and blender are open source projects, completely free and depend on community donation and support. They are both evolving under great leadership and they deserve the credit and respect they get.

This is what I was able to accomplish, I'm pretty proud of it.

<iframe src="http://nfcring.com/threejs/ring.html?sku=NTAG203-V1-NORMAL-T-B-T-16" width="600px" height="600px" scrolling="no" frameborder="0" allowfullscreen></iframe>

[You can see the source code and access the assets here](https://github.com/mclear/nfcring-web/tree/gh-pages/threejs)
