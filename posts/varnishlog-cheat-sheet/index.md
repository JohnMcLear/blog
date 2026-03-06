---
title: "Varnishlog cheat sheet"
date: 2011-04-25
categories: 
  - "varnish"
---

BELOW IS VARNISH V3

Look at an incoming client request of a specific URL: 

```
varnishlog -c -m RxURL:"readysetlearn/readysetlearn.htm"
```



Look at a a backend request of a specific URL: 

```
varnishlog -b -m TxURL:"readysetlearn/readysetlearn.htm"
```



See requests for one specific Hostname: 

```
varnishlog -c -m RxHeader:"Host: etherpad.org"
```



See the age of the cache objects for a specific hostname: 

```
varnishlog -c -m RxHeader:"Host: etherpad.org" | grep Age
```



BELOW IS VARNISH < V3

Look at an incoming client request of a specific URL: 

```
varnishlog -c -o RxURL readysetlearn/readysetlearn.htm
```



Look at a a backend request of a specific URL: 

```
varnishlog -b -o TxURL readysetlearn/readysetlearn.htm
```



See requests for one specific Hostname: 

```
varnishlog -c -o RxHeader "Host: etherpad.org"
```



See the age of the cache objects for a specific hostname: 

```
varnishlog -c -o RxHeader "Host: etherpad.org" | grep Age
```



If an item has a high age it means that varnish is hitting the cache for it.

Thanks to Mithrandir from the #Varnish IRC channel for helping out and thanks to [Tomnomnom](http://Tomnomnom.com) for V3 help!.
