---
title: "Shibboleth IDP configuration for multiple organizations &amp; Google apps"
date: 2009-11-21
categories: 
  - "apps"
  - "google"
  - "idp"
  - "shibboleth"
  - "single-sign-on"
  - "sso"
---

So you want to configure your IDP to allow logins from multiple organizations google apps? IE you want SchoolA to sign into http://docs.SchoolA.com and SchoolB to sign into http://docs.SchoolB.com.

The documentation on googles site isn't very clear so here are some step by step instructions.

Before you even make a start, backup ALL of your IDP configuration files.

PreReqs:

- Working IDP
- Google Apps Educational Account
- CNAME records set for docs.SchoolA.com and docs.SchoolB.com

Firstly [complete the steps](https://shibboleth.usc.edu/docs/google-apps/) documented beautifully by [Will Norris](http://willnorris.com/) - Do the config for any school, we are just doing this to make sure you have a working IDP.

Test the above config changes by browsing to http://apps.SchoolA.com where SchoolA.com is the domain of the school you have configure google apps for. A usual misconception new users have about google apps is that it will create user accounts when you first login. This is not true. Your user account name on google apps must match the value being passed by the IDP. I have written a perl google apps provisioning tool, get in touch if you want it.

It worked? Great! If not, don't continue. Get Will's configuration working first then continue.

Now let's get started configuring your IDP to allow multiple organizations to authenticate to Google Apps.

1\. Log into your google apps admin account at http://google.com/a/SchoolA.com

2\. Click Advanced tools - Set up Single Sign on - Tick Use a domain specified issuer

You are done in Google Apps. Congrats.

3\. Ssh into your IDP

4\. Is your Google Metadata located at /opt/shibboleth-idp/metadata/google-metadata.xml ? It should be, if not, modify the below guide to suite your paths. It will make sense..

5\. Edit /opt/shibboleth-idp/metadata/google-metadata.xml to read

\[code\] <EntityDescriptor entityID="google.com/a/schoola.com" xmlns="urn:oasis:names:tc:SAML:2.0:metadata"> <SPSSODescriptor protocolSupportEnumeration="urn:oasis:names:tc:SAML:2.0:protocol"> <NameIDFormat>urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified</NameIDFormat> <AssertionConsumerService index="1" Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST" Location="https://www.google.com/a/schoola.com/acs" /> </SPSSODescriptor> </EntityDescriptor> \[/code\]

6\. Copy google-metadata.xml to google-metadata2.xml

7\. Edit /opt/shibboleth-idp/metadata/google-metadata2.xml to read

\[code\] <EntityDescriptor entityID="google.com/a/schoolb.com" xmlns="urn:oasis:names:tc:SAML:2.0:metadata"> <SPSSODescriptor protocolSupportEnumeration="urn:oasis:names:tc:SAML:2.0:protocol"> <NameIDFormat>urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified</NameIDFormat> <AssertionConsumerService index="1" Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST" Location="https://www.google.com/a/schoolb.com/acs" /> </SPSSODescriptor> </EntityDescriptor> \[/code\]

8\. Edit /etc/shibboleth/relying-party.xml

9\. Smile

10\. Make me a cup of tea

11\. Replace the entire Relying Party section for the google connectivity. After you are done it should read something like...

\[code\] <RelyingParty id="google.com/a/schoola.com" provider="https://idp.youridp.com/idp/shibboleth" defaultSigningCredentialRef="IdPCredential"> <ProfileConfiguration xsi:type="saml:SAML2SSOProfile" encryptAssertions="never" encryptNameIds="never" /> </RelyingParty> <RelyingParty id="google.com/a/schoolb.com" provider="https://idp.youridp.com/idp/shibboleth" defaultSigningCredentialRef="IdPCredential"> <ProfileConfiguration xsi:type="saml:SAML2SSOProfile" encryptAssertions="never" encryptNameIds="never" /> </RelyingParty> \[/code\]

12\. Search for Google.com again - look for the MetadataProvider section

13\. Copy and paste the first reference replacing .xml with 2.xml, change the second schools id value to GoogleMD2, it should read something like this:

\[code\] <MetadataProvider id="GoogleMD" xsi:type="FilesystemMetadataProvider" xmlns="urn:mace:shibboleth:2.0:metadata" metadataFile="/opt/shibboleth-idp/metadata/google-metadata.xml" maintainExpiredMetadata="true" /> <MetadataProvider id="GoogleMD2" xsi:type="FilesystemMetadataProvider" xmlns="urn:mace:shibboleth:2.0:metadata" metadataFile="/opt/shibboleth-idp/metadata/google-metadata2.xml" maintainExpiredMetadata="true" /> \[/code\]

Congrats, you are done in relying-party.xml!

14\. Edit /etc/shibboleth/attribute-filter.xml

15\. Search for google.com

16\. Edit the value to read "google.com/a/schoola.com"

17\. Copy and paste the policy, replace schoola.com with schoolb.com in the new policy.

It should read:

\[code\] <AttributeFilterPolicy> <PolicyRequirementRule xsi:type="basic:AttributeRequesterString" value="google.com/a/schoola.com" /> <AttributeRule attributeID="principal"> <PermitValueRule xsi:type="basic:ANY" /> </AttributeRule> </AttributeFilterPolicy> <AttributeFilterPolicy> <PolicyRequirementRule xsi:type="basic:AttributeRequesterString" value="google.com/a/schoolb.com" /> <AttributeRule attributeID="principal"> <PermitValueRule xsi:type="basic:ANY" /> </AttributeRule> </AttributeFilterPolicy> \[/code\] 18. I restarted tomcat using the ./Shutdown ./Startup script to test and it worked fine. Test by browsing to http://apps.schoola.com/(assuming you have this cname set). If you have problems please check that you replaced schoola.com and schoolb.com with your domain and also your IDP references.
