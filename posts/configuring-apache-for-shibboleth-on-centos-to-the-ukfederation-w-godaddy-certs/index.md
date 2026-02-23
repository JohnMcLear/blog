---
title: "Configuring Apache for Shibboleth on CentOS to the ukfederation w/ Godaddy certs"
date: 2009-10-27
categories: 
  - "certificates"
  - "csr"
  - "godaddy"
  - "janet"
  - "key"
  - "openssl"
  - "shibboleth"
  - "ukfederation"
---

## Part 3. Apache config. (1 hour)

\[bash\] cd /etc/shibboleth openssl genrsa -des3 -out external.key 2048 openssl req -new -key external.key -out external.csr \[/bash\]

The above will create a CSR request for your resource, when asked what the common name is enter something like shib.yourdomain.com - **DO NOT** use sp.yourdomain.com or the same common name as you used to register your SP!

Edit the CSR and **copy its contents into clipboard**. Then login to your godaddy hosting account and **paste the CSR request into your certificate reques****t.**

```
Godaddy will do their thing then get back to you with a CRT a few files usually within 24 hours.
```

```
When they get back to you with the files copy or download them the files to /etc/shibboleth
```

```
Rename shib.yourdomain.com.crt to external.crt
```

```
Rename gd_bundle.crt to external_int.crt and place it in /etc/shibboleth
```

**```
Edit /etc/httpd/conf.d/ssl.conf
```

> Replace
> 
> ```
> SSLCertificateKeyFile /etc/pki/tls/private/localhost.key
> ```
> 
> ```
> With
> ```
> 
> ```
>  SSLCertificateKeyFile /etc/shibboleth/external.key
> ```
> 
> **Replace**
> 
> SSLCertificateFile /etc/pki/tls/private/localhost.crt
> 
> With
> 
> SSLCertificateFile /etc/shibboleth/external.crt
> 
> ```
> Under SSLCertificateKeyFile paste SSLCertificateChainFile /etc/shibboleth/external_int.crt
> ```

```
Edit /etc/httpd/conf/httpd.conf
```

> ```
> Replace
> ```
> 
> ```
>  UseCanonicalName Off
> ```
> 
> ```
> With
> ```
> 
> ```
>  UseCanonicalName On
> ```
> 
> ```
> Find the line beginning with ServerName
> ```
> 
> ```
> Comment it out
> ```
> 
> ```
> Below it type ServerName shib.yourdomain.com:80
> ```

```
/usr/sbin/apachectl restart
```

```

/usr/sbin/apachectl start

```

```
The above commands will restart Apache or start it if it hasn't already been started
```

```
Edit  /etc/sysconfig/iptables & above all REJECT rules paste:
```

> ```
> -A RH-Firewall-1-INPUT -m state --state NEW -m tcp -p tcp --dport 80 -j ACCEPT
> ```
> 
> ```
> -A RH-Firewall-1-INPUT -m state --state NEW -m tcp -p tcp --dport 443 -j ACCEPT
> ```
> 
> ```
> -A RH-Firewall-1-INPUT -m state --state NEW -m tcp -p tcp --dport 8443 -j ACCEPT
> ```

```
/sbin/service iptables restart
```

```
If everything restarts without any errors then:
```

```
Continue to the testing phase
```**
