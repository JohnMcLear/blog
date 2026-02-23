---
title: "Sending Hex to MyAvatarEditor object using PHP"
date: 2010-05-30
categories: 
  - "ict"
---

[![](images/Random.jpg "Random")](https://mclear.co.uk/wp-content/uploads/2010/05/Random.jpg)

Want to push a hex value from a database to a myavatareditor element? It's easy, here is an example:

Make sure $avatarid is the Hex code for your avatar. PHP example included here..

\[javascript\] <script type="text/javascript"> //<!\[CDATA\[ var avatarvalue = "<?= $avatarid ?>"; var avatarURL = "myavatarcharacter.swf?avatar=" + avatarvalue; swfobject.embedSWF(avatarURL, "avatarSWFContainer", "160", "200", "10.0.0", null, {hosted:true}); function setFacialFeature(){ var avatarSWF = document.getElementById('avatarSWFContainer'); avatarSWF.draw(); } //\]\]> </script> \[/javascript\]
