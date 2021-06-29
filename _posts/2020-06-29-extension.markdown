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

To first learn `TypeScript`, we'll start from `JavaScript`. This is the langauge of the web and it was created with the purpose of scripting browsers _directly_. Learned well, `js` is an incredibly powerful tool you can do a lot with. Especially in an era where almost every application we use is a website.

```js
console.log("Hello Web Browser Extentions");
```

Hosted by: Harsh Deep

## Motivation

Comic: [CHRIS HADFIELD: An astronaut’s advice](http://www.zenpencils.com/comic/106-chris-hadfield-an-astronauts-advice/)

## Workshop

The goal of this workshop is to improve the [courses.illinois.edu](https://courses.illinois.edu) course explorer website by adding on our own functionality. This is a common use case for browser extentions where we create:

* ability to directly search a course in the top bar (currently we can type major but not number)

* automatically creating a google maps link for class locations

### Setup

1. I'm assuming Chrome but all this should work on Firefox or any other browsers. In any case, make sure you have a modern updated web browser installed. If you can read this article... you're good.

2. Get a user script manager, these let you add javascript onto certain pages and we'll use this to prototype first. If you're only making something for yourself or a few friends, this is likely all you need. For Firefox/Chrome a good choice is [TamperMonkey](https://chrome.google.com/webstore/detail/tampermonkey/dhdgffkkebhmkfjojejmpbldmpobfkfo/related?hl=en). 

3. Learn a bit of JavaScript. I'll explain as I go along, but having a little idea of the syntax will help. Check out [JavaScript in 14 minutes](https://jgthms.com/javascript-in-14-minutes/).

### Start Tamper Monkey 

First, Click the icon on the top of your browser to open the menu. Then, select "Create new script" and you should get an editor in a new tab with a starter template.

Fill in the top information similar to this. This is the metadata used by tampermonkey to understand details about the script and when to call it.

```js
// ==UserScript==
// @name         UIUC Course Explorer
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  Improve the course site
// @author       You
// @match        https://courses.illinois.edu/*
// @icon         https://www.google.com/s2/favicons?domain=tampermonkey.net
// @grant        none
// ==/UserScript==
```

Don't worry too much about these but the important two are `@match` which says match all URLs that start with `https://courses.illinois.edu` and `*` is a wildcard character that says this part can be anything. `@grant` means that grant no special permissions will be required to run the script. Check out their [documentation](https://www.tampermonkey.net/documentation.php) if you want to learn more about these options. 

### Approach

Similar to when we were writing Python bots, the broad approach is the same.

1. Identify Pattern - for this we'll inspect element around the page till we can find some common aspects (generally looking for elements, classes, ids)

2. Code Pattern - this is where BeautifulSoup comes in. We figure out how to pattern match what we need.

3. Action. Sometimes we're clicking buttons, filling forms, or performing more sub-extraction. 

### Direct Course Search

The approach we'll take is creating our own custom action to run after the form is submitted.

#### Event Listener

If we poke around the html we find the form's id is `subjectAutoJump-form`.

JavaScript let's us do this using a concept called event listeners. In many types of UI development, the flow of the code is managed by `events` that are triggered when some action happens. Events can be related to page loads, when an element is clicked, when a form is submitted, and many more. We can attach a piece of code called a `callback` which is a function that will run every time the event happens. 

In this case, we attach an event listener using `addEventListener`:

```js
// ==UserScript==
// @name         UIUC Course Explorer
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  Improve the course site
// @author       You
// @match        https://courses.illinois.edu/*
// @icon         https://www.google.com/s2/favicons?domain=tampermonkey.net
// @grant        none
// ==/UserScript==

const searchForm = document.getElementById("subjectAutoJump-form");
searchForm.addEventListener("submit", (event) => {
    console.log("Got a submit henlo");
});
```

but when we run this, we get a problem. Even after the console message message it still does the old action. To prevent this we do `event.preventDefault()` which stops the normal action from happening.

```js
searchForm.addEventListener("submit", (event) => {
    console.log("Got a submit henlo");
    event.preventDefault();
});
```

#### Content Parsing

Likewise, when we poke around the inspect element, we get the search box's id as `subjectAutoJump`. We use `.value` to get it's content. Let's try it out

```js
const searchForm = document.getElementById("subjectAutoJump-form");
searchForm.addEventListener("submit", (event) => {
    console.log("Got a submit henlo");
    const searchBox = document.getElementById("subjectAutoJump");
    const searchText = searchBox.value;
    console.log(searchText);

    event.preventDefault();
});
```

Now if we save it and try putting a few things in the search box, we should get something like this:

```js
Got a submit henlo
cs 125
Got a submit henlo
cs125
```

Now let's split it up. Here we notice that there may or may not be a space at all times, so just a simple split may not do. Instead, we look for a number. For this, we use `regex` which is a syntax to describe patterns in strings. Regex is a complex topic (more in CS 374 and CS 421) but all we're going to do is look for digits from `0-9` of any length. Once we have this, we can use `split` to get the part before and `match` to get the part matching.

```js
function getCourseInfo(searchText) {
    const regexNumbers = /[0-9]+/
    const name = searchText.split(regexNumbers)[0].toUpperCase().trim();
    const possibleNumbers = searchText.match(regexNumbers);
    let number = null;
    if (possibleNumbers !== null) {
        number = possibleNumbers[0].trim();
    }
    return [name, number];
}
```

#### Setting up the behavior 

We've also set it up to give `null` if we don't find a number. Having this `null` case let's us figure out when we want to not run our own function but to just let the old default behavior happen. For this we do:

```js
searchForm.addEventListener("submit", (event) => {
    console.log("Got a submit henlo");
    const searchBox = document.getElementById("subjectAutoJump");
    const searchText = searchBox.value;
    console.log(searchText);

    const [name, number] = getCourseInfo(searchText);
    console.log(`${name}-${number}`);

    if (number == null) {
        return;
    }
    event.preventDefault();
});
```

Now to have our browser go to a new link, we just set `window.location.href` to the new value. If we poke around the code we can see that the base url for all courses are `https://courses.illinois.edu/schedule/DEFAULT/DEFAULT/` and then the subject and number are seperated by a slash. If we put this into code:

```js
const newURL = `https://courses.illinois.edu/schedule/DEFAULT/DEFAULT/${name}/${number}`;
window.location.href = newURL;
```

At this point everything should work and your code so far should be:

```js
// ==UserScript==
// @name         UIUC Course Explorer
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  Improve the course site
// @author       You
// @match        https://courses.illinois.edu/*
// @icon         https://www.google.com/s2/favicons?domain=tampermonkey.net
// @grant        none
// ==/UserScript==

function getCourseInfo(searchText) {
    const regexNumbers = /[0-9]+/
    const name = searchText.split(regexNumbers)[0].toUpperCase().trim();
    const possibleNumbers = searchText.match(regexNumbers);
    let number = null;
    if (possibleNumbers !== null) {
        number = possibleNumbers[0].trim();
    }
    return [name, number];
}

const searchForm = document.getElementById("subjectAutoJump-form");
searchForm.addEventListener("submit", (event) => {
    console.log("Got a submit henlo");
    const searchBox = document.getElementById("subjectAutoJump");
    const searchText = searchBox.value;
    console.log(searchText);

    const [name, number] = getCourseInfo(searchText);
    console.log(`${name}-${number}`);

    if (number == null) {
        return;
    }

    const newURL = `https://courses.illinois.edu/schedule/DEFAULT/DEFAULT/${name}/${number}`;
    window.location.href = newURL;
    event.preventDefault();
});
```

#### Exercise

Add a third term `Fall/Summer/Spring/Winter` to find a course's term as well. For this you can allow people to put in more stuff after a number and figure out the URL pattern for that.

### Part 2 Linking the location displays to Google Maps

```js
function addLocations(rows) {
    if (rows.length === 0) {
        return;
    }

    const rowArr = Array.from(rows);
    const infoRows = rowArr.filter(row => row.id.startsWith("uid"));
    infoRows.forEach((infoRow) => {
        const locationElement = infoRow.getElementsByClassName("app-meeting")[4];
        const locationText = locationElement.textContent;
        const mapsLink = encodeURI(`https://www.google.com/maps/search/${locationText}+UIUC+USA`);
        locationElement.innerHTML = `<a href="${mapsLink}" target="_blank">${locationText}</a>`;
    });
}
const rows = document.getElementsByTagName("tr");
addLocations(rows);
```

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

#### Exercise

Add some if condition to make sure we only create map urls for valid addresses (multiple approaches are possible)

### Converting to a web browser extention

What we made above is called a _userscript_, this is a special type of JavaScript file that is designed to be run by a user. If you only want to make a browser extention for yourself or friends, TamperMonkey/GreaseMonkey/ViolentMonkey. However, if we want to put it up on stores and share it with others, we just have to package it right.

Create a folder on your computer and copy over our _userscript_ as `content.js` inside it. After that we need to create a `manifest.json` file with the right instructions. The exact instructions may vary based on browser, but for Chrome our file will look like:

```js
{
    "manifest_version": 2,
    "name": "UIUC Course Explorer++",
    "version": "0.1",
     "browser_action": {
     },
    "content_scripts": [
      {
        "matches": [
          "https://courses.illinois.edu/*"
        ],
        "js": ["content.js"]
      }
    ]
  }
```

Now open `chrome://extensions` on the browser and turn on Developer Mode. "Load Unpacked" will let you pick the folder for your extension and install what we just made. After this we can disable our TamperMonkey script to check if it worked.

## Publishing

This part is optional, but if you want to publish it on the store:

* [Firefox guide](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Your_first_WebExtension), [Firefox guide 2](https://extensionworkshop.com/documentation/publish/submitting-an-add-on/)

* [Chrome guide](https://developer.chrome.com/docs/webstore/publish/)

If you're going to publish make sure your code is good and versioned well. It's a really cool flex to show that you created a real browser extension! 

## Learn more

* TamperMonkey - [documentation](https://www.tampermonkey.net/documentation.php)

* Event Listeners - [addEventListener](https://www.w3schools.com/jsref/met_element_addeventlistener.asp) and [long list of HTML events](https://www.w3schools.com/jsref/dom_obj_event.asp).

* JS DOM Selectors - [intro tutorial](https://www.tutorialrepublic.com/javascript-tutorial/javascript-dom-selectors.php). DOM stands for Docment Object Model which represents the html tree for the file we were messing with.

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
