---
layout: post
title: Browser Extensions 
date: 2020-06-29
comments: true
external-url:
tag: JavaScript
---

<!-- markdownlint-disable MD004 MD009 MD014 MD024 MD040 -->

Web browsers are among the applications we use the most, but they're not always the best experience. What if we could improve them?

To first learn `TypeScript`, we'll start from `JavaScript`.

```js
console.log("Hello Web Browser Extentions");
```

Hosted by: Harsh Deep

## Motivation

Comic: [CHRIS HADFIELD: An astronaut’s advice](http://www.zenpencils.com/comic/106-chris-hadfield-an-astronauts-advice/)

## Workshop

### Part 1 Direct Course Search

* [Direct Course Search](https://gist.github.com/harsh183/4505b4870fb9a003abe5193e0f7b9c71) - do this, but simpler (string strip and then substring)

* Exercise: add a third term `Fall/Summer/Winter` to find a course's term as well

### Part 2 Linking the location displays to Google Maps

* We retrieve the rows through `const rows = document.getElementsByTagName("tr");`

* We can filter the rows to just get the info rows that we want, seeing that the start is from `uid` leading to

  ```js
  rowArr = Array.from(rows);
  infoRows = rowArr.filter(row => row.id.startsWith("uid"));
  infoRows[3].getElementsByClassName("app-meeting")[4].textContent /
  ```

* We look at the Google Maps API [documentation](https://developers.google.com/maps/documentation/urls/get-started#search-action) to get the pattern `https://www.google.com/maps/search/?api=1&query=WHAT_WE_WANT`

* We generate a url like "https://www.google.com/maps/search/3039+Campus+Instructional+Facility+UIUC+USA". Now, let's create a function to do this.

* use `.innerHTML` like

  ```js
  infoRows[3].getElementsByClassName("app-meeting")[4].innerHTML = `<a target="blank" href="${"https://www.google.com/maps/search/3039+Campus+Instructional+Facility+UIUC+USA"}">${p}</a>`
  ```

* Exercise: add some if condition to make sure we only create map urls for valid addresses (multiple approaches are possible)

## Converting to a web browser extention

This part is optional, but if you want to publish it on the store:

* [Firefox guide](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Your_first_WebExtension), [Firefox guide 2](https://extensionworkshop.com/documentation/publish/submitting-an-add-on/)

* [Chrome guide](https://developer.chrome.com/docs/webstore/publish/)

## Learn more

## Ideas

* Is there something about your browser that could be done better? Maybe something that annoys you?

* Is there something you'd find convenient or nice to have in a browser? For example, maybe a schedule, or a built-in alarm? 
<!-- maybe remove this, if it'll lead to too many people doing exactly those things -->

* Could you come up with an extension idea that relates to something else you've learned in this class or other places?

## Requirements

* You should show it off in your README.md file, with animations/video and an explanation of the game.

* Has to use a Open Source license via a `LICENSE` file

Contributors: Harsh, Maaheen
