---
title: "Using git bisect to debug Etherpad issues"
date: 2013-04-02
categories: 
  - "etherpad"
  - "git"
tags: 
  - "etherpad"
  - "git"
  - "github"
---

Sometimes stuff gets broken due to new commits, we need to know which commit broke functionality.

To do this 

```
git pull git checkout develop
```



Ensure the bug exists then 

```
git checkout master
```



Ensure the bug doesn't exist. If it does checkout older versions IE git checkout release/1.2.8 Next begin the bisect process..



```
git bisect start
```



Tell bisect that master is fine 

```
git bisect good
```



Tell bisect that develop is bad 

```
git checkout develop git bisect bad
```



Bisect will then deliver you a commit state, test this new version.. 

```
bin/run.sh
```



Test, Control C.. Did it work? If so... 

```
git bisect good
```



Did it not work? If so.. 

```
git bisect bad
```



Rinse repeat 'git bisect good' and/or 'git bisect bad' until it delivers you with a commit SHA then create an issue including the details from the SHA.

Basically bisect will tell you which commit introduced the bug.
