---
title: "Transfer videos from Youtube to Vimeo"
date: 2011-05-27
categories: 
  - "developer"
  - "developing"
  - "ict"
  - "php"
  - "video"
  - "youtube"
---

[Tomnomnom made a new set of scripts for automatically uploading from the Linux shell to Vimeo.](https://github.com/TomNomNom/Vimeo-Uploader)

<iframe width="660" height="415" src="http://www.youtube.com/embed/9m4JORJH7xQ" frameborder="0" allowfullscreen></iframe>

Use the scripts to create a super simple way of uploading videos you have downloaded from Youtube (see below) to write straight into Vimeo automatically..

[Get started now!](https://github.com/TomNomNom/Vimeo-Uploader)

Enjoy! :)

UPDATE: BELOW IS THE OLD INFORMATION LEFT FOR HISTORICAL PURPOSES.

  
Lately Iv'e felt a bit paranoid giving Google even control of my digital domain so I wanted to move all my videos to Vimeo and to keep a local copy for me. Google makes it easy for you to individually download your video files but I wanted to bulk copy them from my youtube account to my local box and at the same time upload them to vimeo...

This very rough and buggy PHP that allows you to move all of YOUR videos from Youtube to Vimeo. **You should not use this script to steal anyones content. You should not use it for malicious purposes.** The script is completely legal if used appropriately, it does not violate any of Google's or Vimeo TOS. **If you do use this to upload your files to Vimeo you should delete your videos from youtube as to avoid duplicate content.**

## Prereq's & installation

1\. php5 & curl.. 2. php.ini for Apache w/ a large memory setting. edit memory setting in /etc/php5/apache2/php.ini or whatever 3. ssh/shell access (im too lazy to write a web front end <-- scrap that I wrote a web front end cause I'm super cool.).. 4. Your videos must have a 720p download available else this is just a waste of everyones times. Let's make video on the web better ey? 5. You get a Vimeo API key. http://vimeo.com/api/applications/new -- When registering you will need to set it as a Write application and set a Callback URL as FullURL/vimeo/authenticate.php -- You also want to request perms to upload via -- This can take up to a few days. After registration is click click Upload Access - request, then copy your consumer key and secret to the below options 6. Visit a URL where you extracted the files.

## How it works

1\. Query your YouTube account, gets a list of all videos 2. For each video get the ID, metadata (name, description etc.) and store that in an array 3. Get the video file for this Video 4. Upload the video file and metadata to Vimeo via the API 5. Return to Step 2, it's a funking loopsi.

## Limitations, because there be many

1\. Unicorn rainbows are limited to 127 per session. 2. You can't exclude certain videos 3. You can only do 50 videos at a time. // run it again w/ a higher value in the start-index if you want to do more than 50. 4. First upload fails right now, just a bug.. 5. Breaks upload on many characters, just requires some encoding

[Grab the source code here](http://primaryschool.tv/youtubeToVimeo.tar.gz)

Run by visiting /youtube/index.php

Note: Vimeo has a daily limit on the upload API, I think it's ~10 videos a day..
