---
layout: post
title: Web Browser Extension 
date: 2020-06-29
comments: true
external-url:
categories: TypeScript
---

<!-- markdownlint-disable MD004 MD009 MD014 MD024 MD040 -->

Web Browsers are probably the application we use the most, yet it's not always the best experience. What if we could improve it?

To first learn `TypeScript` we start from `JavaScript`.

```js
console.log("Hello Web Browser Extentions");
```

Hosted by: Harsh Deep

## Motivation

Comic: [CHRIS HADFIELD: An astronaut’s advice](http://www.zenpencils.com/comic/106-chris-hadfield-an-astronauts-advice/)

## Workshop

### Part 1 Direct Course Search

* [Direct Course Search](https://gist.github.com/harsh183/4505b4870fb9a003abe5193e0f7b9c71) - just do this but simpler (string strip and then substring)

* Exercise: be able to add a third term `fall/summer/winter` to get which term as well

### Part 2 Linking the location displays to Google Maps

* We get the rows `const rows = document.getElementsByTagName("tr");`

* We filter the rows to just get the info rows we want seeing that the starting is from `uid` leading to

  ```js
  rowArr = Array.from(rows);
  infoRows = rowArr.filter(row => row.id.startsWith("uid"));
  infoRows[3].getElementsByClassName("app-meeting")[4].textContent /
  ```

* We look at the Google Maps API [documentation](https://developers.google.com/maps/documentation/urls/get-started#search-action) to get the pattern `https://www.google.com/maps/search/?api=1&query=WHAT_WE_WANT`

* We generate a url like "https://www.google.com/maps/search/3039+Campus+Instructional+Facility+UIUC+USA", now lets create a function to do this

* use `.innerHTML` like

  ```js
  infoRows[3].getElementsByClassName("app-meeting")[4].innerHTML = `<a target="blank" href="${"https://www.google.com/maps/search/3039+Campus+Instructional+Facility+UIUC+USA"}">${p}</a>`
  ```

* Exercise: add some if condition to make sure we only create map urls for valid addresses (multiple approaches possible)

## Converting to a web browser extention

This part is optional but if you want to publish it on the store.

* Firefox guide

* Chrome guide

## Learn more

## Ideas

## Requirements

* You should show it off in your README.md file, with animations/video and an explanation of the game.

* Has to use a Open Source license via a `LICENSE` file
