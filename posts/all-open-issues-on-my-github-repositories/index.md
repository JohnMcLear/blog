---
title: "All open issues on my github repositories"
date: 2014-03-13
categories: 
  - "git"
---

I wrote a quick little script that turns all my open github issues onto clickable links..

Copy paste the below into githubIssues.js:

\[code\] // Edit me var username = "YOURUSERNAME"; var password = "YOURPASSWORD"; // stop Editing!

var gittub = require("node-github"); var github = new gittub({version: "3.0.0"});

github.authenticate({ type: "basic", username: username, password: password });

github.issues.getAll({ user: "JohnMcLear", filter: "subscribed", per\_page: 100, sort: "created", direction: "asc" }, function(err, res) { for(var issueKey in res){ var issue = res\[issueKey\]; var line = "<p class='issue'>"; line += issue.created\_at + " "; if(issue.repository) line += issue.repository.full\_name + " "; line += "<a target='\_blank' href='"+issue.html\_url+"'>"; line += issue.title+"</a>"; line += "</p>"; if(issue.title) console.log(line); } }); \[/code\]

Edit your username and password then type:

\[code\]npm install node-github\[/code\]

then:

\[code\]node githubIssues.js &gt; issues.html\[/code\]

Open issues.html in your web browser..

Limitations: Max 100 issues due to Github API limit.
