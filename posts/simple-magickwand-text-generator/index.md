---
title: "Simple MagickWand Text Generator"
date: 2010-01-08
categories: 
  - "font"
  - "imagemagick"
  - "magickwand"
  - "text"
---

Just finishing up for the day and wanted to quickly publish this, it might be a bit sloppy..  
  
Change Font Face, Size, Color & Background image height and width by modifying the GET parameters.  
  
Example GET = <img src="http://primaryschoolteaching.co.uk/generator/font2.php?font=kiddy&txt=api%20for%20school%20fonts&width=150&height=50&fontsize=15&colorcode=b6d4f1">  
  
Example output =  
  
**Code (copy and paste to test2.php and change url):**

<?php  
$font = $\_GET\['font'\];  
$txt = $\_GET\['txt'\];  
$height = $\_GET\['height'\];  
$width = $\_GET\['width'\];  
$fontsize = $\_GET\['fontsize'\];  
$color = $\_GET\['colorcode'\];  
  
// die if font permissions are bad  
if(!is\_readable("$font.ttf")) {  
die("$font is not readable!");  
}  
  
if(extension\_loaded('magickwand')) {  
$resource = NewMagickWand();  
$status = MagickReadImage($resource, "white-pixel.jpg");  
$resource = MagickTransformImage($resource,'0x0',"$heightx$width");  
$draw = NewDrawingWand();  
  
DrawSetFont($draw,"/path/to/$font.ttf");  
DrawSetFontSize($draw, $fontsize);  
DrawSetFillColor($draw, "#$color");  
MagickCropImage($resource, 200, 30, 0, 0 );  
  
$status = MagickAnnotateImage($resource, $draw, 5, 20, 0, "$txt");  
  
header('Content-Type: image/gif');  
echo MagickEchoImageBlob($resource);  
exit;  
}  
?>

  
  
You could now use jQuery to pass the color or whatever on the fly so it autoregens each time you edit a param.. Simples! Don't forget to supply a background file!
