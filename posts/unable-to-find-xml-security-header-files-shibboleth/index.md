---
title: "Unable to find XML-Security header files (shibboleth)"
date: 2009-10-23
categories: 
  - "shibboleth"
---

When installing shibboleth 2+ on debian you may get the error

  

[unable to find XML-Security header files](http://www.google.co.uk/search?rlz=1C1GGLS_en-GBGB344GB344&sourceid=chrome&ie=UTF-8&q=unable+to+find+XML-Security+header+files)

  

This is due to a missing lib

  

Run the command: **apt-get install libxml-security-c-dev**

  

And all your dreams will come true.
