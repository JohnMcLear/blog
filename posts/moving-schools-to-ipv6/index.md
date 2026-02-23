---
title: "Moving schools to IPv6"
date: 2011-02-24
categories: 
  - "ict"
  - "primary"
  - "primary-school"
  - "primary-school-ict"
---

I have a unique position when it comes to moving schools to [IPv6](http://en.wikipedia.org/wiki/IPv6 "IPv6") in that I work with a [technical support](http://en.wikipedia.org/wiki/Technical_support "Technical support") team, a hosted [web services](http://en.wikipedia.org/wiki/Web_service "Web service") team and an internet reseller team so if you think about the connectivity "bridge" then we cover all bases.  When I refer to the bridge I mean we are responsible for the request from a web browser all the way through the [web service](http://en.wikipedia.org/wiki/Web_service "Web service") servicing that request.

## What is IPv6?

So as far as I see it we have a few major considerations and questions to ask and these are...

## Do our school routers support IPv6?

Some of our schools have connectivity from RBCs and some from our resell Internet connectivity, it is much easier for us to work with our resell partners to enable IPv6 as our resell partners advocate moving towards IPv6 as they have an interest in not running out of [IPv4 addresses](http://en.wikipedia.org/wiki/IPv4 "IPv4").  There is no doubt the move towards IPv6 will require collaboration between different internal departments and different [ISPs](http://en.wikipedia.org/wiki/Internet_service_provider "Internet service provider").

## Do our school wireless access points care about IPv6?

Nearly all of the schools we work with have recently refreshed their wireless networks with either Cisco or Meru wireless solutions that we can be confident will properly support IPv6.  You might not think an AP support of IPv6 is important but it's the basics such as configuring the device out of the box or IPv6 [DHCP](http://en.wikipedia.org/wiki/Dynamic_Host_Configuration_Protocol "Dynamic Host Configuration Protocol") client support that can sting you later.  Although APs don't do any routing it is still important the AP & Management system are IPv6 ready and configured.

## Do our school laptop/pc/netbook devices support IPv6?

The vast majority of client devices in schools will support IPv6 out of the box however we will need to get our hardware inventory tool to push a report letting us know which devices don't.  If the device doesn't support IPv6 it is likely that the device will just remain on IPv4 until it is eventually phased out so it doesn't really even matter so much.

## Do our web services host names resolve to IPv6 address(as well as IPv4)?

Because we use [round robin DNS](http://en.wikipedia.org/wiki/Round-robin_DNS "Round-robin DNS") on a lot of our web services we delayed implementing IPv6 however we aim to have this done before June the 1st which is world IPv6 day.

## Remote access and network monitoring

Our remote access all works over IPv4 addresses so we may need to change this but with less than 100 users currently using the service we can worry about this bridge if/when we get there.  Personally I'm not a big fan of schools remoting into their school for security reasons but I understand sometimes it is a necessity although in the future I doubt this will be as predominant although this will require a restructure of SIMS/CMIS licensing models.

## How do we alter Windows DHCP?

The majority of the schools use [Microsoft Windows](http://www.microsoft.com/WINDOWS "Windows") DHCP for issuing IPv4 addresses at current, we will need to alter the scope and ensure we are pushing IPv6 addresses.  This video shows the process involved in [Server 2008](http://www.microsoft.com/windowsserver2008/en/us/default.aspx "Windows Server 2008") to do this.  We are constantly moving schools onto server 2008.  **Note: If your technical support provider recommends Server 2003 please show them this page.**

## What other work does our technical support team need to do?

I think we need to sit down and discuss this and over time we will update this page.

## What time-scale should we be looking at for completed IPv6 deployments?

I think aiming to get all of our schools IPv6 ready by mid 2012 should be okay.

[![Enhanced by Zemanta](images/zemified_e.png)](http://www.zemanta.com/ "Enhanced by Zemanta")
