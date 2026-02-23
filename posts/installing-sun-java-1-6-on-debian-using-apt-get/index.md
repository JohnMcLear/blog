---
title: "Installing Sun Java 1.6 on Debian using Apt-Get"
date: 2009-12-18
categories: 
  - "debian"
  - "java"
  - "sun"
---

echo "deb http://ftp.de.debian.org/debian sid main non-free" >> /etc/apt/sources.list

apt-get install debian-backports-keyring

apt-get update

apt-get install sun-java6-jdk
