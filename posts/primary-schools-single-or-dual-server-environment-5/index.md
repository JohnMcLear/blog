---
title: "Primary Schools – Single or Dual Server Environment."
date: 2012-03-08
categories: 
  - "ict"
  - "primary-school"
---

![](images/tumblr_lsovzeh9bf1qe0eclo1_r5_500.gif)  
One of the biggest single I.T. purchases a school will make is the replacement of its servers. With typical costs of £2000 – £2500 per server, possibly with installation and migration costs on top of that, it’s no wonder that support providers, keen to ensure their customers are making the best use of their budget are questioning whether schools need the traditional two server approach.

## Why do we have two servers?

The traditional setup within primary schools has been two physically disjoint networks, one for curriculum users (teaching staff and pupils), and one for the administrative staff. This provided two sets of ring-fenced resources, both servers acting as file and print servers for their users, with the admin server also hosting the SQL databases for MIS systems. The security of these databases was often cited as a reason for keeping the two networks disjoint. However, using robust security practices will be just as effective at protecting sensitive data, and much less restrictive to users authorised to use that data.

## What’s changing?

The changes in the way technology is utilized mean that there is more and more cross-over between traditional admin and curriculum use.  
Members of the senior leadership team, who have traditionally needed to connect to the admin network, may be teaching and also need access to the curriculum server resources; this would require logging on to a different computer, one connected to the curriculum network, with a different user name and password.  
Teaching staff might wish to have access to the MIS systems on the admin server, whether this is for something simple like desktop registering, or more advanced, such as pupil progress recording.

## So how is it changing?

The first step in closer integration is the physical joining of the two networks, to allow data to pass between them. This allows for the crossover of data between the systems, but doesn’t allow for some of the greater benefits that can be achieved through the joining of both servers into a single domain. With all machines at a site belonging to a single domain for the whole school, it doesn’t matter whether a user is a curriculum or an admin user, they can log on to any client machine, with a single set of user credentials, and have access to their data, whether it is stored on the curriculum server, the admin server or both. There is also potentially simplified access to shared resources such as printers, as well as greater flexibility in the event of a particular printer failure.

## So can we just have one server?

The answer to this question is simple enough, yes, yes you can. With the relative power and storage capacity of computers increasing all the time, many schools who are keen to make budgetary savings see moving their current curriculum and admin servers on to a single machine to be an excellent way to cut costs. Essentially all you are really adding to your MIS server loading is the file and print server role for the curriculum users, and a little overhead for handling things like user authentication. Given that your new server will have a more powerful processor, more memory and probably a better disk subsystem, all that you need to do is add sufficient storage capacity for the curriculum users and you can happily run your school on a single server.

## Should I have just one server?

In many ways this is a trickier question. The single server approach, whilst seeming attractive, does remove some of the potential resiliency you could achieve through retaining a two server architecture. In theory it would be possible to make the servers fully redundant with data being mirrored across both servers. Then in the event of one failing, a few minor configuration changes would allow the school to continue on virtually unaffected in the event of server failure, something which would be impossible in the single server school, (or even the traditional style two server school).

It is unlikely that the complexity of such a high degree of resiliency is necessary (or even desirable) in a primary school environment. However having a second server to help maintain the core server functions such as active directory, DNS, DHCP etc., would allow many I.T. functions to continue unaffected within the school whilst a failed server was replaced. This is something well worth considering in the current environment where the internet can provide access to teaching resources and applications in the event that local server based applications are unavailable.

## Weighing it up. . .

Single server offers potential savings on hardware costs, and systems management overheads, only having to administer a single server. Its potential weakness is that the server becomes a single point of failure for the whole school, rather than just the curriculum users or admin the staff. However so long as the school have reliable backups, both of it data and active directory, a recovery shouldn’t take more than 48 hours (assuming access to replacement hardware).

Twin server systems have the advantage of maintaining the active directory in the event of a server failure. This will allow users to log on, and with a little forethought in implementation allow access to the internet, shared printers and whatever user data is available on the remaining server whilst awaiting the install and configuration of the replacement server.

Article by Steve Dulson, schools network engineer at [Primary Technology](http://primaryt.co.uk)
