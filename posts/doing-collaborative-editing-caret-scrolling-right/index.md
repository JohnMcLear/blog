---
title: "Doing Collaborative editing viewport scrolling right"
date: 2013-03-18
categories: 
  - "etherpad"
tags: 
  - "collaborative"
  - "editing"
  - "editor"
  - "etherpad"
  - "ux"
---

Getting scrolling in an editor right is a complex task with various Gotchas. Getting scrolling right is in a collaborative editing environment is fraught with even more perils.   Most editors, both collaborative and non collaborative get scrolling wrong, yours probably does too.   But fear not! In this post I'm going to explain some edge case behaviours and how you should go about handling them.

I hold Wordpress in really high regard yet Wordpress as an example gets this very wrong(for example hitting page down in your editor will lose your caret if your document is greater than the height of your editor), TinyMCE is probably not to blame for this, WYSIWYG editors on the web in general are broken.

The behaviour for how editors scroll with documents has become a relatively normal experience. When you hit enter you expect to create a new line and for your browser to continue bringing that newline into your viewport.

When we talk about a viewport we mean something like this \[code\] -------------- | document | |----------------| | | | viewport | | | |----------------| | | -------------- \[/code\] As you can see the viewport shows a portion(or if the document is smaller than the viewport the whole) of the document and as a newline is created the viewport is moved down by the pixel height of the new line.  If you are a WYSIWYG or Etherpad user think of it as the large white panel where you can edit text.

So we know that moving the Viewport Offset Top to the right location on a document in a non collaborative environment is really easy, yet there are some behaviours we take for granted.

## Taken for granted

Using left arrow key moves the caret one position left until it hits the beginning of a row then it goes to the last position on the row above

Using the up/down arrows move our caret up, maintaining X(IE 5) position, when the caret hits the Viewpoint offset minus the Above line height the viewport is moved by minus the Above line height. Similar happens for the down arrow. If there is no line X content the caret X position is 0. 0 is not retained though, if the user presses up/down again the caret maintains it's original trajectory, IE 5

Using the page up/down arrows move our caret up to the first visible line in the viewport. Hitting page up again will take the current viewport height and move the first fully visible line in the new viewport position. Page down does similar.

Page up: \[code\] |----------------| | viewport | | | |----------------| | document | -------------- \[/code\]

Page down: \[code\] -------------- | document | | | |----------------| | | | viewport | | | |----------------| \[/code\] If your editor gets these wrong then you have serious problems.

## Gotchas

It's at this point that collaborative editing throws some gotchas in.

## Ever changing line heights above content

As you type this happens.. State a: \[code\] -------------- | document | | | |----------------| | | | viewport | | | |----------------| \[/code\] State b: \[code\] -------------- | document | | | | | |----------------| | | | viewport | | | |----------------| \[/code\] As you can see here another user has edited the content above our viewport which has left our viewport moved further down the document. This isn't the default behaviour with collaborative editors, you will have to deal with this edge case specifically.

The same problem exists if content is resized/removed above your content, again knowing the caret position at modification is how we solve this however there is another gotcha..

## The author is reading

So your author is reading content 5 lines above your current caret position and someone adds new content at the top of the document, you will not want to move the users caret position to the new location. I call this problem the "viewport war" problem.

### How we solve this problem

Part 1: Is the caret in viewport range at all(If not we can assume the user is reading text elsewhere in the pad so don't need to do anything)?

Part 2: If a new change above would modify the viewport to the point where the caret would no longer be visible for the user then always put the Offset Top at Caret Offset Top - (ViewPort height / 2). This means that the Caret is in the middle of the Y portion of the Viewport.

## Highlighting

During highlight we should never allow the viewport to be moved by an edit event, only the user should be able to change it however this poses a new problem.. Imagine we are highlighting lines 5 to 10 and someone deletes lines 0, our editor would now look something like this..

\[code\] |----------------| | |------------| | | | document | | | | | | |-| |-| |-|------------|-|

\[/code\] Note the line above the document, the document is now below the top of our viewport.

### How we solve this problem

This is another issue you will have to deal with in your editor. The best way is to basically stop the viewport moving if the content is being highlighted, this means that you allow the document (note we say document and not viewport) Offset Top to actually be greater than 0.

## So to summarize

\* Don't allow edits above the viewport to move the viewport out of the visible caret location unless the caret is already outside the visible caret location. \* Don't allow user changes to move viewport when author is highlighting

Anyway I wrote this so I can refactor the caret and viewport in [Etherpad](http://etherpad.org), a free and open source really-real time collaborative editor.
