---
title: "Ajax CSV upload to a Table with jQuery and PHP"
date: 2012-01-26
categories: 
  - "developer"
  - "developing"
  - "development"
  - "jquery"
  - "php"
---

So I had to write a new user importer for [School Email](http://schoolemail.co.uk) and I was looking for a simple plugin in solution but didn't find one so here is a simple way of uploading a csv file that is uploaded to a file and rendered to a table..

Projects used: [CsvToTable](http://code.google.com/p/jquerycsvtotable/) & [jQuery File Upload](http://blueimp.github.com/jQuery-File-Upload/) & [Editable Grid \*optional](http://www.webismymind.be/editablegrid/) for live edits.

Grab those two projects, grab the below files and put them in a /js folder then put the .js files into your head..

Put the jQuery-File-Upload folder in your root, we will be uploading files to here.. You may want to add a layer of security in front of the upload function.

\[code\] <head> <script src="/js/csvToTable.js"></script> <script src="/js/jquery.iframe-transport.js"></script> <script src="/js/jquery.fileupload.js"></script> </head> \[/code\]

At the bottom of your body add.. \[code\] <div id="csvToTable"></div> <div id="fileupload"></div> <script> var loggedIn = 1; // you will want to modify this if you require auth $(function () { if(loggedIn == "1"){ $('#fileupload').fileupload({ dataType: 'json', acceptFileTypes: '/(csv)$/i', url: '/jQuery-File-Upload/php/index.php', done: function (e, data, Users) { $.each(data.result, function(index, file){ $('#csvToTable').html(""); $('#csvToTable').CSVToTable(file.url).bind("loadComplete",function() { console.log("Loaded data into table"); /\*

Call functions to manipulate data here

\*/ });; }); } }); } }); </script> \[/code\]

[Want to make your table editor like the rest of the cool kids? Check out this jQuery plugin](http://www.webismymind.be/editablegrid/)
