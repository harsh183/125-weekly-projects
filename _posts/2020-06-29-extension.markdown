---
layout: post
title: Browser Extensions 
date: 2020-06-29
comments: true
external-url:
tag: JavaScript
toc: true
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

## Ethics

* [Techdirt - Facebook's Threat To NYU Researchers Is A Mistake, But It's The Inevitable Follow On To Overreaction To Cambridge Analytica](https://www.techdirt.com/articles/20201024/02131045571/facebooks-threat-to-nyu-researchers-is-mistake-inevitable-follow-to-overreaction-to-cambridge-analytica.shtml) - interesting article on the privacy and control over external browser extentions in a fight between NYU and Facebook.

## Commercial Impact of Open Source

At first FOSS (Free and Open Source Software) was starting out away and independent from companies and many of them like Microsoft were extremely against the idea of open source. However times have changed and now almost every major company is uses open source, and many large companies are also [contributors to open source software](https://www.forbes.com/sites/adrianbridgwater/2019/09/07/the-impact-of-the-tech-giants-on-open-source/?sh=30d5493bd277). Companies can often save money using open source software since they don't have to write as much software on their own, and there are often volunteers willing to maintain it the software. Having a large community reading the code and finding out bugs also leads to software that is more reliable and secure for businesses. Since FOSS lowers the cost for software, many companies now have a lower barrier to entry and this has lead to many new startups from developing countries that would not be possible a few decades ago.

## Ideas

* Is there something about your browser that could be done better? Maybe something that annoys you?

* Is there something you'd find convenient or nice to have in a browser? Find something that you have to do outside yo

* Could you come up with an extension idea that relates to something else you've learned in this class or other places?

## Requirements

* You should show it off in your README.md file, with animations/video and an explanation of the game.

* Has to use a Open Source license via a `LICENSE` file

Contributors: Harsh, Maaheen
