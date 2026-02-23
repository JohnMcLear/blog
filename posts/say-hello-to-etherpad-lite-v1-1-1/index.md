---
title: "Say Hello to Etherpad Lite V1.1.1"
date: 2012-07-05
categories: 
  - "features"
---

## Oh you haven’t heard about us already

Etherpad Lite is a collaborative editor, sort of like a web-based multiplayer Notepad but with some really amazing features and a really developer friendly community and framework. Etherpad Lite is completely open-source and comes with no douchery what so ever attached..

If you scroll to the bottom of this post you can see Etherpad Lite in action. The Etherpad Foundation (That’s us) maintain a [public Etherpad Lite sandbox deployment for you to start toying with.](http://beta.etherpad.org) The public API key is EtherpadFTW.

[Have you checked out the plugins? They are freaking amazing!](http://etherpad.org/?s=plugin)

## What’s new with the software?

1. Support node v0.8
2. Various bugfixes (See: [https://github.com/Pita/etherpad-lite/pull/834](https://github.com/Pita/etherpad-lite/pull/834))
3. Various new hooks (aceEditEvent, handleMessage)
4. Various new API endpoints (getLastEdited, lastPadsOfAuthor, listAuthorsOfPad, padUsersCount)
5. Various resolution of security issues (Disconnect on lack of authentication)
6. Plugin installation no longer needs a server restart to be active.
7. Nazi’s on the moon
8. Better Microsoft Windows support out of the box
9. Postgres support
10. Unified timeslider and editing protocol
11. Better disconnect handling

## What’s new in the foundation?

1. Marcel Kehr is our bugmaster.
2. Redhog and FourPlusOne now have more authority over the repo.
3. Berkley, MIT, Mozilla and various other fantastic organizations now run Etherpad and we’re really greatful for their support!
4. We’re looking for more sponsors so we can dedicate more resources into making the software and the community flow better, [please get in touch](http://etherpad.org/contact) if you can help!

## What’s next for the foundation?

We have achieved our goal of making etherpad easy to adopt for web developers, we’re really happy with the number of contributors and new plugins being developed by the community. Our next goals are:

1. Povide a robust testing framework
2. Migrate any legacy Etherpad instances(such as PrimaryPad, PiratePad) to Etherpad Lite
3. Language translation support
4. Integration with even more CMS’, Kudos to Moodle, Elgg, MediaWiki and others for their integration to date!

Whilst these might not seem like exciting or bells and whistle new features they will allow Etherpad to enter into a more enterprise type environment. Don’t worry guys, we’re not all of a sudden going to suggest a migration to Java ![;)](images/icon_wink.gif) Our goal is to ensure our current users have a stable, flexible and well supported future with Etherpad. Most of the cool shiny new features that create exciting new UI components are being developed as plugins so you should visit /admin/plugins after you install to see what is available!

We’re desperatley trying to find someone who can lead our community efforts so if you love organizing meet ups and/or love social networking [please get in touch.](http://etherpad.org/contact)

#### **Thanks** to 0ip, jhollinger, redhog, mtraceur, cboylan, marcelkehr, pita and others for making 1.1.1 possible ![:)](images/icon_smile.gif) Without their and others hard work we would be months behind on our release schedule. We all owe them a great deal of gratitude!

Thanks also to our [current sponsors and new sponsors](http://etherpad.org/sponsors/) especially ones that advocate for freedom on the internet ![;)](images/icon_wink.gif) . Kudos to the UN, NATO, various Pirate Parties and other government bodies for fighting litigation that could cripple freedom of speech on the internet, without you guys in our corner our struggle would be a lot more fraught with danger..

Existing Etherpad Lite users, don’t delay, **git pull** today!

Ninjas – [Visit Etherpad Lite on Github](https://github.com/Pita/etherpad-lite)  
Warriors – [Get Etherpad Lite for Linux](https://github.com/Pita/etherpad-lite/tarball/master)  
Pretenders – [Get Etherpad Lite Microsoft Windows](http://beta.etherpad.org/static/etherpad-lite-win.zip)
