---
title: "Etherpad - cp: missing destination file operand after `lib/'"
date: 2010-08-24
categories: 
  - "etherpad"
---

This error is caused by the MYSQL\_CONNECTOR\_JAR environment variable/export not being set.

Set it by typing..

\[bash\] export MYSQL\_CONNECTOR\_JAR="path to your mysql connector.jar" \[/bash\]
