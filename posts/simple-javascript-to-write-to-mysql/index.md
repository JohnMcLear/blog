---
title: "Simple Javascript to write to mysql"
date: 2010-05-30
---

[![](images/IMAG0133-300x200.jpg "IMAG0133")](https://mclear.co.uk/wp-content/uploads/2010/05/IMAG0133.jpg)

This is more of a braindump/code dump for me. [Original source](http://www.w3schools.com/php/php_ajax_database.asp)...

Note: If you are going to use [PHP](http://www.php.net/ "PHP") values in this script please make sure they are set first...

Note2: I know javascript isn't writing directly to mysql, this is my preferred method. function.php does the actual writing to mysql.. (uses update function - if you are reading this I expect you already know how to write a simply mysql update/insert statement and execute it inside of php..

**Example.html**

\[javascript\] <!-- Function to save avatarID --> <script type="text/javascript"> function showUser(str) { if (str=="") { document.getElementById("avatarsavediv").innerHTML=""; return; } if (window.XMLHttpRequest) {// code for IE7+, Firefox, Chrome, Opera, Safari xmlhttp=new XMLHttpRequest(); } else {// code for IE6, IE5 xmlhttp=new ActiveXObject("Microsoft.XMLHTTP"); } xmlhttp.onreadystatechange=function() { if (xmlhttp.readyState==4 && xmlhttp.status==200) { document.getElementById("avatarsavediv").innerHTML=xmlhttp.responseText; } } // best to set a new variable name so I don't forget what I'm working on var avatarid = str; // below we can grab a mysql value if we need to var phpnickname = "<?= $username ?>"; var avurl = "function.php?nickname="+phpnickname+"&avatarid="+avatarid; xmlhttp.open("GET",avurl,true); xmlhttp.send(); } </script> \[/javascript\]

\[html\] <div id="avatarsavediv"></div> \[/html\]

Final note: The above shows the output

![Reblog this post [with Zemanta]](images/reblog_e.png)
