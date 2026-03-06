---
title: "Your system does not meet the requirements to create android projects: undefined"
date: 2013-06-03
categories: 
  - "cordova"
tags: 
  - "cordova"
  - "phonegap"
---

Cordova platform add android errors with 

```
Your system does not meet the requirements to create android projects: undefined
```



Did you remember to 

```
chown -R YOURUSERNAMEHERE /usr/local/lib/node\_modules/cordova
```



You can check with.. 

```
ls -lsh /usr/local/lib/node\_modules/cordova
```

 You should see your username, not root..

If so.. Let's do a quick update of Cordova: 

```
cordova -v # review the version you are at npm update cordova cordova -v # review the new version
```



Let's make sure android works and the path is set to the android binary: 

```
android
```



This brings up the Android SDK Manager.

Test an emulator by hitting up: Tools > Manage AVDS, creating an image then hit Start. If your Android emulator works then continue, else something is up with your ADT/SDK deployment

Open up a CLI, type: 

```
export | grep PATH
```



Make sure your Android SDK **platform-tools** and **tools** folders are available in the PATH variable.

Going okay? Let's update the Android SDK 

```
android update sdk
```



Now try visit your cordova app folder and try 

```
cordova platform add android
```



Still no luck? Try using the master2 branch of the cordova-cli repo \*Warning, this is dangerous. 

```
cd ~ git://github.com/apache/cordova-cli.git cd ~/cordova-cli git checkout master2 sudo npm install -g exit cordova -v
```



The above should output a new cordova version #

Post a comment! :)
