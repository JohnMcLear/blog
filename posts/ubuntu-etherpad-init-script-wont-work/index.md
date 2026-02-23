---
title: "Ubuntu Etherpad Init script won't work"
date: 2010-08-10
categories: 
  - "etherpad"
---

This is due to a permission error on the log folder

Quickest fix is:

\[bash\] chown -R etherpad /var/log/etherpad \[/bash\]

Try that then do \[bash\] cd /usr/share/etherpad/bin sudo -u etherpad ./run.sh \[/bash\]
