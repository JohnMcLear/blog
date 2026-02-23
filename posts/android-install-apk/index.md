---
title: "Android install APK"
date: 2010-06-28
categories: 
  - "android"
  - "google"
  - "ict"
tags: 
  - "android-operating-system"
  - "android-sdk"
  - "tools"
---

So you are beta testing an application or whatever and you have been given an .apk file to install.

Before we start make sure you have the [android device driver installed, if not you can download it here.](http://developer.android.com/sdk/win-usb.html)

1\.  Plug the phone in to your PC with a USB Cable.  When prompted DO NOT mount USB.

2\.  On the phone goto Settings --> Applications then click the **Unknown sources** tick box.

3\.  On your PC **Download** the [Android SDK](http://code.google.com/android/intro/installing.html)

4\.  **Extract** the Android SDK to c:\\androidsdk

5\.  **Copy** the .apk file you were given to c:\\androidsdk\\tools

6\.  Click Start --> Run then type in:

> c:\\androidsdk\\tools\\adb install -r c:\\androidsdk\\tools\\_whatever.apk_

**Make sure you replace whatever.apk with the name of the file you copied.**

7\. Your application should now be installed.  Visit the application menu on the Android device and look for your icon.

###### Related articles by Zemanta

- [Lesson Not Learned: AT&T locks down the HTC Aria's app selection](http://www.mobilecrunch.com/2010/06/15/lesson-not-learned-att-locks-down-the-htc-arias-app-selection/) (mobilecrunch.com)
- [Install Android packages directly from GitHub](http://github.com/blog/665-apk-downloads-for-android-projects) (github.com)
- [HTC Aria Rooted Two Days After Release, Instructions Are Live](http://www.androidpolice.com/2010/06/22/htc-aria-rooted-two-days-after-release-instructions-are-live/) (androidpolice.com)

[![Enhanced by Zemanta](images/zemified_e.png)](http://www.zemanta.com/ "Enhanced by Zemanta")
