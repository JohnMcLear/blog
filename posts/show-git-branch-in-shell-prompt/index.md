---
title: "Show git branch in shell prompt"
date: 2012-03-28
---

nano ~/.bashrc Paste in: \[bash\] function parse\_git\_branch\_and\_add\_brackets { git branch --no-color 2> /dev/null | sed -e '/^\[^\*\]/d' -e 's/\* \\(.\*\\)/\\ \\\[\\1\\\]/' } PS1="\\h:\\W \\u\\\[\\033\[0;32m\\\]\\$(parse\_git\_branch\_and\_add\_brackets) \\\[\\033\[0m\\\]\\$ " \[/bash\] Save. You will probably need to log out and back in to see this.
