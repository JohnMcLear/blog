---
title: "Adding location awareness to Ushahidi"
date: 2010-12-28
categories: 
  - "developer"
  - "developing"
  - "php"
  - "ushahidi"
---

This post is for site admins who want to add location awareness to their ushahidi deployment. Location awareness allows ushahidi to know where the visitor is coming from and display them a map local to them. It requires the user to have an ip v4 address. It is not the best solution for this problem but for now it works...

First things first, visit your application/controllers/main.php and comment out these lines

\[php\] $this->themes->js->latitude = Kohana::config('settings.default\_lat'); $this->themes->js->longitude = Kohana::config('settings.default\_lon'); \[/php\]

Paste this below the lines you have commented out:

\[php\] include\_once 'DetectLocation.php'; // this isn't the best way but it works.. $this->themes->js->latitude = $lat; $this->themes->js->longitude = $lng; \[/php\]

Next visit [ipinfodb.com](http://ipinfodb.com/) and grab their mysql database, extract it then import it into your mysql deployment, I used the database name ipinfo.

Create a new php file called DetectLocation.php in the root of your Ushahidi deployment.

Paste this into it

\[php\] <?php // Using data from http://ipinfodb.com/ -- this should be in the ipinfo database // Code by John McLear, all free licenses attached. Please re-use, modify & redistribute

$dbuser = 'ipinfo'; // using a psuedo/differnet user because I'm cool like that. $dbpass = ''; $dbhost = 'localhost'; $dbname = 'ipinfo';

$conn = mysql\_connect($dbhost, $dbuser, $dbpass) or die ('Error connecting to mysql');

mysql\_select\_db($dbname) or die('Could not select database');

$ipAddress = mysql\_real\_escape\_string($\_SERVER\['REMOTE\_ADDR'\]); // Get IP Addr of visitor

$query = "SELECT \* FROM \`ip\_group\_city\` " . "WHERE \`ip\_start\` <= INET\_ATON( '$ipAddress' ) " . "ORDER BY ip\_start DESC " . "LIMIT 1";

$resultLocation = mysql\_query($query);

while ($row = mysql\_fetch\_array($resultLocation)) { $lat = $row\['latitude'\]; $lng = $row\['longitude'\]; } ?> \[/php\]

Test it by visiting your Ushahidi deployment, your map should be centred on your location.

So quick recap. We are using a local mysql database to lookup locations by IP. This is fast, fast is good. It isn't perfect. Perfect would be better. Feel free to improve upon, change/correct..

Note: You probably also want to do the same changes on reports.php and alerts.php
