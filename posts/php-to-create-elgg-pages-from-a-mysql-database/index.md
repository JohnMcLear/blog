---
title: "PHP to create Elgg pages from a mysql database"
date: 2009-12-29
categories: 
  - "elgg"
  - "mysql"
  - "php"
---

**Installation:**

1. Save to below script to the root of your Elgg install as importelgg.php
2. Change the bits in bold to suit your environment.
3. Log into your elgg site as the user you want to upload as then browse to the script.

**Code:**

  

<?php

// Modified from edit.php from Elgg doc's by John McLear - www.mclear.co.uk

set\_time\_limit(0); // We dont want the script to time out

require\_once 'engine/start.php';

// Load configuration

global $CONFIG;

  

$dbhost = '**localhost**'; // The MySql Hostname

$dbuser = '**root**'; // MySQL Username

$dbpass = '**yourpassword**'; // MySQL Password

$conn = mysql\_connect($dbhost, $dbuser, $dbpass, TRUE) or die ('Error connecting to mysql'); // TRUE so we dont overwrite connection

$dbname2 = '**mydatabase**'; // The databasename

  

mysql\_select\_db($dbname2);

$sql="**SELECT title,contents FROM pages**"; // Get the content from the source database

$result=mysql\_query($sql);

  

// Go through the records and create what you need from that

while ($row=mysql\_fetch\_array($result)) {

$title=$row\["**title**"\]; //Set the title value from the mysql title field

$content=$row\["**contents**"\]; // Same as above but for contents

gatekeeper();

set\_context('pages');

// Get group fields

$input = array();

foreach($CONFIG->pages as $shortname => $valuetype) {

$input\[$shortname\] = get\_input($shortname);

if ($valuetype == 'tags')

$input\[$shortname\] = string\_to\_tag\_array($input\[$shortname\]);

}

// Get parent

$parent\_guid = (int)get\_input('parent\_guid', 0);

// New or old?

$page = NULL;

$pages\_guid = (int)get\_input('pages\_guid');

if ($pages\_guid)

{

$page = get\_entity($pages\_guid);

if (!$page->canEdit())

$page = NULL; // if we can't edit it, go no further.

}

else

{

$page = new ElggObject();

if (!$parent\_guid)

$page->subtype = 'page\_top';

else

$page->subtype = 'page';

// New instance, so set container\_guid

$container\_guid = get\_input('container\_guid','**8849**'); // Set the container GUID to a static user

$page->container\_guid = $container\_guid;

}

// Have we got it? Can we edit it?

if ($page instanceof ElggObject)

{

// Save fields - note we always save latest description as both description and annotation

if (sizeof($input) > 0)

{

foreach($input as $shortname => $value) {

if ((!$pages\_guid) || (($pages\_guid) && ($shortname != 'title')))

$page->$shortname = $value;

}

}

// Validate create

$page->title = $title;

if (!$page->title)

{

register\_error(elgg\_echo("pages:notitle"));

  

forward($\_SERVER\['HTTP\_REFERER'\]);

exit;

}

// Access ids (Make it public)

$page->access\_id = 2;

// Get the content

$page->description = $content;

// Write access id (Make it public)

$page->write\_access\_id = 2;

// Set parent

$page->parent\_guid = $parent\_guid;

// Ensure ultimate owner

$page->owner\_guid = ($page->owner\_guid ? $page->owner\_guid : $\_SESSION\['user'\]->guid);

// finally save

if ($page->save())

{

// Now save description as an annotation

$page->annotate('page', $page->description, $page->access\_id);

system\_message(elgg\_echo("pages:saved"));

//add to river

add\_to\_river('river/object/page','create',$\_SESSION\['user'\]->guid,$page->guid);

echo "$title - DONE<br/>";

}

else

register\_error(elgg\_echo('pages:notsaved'));

  

}

else

{

register\_error(elgg\_echo("pages:noaccess"));

}

usleep(250000); // Just a little rest not to be overspammy

}

?>
