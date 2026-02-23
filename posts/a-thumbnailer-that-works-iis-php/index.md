---
title: "A thumbnailer that works - IIS &amp; PHP"
date: 2009-10-15
categories: 
  - "iis"
  - "php"
  - "thumbnail"
---

**About:**

  

This application downloads a copy of a websites screen capture and creates a small thumbnail. You can see this thumbnailer in action [here](http://primarygamesarena.com/).

  

**Requirements:**

- IIS on Server 2003/8+
- PHP (tested working) - To test PHP create a .php file that includes and browse to the file in IE
- A fully updated IE with a fully updated java & flash (Test by visiting sites)

When you install PHP ensure that PHP GB Library is installed

  

This application is a modified version of [http://www.zubrag.com/scripts/website-thumbnail-generator.php](http://www.zubrag.com/scripts/website-thumbnail-generator.php) - It relies on IE Capt which is included in the package but is also available from [http://iecapt.sourceforge.net/](http://iecapt.sourceforge.net/)

  

**Installation:**

1. Download it here
2. Extract the application to c:\\inetpub\\wwwroot\\th
3. Check that webthumb.php is in c:\\inetpub\\wwwroot\\th
4. Create c:\\caps and set everyone to full control (This will be where the screen caps are stored)
5. Browse to http://127.0.0.1/th/webthumb.php?url=http://test.com - After a few seconds you should see the thumbnail of test.com
6. To put a thumbnail on your website simply copy/paste this <img src="http://yourhostname.com/th/webthumb.php?url=http://thumbnailyouwant.com" /> Replacing yourhostname.com with the hostname of the server hosting this application and thumbnailyouwant with the url of the website you want to thumbnail.

Lastly you can add a level of security by commenting out the line if (0 == 0){} in webthumb.php, afterwards it should look like //if (0 == 0){}. Once this is done you will need to remove the commented lines above that begins with if(stri.... and replace primarygamesarena.com with the URL of your website that you will want thumbnailed images on. This will stop any site other than your own using your thumbnailer application.
