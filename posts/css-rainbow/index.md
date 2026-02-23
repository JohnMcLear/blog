---
title: "CSS rainbow"
date: 2012-11-08
---

Chrome only, very easy to port to firefox/IE

\[code\] .rainbow { /\* Pretty rainbow colors chrome \*/ background: -webkit-gradient( linear, left top, left bottom, /\* red \*/ color-stop(0%,rgba(255,50,50,1)), color-stop(13%,rgba(255,50,50,1)), /\* yellow \*/ color-stop(14%,rgba(238,255,50,1)), color-stop(27%,rgba(255,224,50,1)), /\* pink \*/ color-stop(28%,rgba(255,50,248,1)), color-stop(41%,rgba(238,50,255,1)), /\* green \*/ color-stop(42%,rgba(42,201,40,1)), color-stop(55%,rgba(0,160,11,1)), /\* purple \*/ color-stop(56%,rgba(122,24,122,1)), color-stop(69%,rgba(122,24,122,1)), /\* orange \*/ color-stop(70%,rgba(255,146,50,1)), color-stop(83%,rgba(255,139,50,1)), /\* blue \*/ color-stop(84%,rgba(30,87,153,1)), color-stop(100%,rgba(30,87,153,1)) ); } \[/code\]

Apply the rainbow class to your element IE \[code\] <div class=rainbow>... \[/code\]
