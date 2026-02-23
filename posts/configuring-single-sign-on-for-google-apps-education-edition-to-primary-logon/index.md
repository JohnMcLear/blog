---
title: "Configuring Single Sign on for Google Apps Education Edition to Primary Logon"
date: 2009-11-24
categories: 
  - "apps"
  - "google"
  - "ict"
  - "primary"
  - "primary-email"
  - "primary-school-email"
  - "primary-school-ict"
  - "school-email"
---

If you use Primary Logon or have a Shibboleth IDP representing your school you can achieve this. Visit [http://google.com/a/yourdomain.com](http://google.com/a/yourdomain.com) ß remember to replace yourdomain.com with your domain

1. Login with your username and password
2. Click Advanced Tools
3. Click Set up single Sign on
4. Under Sign-in page paste:
5. https://idp.primarylogon.co.uk/idp/profile/SAML2/Redirect/SSO
6. Under sign-out page paste:
7. [](http://yourdomain.com/)[http://yourdomain.com](http://yourdomain.com/) or [http://primarylogon.co.uk](http://primarylogon.co.uk/) ß remember to replace yourdomain.com with your domain
8. Under Change password URL paste:
9. https://primarylogon.co.uk/password
10. Click Browse to select your Verification Certificate – Type in http://primarylogon.co.uk/idp.crt
11. Click Save Changes
12. Click Users and groups
13. Click Settings
14. Put a Tick in the box “Enable Provisioning API”
15. Click Save Changes
16. Log out of Google apps
17. Sign into Primary Logon at [http://primarylogon.co.uk](http://primarylogon.co.uk/)
18. You need to be admin user on Primary Logon to do this.
19. Click Control Panel
20. Click Google Apps Docs
21. Click Purchase
22. Click OK
23. Where you see Google Docs near the top you will see an input box. Type your school’s domain In this input box.
24. Click the pencil.
25. Click OK
26. Wait 24 hours for user accounts to be made.

Note: Schools who don’t use Primary Logon will have to a) contact their schools Shibboleth/UK Federation Identity provider(Probably your LA/Council) and request that they add a record to their IDP for your Google apps. Instructions to do this are available at http://www.mclear.co.uk/2009/11/shibboleth-idp-configuration-for.html and b) get the correct Identity Provider Sign in page, Sign out page and Change Password URL from their Identity Provider.

**[Now you are done configuring you can get to Testing your Primary School Google Apps Education Edition Configuration](https://mclear.co.uk/2009/11/24/testing-your-primary-school-google-apps-education-edition-configuration/) [à](https://mclear.co.uk/2009/11/24/testing-your-primary-school-google-apps-education-edition-configuration/)**
