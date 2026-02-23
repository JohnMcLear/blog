---
title: "Etherpad database tests"
date: 2015-03-02
categories: 
  - "etherpad"
---

I was curious how much database affected Etherpad performance and with the new load test tool it was pretty easy for me to test.. I expect Redis will be the most performant as it is tuned for KVS, I expect MySQL will follow second and DirtyDB will come in somewhere behind..

The idea behind the test is to do a snapshot of usage, simulating a lot of clients and authors generating and consuming a lot of content until the server can no longer serve responses to requests in a timely fashion (100ms)...

I tested the following databases..

DirtyDB 0.6.9, standard. Redis 2.8.4, standard. MySQL 14.14, MYISAM db.

I used the following configs, obviously commenting out when not using a specific database:

\[javascript light="true"\] "dbType" : "dirty", "dbSettings" : { "filename" : "var/dirty.db" } "dbType" : "mysql", "dbSettings" : { "user" : "etherpad", "host" : "localhost", "password": "test", "database": "etherpad" } "dbType" : "redis", "dbSettings" : { "host" : "localhost", "port" : 6379, "database" : 0 } \[/javascript\]

Important notes: \* I killed the Etherpad server process in between each run. \* I ran the same test 3 times and took a mean average of the results. \* The server ran on one of my cores, the testing client on the other. \* The read write ops are ~ 5:1 (read/write) but Etherpad will be holding data in memory so it's plausible the database is hardly being touched at all. \* Node version is v0.12 - Etherpad sha is cc0eaba7e262ccc97aa0ce34b5e4d0f6eac4fd08

The command used to run the test: \[javascript\]etherpad-load-test\[/javascript\]

Every 5 second this test creates new users in the ratio of 4 lurkers to 1 author, the author contributes content. After 50 seconds, 10 authors will be on the pad and 40 lurkers. All of these authors will be generating content. The test continues until responses are no longer processed within 100ms.

## Results

**Redis** Clients Connected: 304 Authors Connected: 76 Lurkers Connected: 228 Sent Append messages: 15337 Commits accepted by server: 15310 Commits sent from Server to Client: 33638

**MySQL** Clients Connected: 320 Authors Connected: 80 Lurkers Connected: 240 Sent Append messages: 16607 Commits accepted by server: 16506 Commits sent from Server to Client: 32201

**DirtyDB** Clients Connected: 308 Authors Connected: 77 Lurkers Connected: 231 Sent Append messages: 15426 Commits accepted by server: 15325 Commits sent from Server to Client: 34636

\*NOTE: DirtyDB WILL have severly slow startup times after 1M rows. To simulate this I created 1M rows and ran the test again, this was the result.

Firstly how to make dirty even dirtier.. \[bash\] # get the current size wc -l var/dirty.db

\# do until wc -l shows ~1M cat var/dirty.db{,} | sponge var/dirty.db \[/bash\]

**DirtyDB 1M Rows** Clients Connected: 308 Authors Connected: 77 Lurkers Connected: 231 Sent Append messages: 15108 Commits accepted by server: 15007 Commits sent from Server to Client: 33238

## Summary

Well I must say I did expect database choice to have an impact on editor performance but it doesn't look that way under the tests I performed.. I'm going to go back to the drawing board to find a test that will should help us decide once and for all which is the most performant database for Etherpad!

My thought for a new test is:

1) Remove all Lurkers, they are just putting load on the test app and it's the test app that's maxing out, not the server.

2) Send messages more frequently (See 1 but also go beyond normal human rates of contribution)

## Update...

Since I did the original tests I modified the load test tool to create authors only, here are the results...

**Redis Authors only** Clients Connected: 180 Authors Connected: 180 Sent Append messages: 20553 Commits accepted by server: 20452 Commits sent from Server to Client: 22866

**MySQL Authors only** Clients Connected: 184 Authors Connected: 184 Sent Append messages: 23045 Commits accepted by server: 22944 Commits sent from Server to Client: 20369

**DirtyDB Authors only** Clients Connected: 204 Authors Connected: 204 Sent Append messages: 28555 Commits accepted by server: 28454 Commits sent from Server to Client: 21565

**DirtyDB 1M+ rows Authors only** Clients Connected: 202 Authors Connected: 202 Sent Append messages: 26319 Commits accepted by server: 26218 Commits sent from Server to Client: 18200

## Conclusion #2

With these tests it seems that the database doesn't affect performance of heavy editor usage. My only assumption is that when the database gets large enough selects and puts will be slow enough to warrant a complex database. DirtyDB has obvious disadvantages of being unable to take home to your mother.
