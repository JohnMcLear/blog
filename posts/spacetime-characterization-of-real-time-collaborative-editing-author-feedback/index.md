---
title: "Spacetime Characterization of Real-Time Collaborative Editing author feedback"
date: 2020-06-13
---

This is feedback for the authors of the paper on "[Spacetime Characterization of Real-Time Collaborative Editing](https://github.com/ether/RTCE/blob/master/paper/cscw-2018-rtce.pdf)". It is an excellent paper full of useful insight for [Etherpad](https://etherpad.org).

I'm writing this as an author and maintainer of Etherpad, which for this study was primarily used for providing the data used in the analysis.

I have some suggestions for future research/development of the project with a goal to help improve Etherpad and other RTCE.

I improved the documentation and bugfix the RTCE Analysis and my efforts on this are available on the [Etherpad Foundation RTCE Github Repository.](https://github.com/ether/RTCE)

## Simulate data to validate analysis.

Spacetime data could be simulated to ensure analysis is accurate.

Suggestion: Generate space-time edits with known values. [etherpad-loadtest](https://github.com/ether/etherpad-load-test) could do this with just a few hours work probably.

## Programming complexity

A single programming language could be used to complete the task.

Suggestion: Rewrite analysis tasks in NodeJS using Etherpad's built in methods. This would be a few days work.

## Supplemental features

Analyzing RTCE along side other communication methods (IE Video conferencing within Etherpad) would be extremely useful. See [ep\_webrtc](https://github.com/ether/ep_webrtc), [ep\_author\_follow](https://github.com/ether/ep_author_follow), [ep\_comments\_page](https://www.npmjs.com/package/ep_comments_page) plugins for example..

Suggestion: Speak to WMF to discuss the potential of them rolling out Video chat for a trial period and do a side-by-side comparison to see if there is any difference in findings. This would be a few days prep work then a few months to gather data.

## Multiple sources of data.

Using a single source(WMF) for data is not ideal.

Suggestion: Analyze video.etherpad.com, 26LLC (online tutoring platform), WMF and FramaPads content.

## Database support

Only supporting a single database store(MySQL) is not ideal as some large instances use Postgres, Maria, Redis etc.

Suggestion: Use Etherpad internals to generate data allowing for analysis of a much larger set of Etherpad instances.

## Conclusion

The goal of RTCE software is to **reduce** the amount of changesets and as such complimentary tools are included as they are often computationally cheaper than editing the pad; some examples are; Chat, Video Chat, Voice Chat and Comments(with suggestions) functionality.

Changesets or RTCE edits are relatively computationally expensive compared to a user doing peer to peer video chat, we want to minimize them **so the measurement of success for Etherpad is reducing changesets to complete a document**, which is contrary to this paper and may be somewhat surprising to the authors!
