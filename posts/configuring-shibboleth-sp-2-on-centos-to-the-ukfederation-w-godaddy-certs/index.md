---
title: "Configuring Shibboleth SP 2 on CentOS to the ukfederation w/ Godaddy certs"
date: 2009-10-27
categories: 
  - "certificates"
  - "janet"
  - "key"
  - "shibboleth"
  - "shibboleth2-xml"
  - "ssl"
  - "ukfederation"
---

Part 2. Shibboleth Config (6 hours)

\[bash\] cd /etc/shibboleth wget http://metadata.ukfederation.org.uk/ukfederation.pem wget http://metadata.ukfederation.org.uk/ukfederation-metadata.xml \[/bash\]

Edit shibboleth2.xml

> Replace all instances of sp.example.org with your Entity ID ie sp.yourdomain.com
> 
> Search for ApplicationDefaults
> 
> Add homeURL="https://sp.domainz.com/ahomeurl" under entityID - homeURL is the first url of the resource if none is specified.
> 
> Search for <sessions
> 
> **Before the default example (Reading Default example directs to a speci... " Insert:**
> 
> \[bash\] <SessionInitiator isDefault="true" id="UKFederation" Location="/WAYF/UKFederation" type="WAYF" defaultACSIndex="5" URL="https://wayf.ukfederation.org.uk/WAYF" /> \[/bash\]
> 
> Search for exportLocation
> 
> Under exportLocation replace http://localhost with https://localhost
> 
> Replace all instances of root@localhost with the technical support email address
> 
> Search for MetadataProvider
> 
> This bit gets messy so pay close attention.....
> 
> After the line reading Insert
> 
> \[bash\] <MetadataProvider type="XML"
> 
> uri="http://metadata.ukfederation.org.uk/ukfederation-metadata.xml"
> 
> backingFilePath="/etc/shibboleth/ukfederation-metadata.xml" reloadInterval="14400">
> 
> <MetadataFilter type="RequireValidUntil" maxValidityInterval="2592000"/>
> 
> <SignatureMetadataFilter certificate="ukfederation.pem"/>
> 
> </MetadataProvider> \[/bash\]
> 
> Search for the line **Delete it or comment it out.**
> 
> Directly below it paste the following:
> 
> /etc/shibboleth/sp.key /etc/shibboleth/sp.crt
> 
> Don't forget to replace yourpassword with your key password if you have set one!

For now we are done in shibboleth2.xml

Run ./keygen.sh to generate your new key pair \[bash\] mv sp-key.pem sp.key mv sp-cert.pem sp.crt \[/bash\]

[Now we must configure Apache for shibboleth](https://mclear.co.uk/2009/10/27/configuring-apache-for-shibboleth-on-centos-to-the-ukfederation-w-godaddy-certs/)
