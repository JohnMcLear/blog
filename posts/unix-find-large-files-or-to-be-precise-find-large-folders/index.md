---
title: "Unix find large files | find large folders"
date: 2011-05-17
categories: 
  - "debian"
  - "developing"
  - "ict"
---

Thanks to [Mark](http://blog.markftw.com) for reminding me about these, I claim no credit for these, I just use them.



```
find . -type f -size +100000k -exec ls -lh {} \\; | awk '{ print $8 ": " $5 }'
```





```
du --max-depth=1 -h
```


