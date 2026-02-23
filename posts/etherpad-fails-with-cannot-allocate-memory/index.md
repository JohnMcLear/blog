---
title: "Etherpad fails with Cannot Allocate memory"
date: 2010-11-02
categories: 
  - "etherpad"
---

Java likes memory.  VPS has some serious issues with this.  This is not an Etherpad issue.

**Problem:** java.io.IOException: Cannot run program "cp": java.io.IOException: error=12, Cannot allocate memory at java.lang.ProcessBuilder.start(ProcessBuilder.java:460) at java.lang.Runtime.exec(Runtime.java:593) at java.lang.Runtime.exec(Runtime.java:431) at java.lang.Runtime.exec(Runtime.java:328) at Main$$anon$2.copyFile$1((virtual file):252) at Main$$anon$2.doMake((virtual file):263) at Main$$anon$2.((virtual file):337) at Main$.main((virtual file):4) at Main.main((virtual file)) at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method) at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:39) at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:25) at java.lang.reflect.Method.invoke(Method.java:597) at scala.tools.nsc.ObjectRunner$$anonfun$run$1.apply(ObjectRunner.scala:75) at scala.tools.nsc.ObjectRunner$.withContextClassLoader(ObjectRunner.scala:49) at scala.tools.nsc.ObjectRunner$.run(ObjectRunner.scala:74) at scala.tools.nsc.ScriptRunner$.scala$tools$nsc$ScriptRunner$$runCompiled(ScriptRunner.scala:381) at scala.tools.nsc.ScriptRunner$$anonfun$runScript$1.apply(ScriptRunner.scala:414) at scala.tools.nsc.ScriptRunner$$anonfun$runScript$1.apply(ScriptRunner.scala:413) at scala.tools.nsc.ScriptRunner$.withCompiledScript(ScriptRunner.scala:351) at scala.tools.nsc.ScriptRunner$.runScript(ScriptRunner.scala:413) at scala.tools.nsc.MainGenericRunner$.main(MainGenericRunner.scala:168) at scala.tools.nsc.MainGenericRunner.main(MainGenericRunner.scala) Caused by: java.io.IOException: java.io.IOException: error=12, Cannot allocate memory at java.lang.UNIXProcess.(UNIXProcess.java:148) at java.lang.ProcessImpl.start(ProcessImpl.java:65) at java.lang.ProcessBuilder.start(ProcessBuilder.java:453) ... 22 more

**Cause:** VPS has no swap memory free.

**Solution:** Do not use a VPS as [documented here](https://mclear.co.uk/2010/02/24/etherpad-minimum-requirements-memory-ram/).  If you must use a VPS ensure you have some swap space.
