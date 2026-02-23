---
title: "Only display this months data in Ushahidi"
date: 2010-12-28
categories: 
  - "developer"
  - "developing"
  - "php"
  - "ushahidi"
---

This is a simple hack to make Ushahidi display only the current months worth of data. This is useful if you have a large dataset with no real need to display historical data to your users.

Modify application/controllers/main.php lines 327 onwards.

\[php\] /\* Commented out by John McLear \*/ // $first\_month = 1; // $last\_month = 12;

/\* Added by John McLear as to only show the current month of data \*/ $first\_month = date('m'); $last\_month = date('m'); /\* End of new code \*/

$i = 0;

foreach ($query as $data) { $date = explode('-',$data->dates);

$year = $date\[0\]; $month = $date\[1\];

/\* Added by John McLear \*/ // Only includes from the month we are in now, yes this sucks but it works if ($month == $first\_month){

// Set first year if($i == 0) { $first\_year = $year; $first\_month = $month; }

// Set last dates $last\_year = $year; $last\_month = $month; }

$i++; } \[/php\]
