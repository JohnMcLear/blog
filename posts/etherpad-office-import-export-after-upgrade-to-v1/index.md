---
title: "Etherpad Office Import &amp; Export after Upgrade to V1"
date: 2010-05-05
categories: 
  - "etherpad"
---

V1 does not natively support office import / exports yet due to a licensing issue but if you had it working before you can do a few steps that will get you started.  We use Open Office in a headless mode to accomplish this.

1\.  Copy the cos.jar to infrastructure/lib (replacing etherpadbackup is the folder you backed your original etherpad installation to (etherpad <v1)

\[bash\] cp /usr/local/etherpadbackup/trunk/infrastructure/lib/cos.jar /usr/share/etherpad/infrastructure/lib/ \[/bash\]

2\. Run soffice in headless mode

\[bash\] /usr/bin/soffice -headless -nofirststartwizard -accept=”socket,host=localhost,port=8100;urp;StarOffice.Service” \[/bash\]

3\. Uncomment the lines in execution.scala that are commented "REMOVED\_COS\_OF\_COS"

4\. Reset your exports

\[bash\] export JAVA\_HOME="/usr/lib/jvm/java-6-sun" export SCALA\_HOME="/usr/share/java" export JAVA="/usr/bin/java" export SCALA="/usr/bin/scala" export PATH="/usr/bin:/usr/bin:/usr/local/mysql/bin:$PATH" export MYSQL\_CONNECTOR\_JAR="/usr/share/java/mysql-connector-java-5.1.10.jar" \[/bash\]

4\. Rebuild and Run.

\[bash\] cd /usr/share/etherpad/etherpad/ bin/rebuildjar.sh clearcache /etc/init.d/etherpad stop /etc/init.d/etherpad start \[/bash\]

Note, in your etherpad.properties.local you should have the line:

\[bash\]etherpad.soffice = /usr/bin/soffice\[/bash\]

It is important so don't forget it.
