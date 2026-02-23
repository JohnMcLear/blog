---
title: "Be Funky API doesn't seem to work for me :("
date: 2009-06-04
categories: 
  - "be-funky"
  - "befunky"
  - "befunky-com"
  - "cartoon-api"
  - "cartoonizer"
  - "photo-editing"
---

Hrm, appears that the BeFunky.com API doesn't work from the example they paste.

  

I tried many different methods of rewritin the URL and the PHP but I still failed :(

  

Does anyone have a good working example?

  

  

\*\*\* Since I posted this I found a solution! :) \*with help from Phiz Uglyface

  

Download the files at http://primaryt.co.uk/befunky.zip and extract them to a new folder on your webserver.

  

Edit the:

1. key  
    
2. secret  
    
3. post\_url  
    
4. callbackURL  
    
5. imgLink  
    

  

Values in index.php to suit your setup. Making sure that the files referenced exist in the correct location.
