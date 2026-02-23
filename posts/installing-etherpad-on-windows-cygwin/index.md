---
title: "Installing Etherpad on Windows (CYGWIN)"
date: 2010-02-18
categories: 
  - "etherpad"
  - "guide"
  - "howto"
---

**[The new documentation for how to deploy Etherpad Lite on Windows is available here](http://etherpad.org/2011/08/11/installing-etherpad-lite-on-windows/) -- You should refer to this.**

**BELOW IS THE OLD DOCUMENTATION FOR ETHERPAD FULL**

Grab the latest Etherpad .zip from [http://etherpad.org](http://etherpad.org) and extract to c:\\etherpad

Download and install Cygwin from [http://www.cygwin.com/](http://www.cygwin.com/) - use defaults

Download Scala from [http://www.scala-lang.org/sites/default/files/linuxsoft\_archives/downloads/distrib/files/scala-2.7.7.final.zip](http://www.scala-lang.org/sites/default/files/linuxsoft_archives/downloads/distrib/files/scala-2.7.7.final.zip) and extract to c:\\etherpad\\scala-2.7.7

Download and install MySQL server from [http://dev.mysql.com/downloads/mysql/](http://dev.mysql.com/downloads/mysql/) Create a MySQL database "etherpad" and a database user "etherpad"

Download the MySQL connector from [http://dev.mysql.com/downloads/mirror.php?id=402367](http://dev.mysql.com/downloads/mirror.php?id=402367) and extract to c:\\etherpad\\mysql-connector-java-5.1.16

Download Java from [http://www.oracle.com/technetwork/java/javase/downloads/jdk-6u25-download-346242.html](http://www.oracle.com/technetwork/java/javase/downloads/jdk-6u25-download-346242.html) and extract to c:\\etherpad\\JDK1.6\_23

Open Cygwin (doubleclick on icon)

Change directory to Etherpad: \[bash\]cd /cygdrive/c/Etherpad/\[/bash\]

Copy the Libraries from one folder to another (temp fix): \[bash\]cp /cygdrive/c/Etherpad/infrastructure/lib/\* /cygdrive/c/Etherpad/infrastructure/ace/lib\[/bash\]

Begin your build (if this errors check your task manager and check there are no java instances running that may cause a conflict): \[bash\]bin/build.sh\[/bash\]

Copy the default config to the correct location: \[bash\]cp etherpad/etc/etherpad.localdev-default.properties etherpad/etc/etherpad.local.properties\[/bash\]

Edit etherpad/etc/etherpad.local.properties and set etherpad.SQL\_JDBC\_URL = jdbc:mysql://localhost:3306/etherpad etherpad.SQL\_PASSWORD = yoursqlpassword etherpad.SQL\_USERNAME = etherpad etherpad.adminPass = somestrongpassword topdomains = yourhostname.com,localhost

You can now run etherpad via: \[bash\]bin/run.sh\[/bash\]

Access your Etherpad server at: http://localhost:9000/

**BELOW IS THE OLD DOCUMENTATION THAT I AM LEAVING FOR THE SAKE OF HISTORY AND FOR REFERENCE. DAVE. WE CAME A LONG WAY DAVE.. IT'S BEEN EMOTIONAL :~**

Below is my documentation that is sketchy, you should [**follow this guide instead.**](http://bitbucket.org/gyokuro/etherpad-win/wiki/Home)

In Windows: - Install Java, Scala, MySQL, mysqlconnector and Mercurial under Windows. - JAVA should be set to the java executable. - JAVA\_HOME should be set to the main jdk directory. - SCALA should be set to the scala executable. - SCALA\_HOME should be set to the main scala distribution directory. - PATH should contain $JAVA, $SCALA, and mysql - MYSQL\_CONNECTOR\_JAR should be set to the mysql-connector JAR file included in the mysql-connector download.

\- Install Cygwin.

[These Files are needed](http://primaryschoolict.com/epad_cygwin.rar) in /etherpad/trunk/ since the archive holds files both in the etherpad and the infrastructure subfolder.

1. Make a backup of your bin folder
2. Extract the contents of the above .Rar file to the bin folder
3. Run bin/rebuildjar.sh
4. After installation run bin/run-local.sh

Full docs coming later. Post questions as comments and I should be able to answer.

All props goto Jutsi for discovering the solution. Feeling confident without the full docs? Follow the unix docs for config settings and you should be good to go.

See also: Etherpad-win repository all props to Gyokuro:  [http://bitbucket.org/gyokuro/etherpad-win/overview/](http://bitbucket.org/gyokuro/etherpad-win/overview/) Etherpad-win wiki all props to Gyokuro: [http://bitbucket.org/gyokuro/etherpad-win/wiki/](http://bitbucket.org/gyokuro/etherpad-win/wiki/))
