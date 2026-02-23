---
title: "Adding i18n to a Cordova App"
date: 2014-02-14
categories: 
  - "cordova"
  - "developer"
  - "developing"
  - "development"
---

i18n (Internationalization) in applications roughly means adding support for translations and other languages.  In this blog post I will talk you through a general approach to implementing i18n in Cordova Apps.  If your app isn't open-source, move along, the 90s is on another website.

As Cordova apps are written in HTML/CSS/JS we can easily leverage existing web platforms and services to provide i18n at break-neck speeds.

TLDR Services/frameworks used: \* [Translatewiki to provide translations](http://translatewiki.net) \* [Marcel's html10n i18n implementation](https://github.com/marcelklehr/html10n.js) \* Handlebars for templating \* Etherpad implementation of detecting locale/language also written by Marcel

## Implementation steps

\* Ensure your app [fulfills Translatewiki's requirements (Open source etc)](https://translatewiki.net/wiki/Translating:New_project) \* Talk to Translate / Internationalization team at Wikimedia foundation before creating Gerrit commit \* [Gerrit commit to TranslateWiki adding support for your App.](http://www.gossamer-threads.com/lists/wiki/mediawiki-cvs/431805) \* Include handlebars and [html10n](https://github.com/mclear/NFC_Ring_Control/blob/refactor/www/js/html10n.js) libraries in your app \* [Modify your HTML putting markup in handlebar script tags](https://github.com/mclear/NFC_Ring_Control/blob/refactor/www/index.html) \* [Move your text strings into locales files.](https://github.com/mclear/NFC_Ring_Control/blob/refactor/www/locales/en.json) \* [Include a handlebars html10n render helper](https://github.com/mclear/NFC_Ring_Control/blob/refactor/www/js/nfcRing/ui.js#L71) \* [Use the Etherpad implementation of detecting locale/language](https://github.com/mclear/NFC_Ring_Control/blob/refactor/www/js/nfcRing/ui.js#L75)\* Give someone at WMF access to commit to your Repo

## Sit back and enjoy..

Once you have completed your implementation and it's approved by the WMF the WMF translation team will translate all of your strings and commit them back to your repo. You might want to provide the WMF team with the ability to see each of your strings in situ in a browser, this means providing a mechanism to [fake Cordova events..](https://github.com/mclear/NFC_Ring_Control/blob/refactor/www/index.html#L160)

## Summary

This implementation is basically a straight copy of how we handle i18n in Etherpad, it's pretty robust and clean to implement. All in all a complete refactor of the NFC Ring Control App while implementing i18n took about a week of full time commitment, well worth doing as now the larger community can provide translations which if I was to do hans solo would take months :)
