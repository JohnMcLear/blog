---
title: "Getting author ownership right in a collaborative editor"
date: 2013-04-06
categories: 
  - "etherpad"
tags: 
  - "authorship"
  - "collaborative"
  - "editing"
  - "editor"
  - "etherpad"
  - "ownership"
---

In this blog post I'm going to explain the complexities of getting content ownership in a document right. All popular collaborative editors get this wrong, some more drastically than others.

Knowing who owns a certain piece of text in a document is an extremely important part of a collaborative editor, I will explain why later in the post.

Let's start with a basic example.

John writes. \[code\] My dog ate the tree \[/code\]

Now Dave swaps the words tree and dog around. We get

\[code\] My tree ate the dog \[/code\]

The actual sentiment of the sentence has changed a lot but that wasn't John's intention yet if we look at the sentence in all collaborative Editors there is no representation that Dave modified the text.

As you can imagine this is a huge problem as far as sentiment analysis, [Etherpad suffers from this](https://github.com/ether/etherpad-lite/issues/1696) too. Sentiment is distorted without the viewer being aware, imagine now we are working on a legal document and we replace the word tree and dog with friend and zombie...

As text is modified in Etherpad new attributes IE underline/bold/strikethrough aren't made clear to the viewer. IE if John writes \[code\] Hello world \[/code\]

Then Dave applies a strikethrough on this text we have no recollection that Dave made this modification. The viewer is under the impression that John struck this this piece of text, this is misleading.

Undo also falls into the trap of modifying someone elses text without it being clear, the same applies as the basic example, sentiment can be modified without the original Authors consent.

## So what's the solution?

### Boldly going..

At current each piece of text in Etherpad has an author owner, I propose that on attribute modification (IE bold/strikethrough) additionally each additional author exists in an "editors" array. The original author would still be listed as the "creator/author".

### To the replicator..

In the "tree ate the dog" example the original author(John) should still be maintained but additionally(this is the new bit) the editor(Dave) should be added to the "editors" array. Part of Etherpad's design is that as text is Copy/Pasted the original Author is maintained, this is healthy and by adding the editors array we should be able to identify that Dave has modified John's content.

### Undoing the deed

John might delete Dave's text then hit Undo but then we have to decide if the undone text is owned by Dave, John or if it's owned by Dave with a modification from John. Again adding Dave as an editor of the content would make it clear that a second author has modified the content.
