---
title: "Success: optimizing the Etherpad Java VM"
date: 2010-01-21
categories: 
  - "etherpad"
---

After weeks of tweeking i finally found an environment that works smoothly

  

2GB VM

  

I kept my ${MXRAM} at 1800M

  

$JAVA -classpath $CP \\

\-server \\

\-Xmx${MXRAM} \\

\-Xms${MXRAM} \\

\-Djava.awt.headless=true \\

\-XX:MaxGCPauseMillis=500 \\

\-XX:+UseParallelGC \\

\-Dappjet.jmxremote=true \\

$JAVA\_OPTS \\

net.appjet.oui.main \\

\--configFile=${cfg\_file} \\

"$@"

  

Note the lack of logging etc.
