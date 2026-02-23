---
title: "Using git flow to release new version"
date: 2012-10-03
categories: 
  - "etherpad"
  - "git"
---

Using git flow to release a new version of software enables developers to easily switch between releases to locate bugs and/or introduce new features.

In this example we are releasing version 1.1.4.

NOTE TO SELF: Remember to bump the version in src/packages.json

\[code\] # debian/ubuntu only apt-get install git-flow

\# checkout the development branch git checkout develop

\# first time only, accept defaults git flow init

\# start the release process # note the releases-1.1.4 bit, this should be 1.1.4 only but I'm following the pattern of Etherpad Lite git flow release start 1.1.4

\# publish the release to a new release branch git flow release publish 1.1.4 \[/code\]

Check everything fully one last time IE packages.json and let travis run it's tests..

\[code\] git flow release finish 1.2.4 git push origin master --tags \[/code\]

Now in root do

\[code\] make docs \[/code\]

then copy the out/doc folder to ether.github.com repo doc/vx.x.x folder

\[code\] mv out/doc/ ../ether.github.com/doc/v1.4.1/ \[/code\]

create the windows binary

\[code\] bin/buildforwindows.sh \[/code\]

copy the last 10 digits of the sha from git log to the end of the windows package file name before .zip

put this .zip in the ether.github.com/downloads folder and commit / push that.
