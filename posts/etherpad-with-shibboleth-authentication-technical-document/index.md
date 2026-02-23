---
title: "Etherpad with Shibboleth Authentication (Technical document)"
date: 2010-03-05
categories: 
  - "etherpad"
  - "shibboleth"
---

[![](images/ShibEpad.png)](http://4.bp.blogspot.com/_NislCXjnul0/S4_e2Pn6LnI/AAAAAAAACsw/WExEbrus3vM/s1600-h/ShibEpad.png)I want to login to Etherpad with my UK federation/Shibboleth login.  
  
Firstly I need to get my SP working.  
Configure SP & Apache initially..  
I need to [configure Tomcat to use Shibboleth for Authentication](http://wiki.oss-watch.ac.uk/ShibbolethTomcatIntegration) [configure Jetty to use Shibboleth Authentication.](http://docs.codehaus.org/display/JETTY/Configuring+AJP13+Using+mod_jk)  
Once this is done I will have the users attributes as environment variables.  
  
Now I have the variables I need to create a script to check the variables and create an account if required.  All sounds pretty simple right?  Let's hope so, as I make progress I will document my changes.  
  
I'm referring to the LDAP plugin patch code for how to handle "talking to etherpad".  
  
ETA is 3/4 weeks.  Sucks that I need to use Apache but oh well!!  
  
Note:  Etherpad runs on Jetty, not Tomcat and doesn't require Apache.  It is the shibboleth element of this that requires Apache to operate.  
  
Note:  Thanks to nuba for reminding me about Jetty.
