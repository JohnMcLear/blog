---
title: "How to use Open source software to turn a portrait picture into something that resembles a cartoon (with additional alternatives) -- (TECHNICAL)"
date: 2009-06-16
categories: 
  - "be-funky"
  - "be-funky-alternative"
  - "gimp"
  - "gmic"
  - "imagemagick"
  - "picture"
  - "portrait"
  - "primary-pictures"
---

Important notes: Not everyone thinks a cartoon looks the same, cartoons come in many different formats and I try to present some options on this page. This is a technical document and not for general purpose consumption.

  

ImageMagick++ and GMIC are required. GimpUI is not but Gimp is. Unix is probably required and is recommended.

  

What I have tried to do is take a normal picture of a primary school kid and treat it so that it is more appealing to the pupil to put on an object of their personal posession.

  

I have released my findings so if anyone else tries to do the same thing they can:

  

Simplfied instructions:

Install GIMP-Devel

Install Dependancies for ImageMagick++

Install ImageMagick++

Install Dependancies for GMIC (take note on ftw3)

Install GMIC (takes a long time)

Once GMIC is installed run the commands that I have placed above each example.

  

You may wish to process this with PHP or Python or so, that should be very simple to do :)

  

GMIC seems to have much lower overheads than ImageMagick++.  
  

Original Image:

[![](images/LexiSyd122607CRPRET2plvrtstb047%20copy.jpg)](http://kinnairdphotography.com/content/00/01/39/27/66/userimages/LexiSyd122607CRPRET2plvrtstb047%20copy.jpg)

[](http://kinnairdphotography.com/content/00/01/39/27/66/userimages/LexiSyd122607CRPRET2plvrtstb047%20copy.jpg)  

**GMIC command:**

**gmic example.jpg -tetris 50 -o example3.jpg**

**GMIC command:**

**gmic example.jpg -edges 30 -o example5.jpg**

**

**GMIC command:**

**gmic example.jpg -drawing 30 -o example7.jpg**

  

  

  

  

**GMIC command:**

**gmic example.jpg -stencilbw 20 -o example6.jpg**

_Yes this looks very weird but if you apply the same effect to the picture of a boy they look like Harry Potter which is pretty cool if your a Primary School kid.._

  

  

  

**GMIC command:**

**gmic example.jpg -pencilbw 1 -o example8.jpg**

**
