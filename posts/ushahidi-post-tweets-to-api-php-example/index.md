---
title: "Ushahidi post tweets to API php example"
date: 2010-07-15
categories: 
  - "ict"
  - "my-school-closures"
  - "school"
  - "school-closures"
  - "ushahidi"
---

[![](images/filter-full1.png "filter-full[1]")](https://mclear.co.uk/wp-content/uploads/2010/07/filter-full1.png)

**The below code takes an rss search result from twitter, detects the authors location then posts the information to [Ushahidi](http://www.ushahidi.com "Ushahidi") via the [API](http://en.wikipedia.org/wiki/Application_programming_interface "Application programming interface").**

**Application I used it in**: [My School Closures](http://myschoolclosures.com) for detecting people who tweet about school closures.  Unfortunately I have to use pipes for the location builder which isn't elegant as [Yahoo Pipes](http://pipes.yahoo.com "Pipes") sucks and I wish I never started playing with it.  Feel free to play with the pipe I created to get geo location information from a location name, it is the pipe that has the json\_decode.

**You will need mysql and a table for the guids** (this stops us from spamming twitter for authors we have already located). Make sure you change the configuration settings and create a table in mysql.

The method is simple, the code isn't pretty and will require polishing but here it is:

\[php\] <pre> <?php //CONFIGURE THE SETTINGS BELOW //twitter settings $twitterusername = "mytwitteraccount"; $twitterpassword = "apasswordgoeshere";

//database settings $host = "databasehostname"; $user = "databaseusername"; $pass = "databasepassword"; $dbname = 'databasename';

// You should create a table called tweetguids in your database $tablename = "tweetguids";

// Change the below feed to a rss feed similar to below $rssurl = "http://pipes.yahoo.com/pipes/pipe.run?\_id=a9663ebc09e69b9195fb2407fba9f2bc&\_render=rss";

// END OF CONFIG

$conn = mysql\_connect($host, $user, $pass) or die ('Error connecting to mysql'); mysql\_select\_db($dbname);

ini\_set('display\_errors', 1); ini\_set('log\_errors', 1); ini\_set('error\_log', dirname(\_\_FILE\_\_) . '/error\_log.txt'); error\_reporting(E\_ALL);

$rss = simplexml\_load\_file($rssurl) or die("failure"); $count = 0; foreach ($rss->channel as $chan) { $time = $chan->pubDate; } foreach ($rss->channel as $chan){$time = $chan->pubDate;} foreach ($rss->channel->item as $item) { // only do first 10 records if ($count < 10) { $foundguid=0; $guidnew=$item->guid; // Check to see if guid exists in db already $sql="SELECT \* FROM $tablename where guid = \\"$guidnew\\""; $result=mysql\_query($sql, $conn); while ($row=mysql\_fetch\_array($result)) { $foundguid=1; echo "Foundguid: $foundguid"; } if($foundguid==1) { echo "We found an alredy existing guid..."; } else { $count = $count + 1; $task="report"; $incident\_title=$item->title; $guidnew=$item->guid; $incident\_title=str\_replace(" ","+",$incident\_title); $incident\_description=$item->description; $incident\_description=str\_replace(" ","+",$incident\_description); $incident\_date=date("m/d/Y",$time); $incident\_hour=date("H",$time); $incident\_minute=date("i",$time); $incident\_ampm=date("a",$time); $incident\_category="Possible Closure"; $location\_name="Unknown"; $author = $item->author; $author = str\_replace(" ","+",$author); $pos = strpos($author,"+"); //$author = substr($author,0,$pos); $author = str\_ireplace("http://twitter.com/","",$author); $url = "http://$twitterusername:$twitterpassword@api.twitter.com/1/users/lookup.xml?screen\_name=$author"; //echo $url; $output = simplexml\_load\_file($url) or die("badauth"); foreach ($output->user as $item) { // Get the values out of the XML $location=$item->location; // Clean up the location $location=str\_ireplace("-",",",$location); $location=str\_ireplace(" ",",",$location); // $location=preg\_replace("/\[^a-zA-Z0-9\\s\]/", "", $location); echo "<br/><b>Location content: $location<br/>"; // Pass the location to yahoo pipe $location = str\_ireplace(" ","",$location); //echo "<br/>Loc: $location"; $locationurl = "http://pipes.yahoo.com/pipes/pipe.run?\_id=03539616e4cdd62eb15ed26b81e3041e&\_render=json&q=$location";

$ch = curl\_init(); curl\_setopt($ch, CURLOPT\_URL, $locationurl); curl\_setopt($ch, CURLOPT\_RETURNTRANSFER, 1);

//make the request $json = curl\_exec($ch); $arr = (json\_decode($json,true)); $blah = $arr\['value'\]\['items'\]\[0\]\['name'\]\['loc'\]; //print\_r($blah); $latitude = $blah\['lat'\]; $longitude = $blah\['lon'\]; $location\_name = $blah\['city'\]; }

$incident\_description="Closure reported from twitter"; $url = "task=report&incident\_title=$incident\_title&incident\_description=$incident\_description&incident\_date=$incident\_date&incident\_hour=$incident\_hour&incident\_minute=$incident\_minu$ $posturl = "http://myschoolclosures.com/ushahidi/api"; $Curl\_Session = curl\_init($posturl); curl\_setopt ($Curl\_Session, CURLOPT\_POST, 1); curl\_setopt ($Curl\_Session, CURLOPT\_POSTFIELDS, $url); curl\_setopt ($Curl\_Session, CURLOPT\_FOLLOWLOCATION, 1); curl\_exec ($Curl\_Session); curl\_close ($Curl\_Session); //Write to the database $sqlgo="INSERT INTO $tablename VALUES (\\"$guidnew\\")"; $result=mysql\_query($sqlgo, $conn); } } //Write anything else to DB just in case anything trails behind $sql="INSERT INTO $tablename VALUES (\\"$guidnew\\")"; $result=mysql\_query($sql, $conn); $row=mysql\_fetch\_array($result); //echo "<br/>$sql<br/>"; } ?> \[/php\]
