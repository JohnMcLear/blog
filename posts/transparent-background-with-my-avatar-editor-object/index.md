---
title: "Transparent background with My Avatar Editor Object"
date: 2010-08-29
categories: 
  - "games-based-learning"
  - "ict"
  - "primary-school"
  - "primary-school-ict"
---

[![](images/Untitled1.png)](https://mclear.co.uk/wp-content/uploads/2010/08/Untitled1.png) If you are using the javascript swfobject method for the hosted [My Avatar Editor](http://code.google.com/p/myavatareditor/) object you can use this code to give your avatar a transparent background: \[javascript\] <script type="text/javascript"> //<!\[CDATA\[ var avatarvalue = "<?= $avatarid ?>"; var avatarURL = "myavatarcharacter.swf?avatar=" + avatarvalue; swfobject.embedSWF(avatarURL, "avatarSWFContainer", "160", "200", "10.0.0", null, {hosted:"true"},{wmode:"transparent"}); function setFacialFeature(){ var avatarSWF = document.getElementById('avatarSWFContainer'); avatarSWF.draw(); } //\]\]> </script> \[/javascript\]

The only bit you need to change from the default code is the parameter which is the **{wmode:"transparent"}** bit
