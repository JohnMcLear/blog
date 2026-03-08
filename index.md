---
layout: default
title: John McLear's Musings
---

Hacker, Maker, Ex-Ginger

---

- [Contact Me](/contact-me/)
- [Privacy Policy](/privacy/)
- [My Sites](/sites/)
- [Acknowledgements](/thanks/)
- [RSS Feed](/feed.xml)

---

## Latest Posts
{% assign posts = site.pages | where_exp: "item", "item.url contains '/posts/'" | sort: "date" | reverse %}
{% for post in posts %}
- [{{ post.date | date: "%Y-%m-%d" }} - {{ post.title }}]({{ post.url }}){% if site.data.broken_posts.broken contains post.url %} \[broken\]{% endif %}
{% endfor %}
