---
title: "Postfix RBL / MTA level drop spam prior to it hitting spamassassin"
date: 2010-03-22
---

This is the config I use to drop spam - paste this to the bottom of your main.cf:

\[bash\] disable\_vrfy\_command = yes smtpd\_delay\_reject = yes smtpd\_helo\_required = yes smtpd\_helo\_restrictions = permit\_mynetworks, reject\_non\_fqdn\_hostname, reject\_invalid\_hostname, permit smtpd\_recipient\_restrictions = permit\_mynetworks,reject\_unauth\_destination reject\_rbl\_client list.dsbl.org, reject\_rbl\_client sbl.spamhaus.org, reject\_rbl\_client cbl.abuseat.org, reject\_rbl\_client dul.dnsbl.sorbs.net, smtpd\_error\_sleep\_time = 1s smtpd\_soft\_error\_limit = 10 smtpd\_hard\_error\_limit = 20 \[/bash\]
