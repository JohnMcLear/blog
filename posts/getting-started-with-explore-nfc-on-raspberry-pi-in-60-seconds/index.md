---
title: "Getting started with Explore NFC on Raspberry Pi in 60 seconds (Also Raspbmc)"
date: 2014-01-20
categories: 
  - "nfc"
  - "nfc-ring"
---

The docs from NXP are slightly over verboose, here I make the assumption you already have a Pi installed and know a little about SSH and using the Linux Terminal. It's worth noting I'm doing some of these steps on Raspbmc too so things may differ slightly from your environment. I will try cover both wheezy and Raspbmc

**Put module onto Raspberry Pi by y'know, putting it on the Pi.. Reboot..**

SSH into your Pi username pi, password raspberry `ssh pi@your-pi-ip-address`

**Update your Pi and install some deps** SPI was added late 2013 so it might not be available in your Kernel, doing an update is easy, do.. `sudo apt-get update && sudo apt-get upgrade && sudo apt-get install ca-certificates git-core cmake` -- Make a cup of tea

`cd ~ && sudo wget http://goo.gl/1BOfJ -O /usr/bin/rpi-update sudo chmod +x /usr/bin/rpi-update && sudo rpi-update sudo ldconfig` Note: If you get a prompt saying you might not need this firmware or it's the wrong update then just skip this step.

**Enable SPI (not required on Raspbmc)** `sudo nano /etc/modprobe.d/raspi-blacklist.conf` -- Comment out blacklist spi-bcm2708 -- Change it to read (note the hash) `# blacklist spi-bcm2708`

**Enable Pi on Rasmbmc** `sudo boblightd` [For posterity further information about this fix is on this thread](http://forum.stmlabs.com/showthread.php?tid=12960&pid=94924#pid94924) -- Note that sudo boblightd toggles SPI pins so running it twice might not work..

**Reboot** `sudo shutdown -r now` -- Make a cup of tea

**Grab the demo polling app from my Git Repo of the NXP S/W** `cd ~ git clone https://github.com/JohnMcLear/NXP-Raspberry-Pi-Card-Polling-Demo.git cd NXP-Raspberry-Pi-Card-Polling-Demo cmake source make` -- Make a cup of tea

**Test** `sudo ./card_polling`

My end goal here is to use my [NFC Ring](http://nfcring.com) to start/play/pause videos in xbmc using the Pi shield.. Wish me luck..

Q: I get Failed to open bal. A: You forgot to run card\_polling as sudo.. `sudo ./card_polling`
