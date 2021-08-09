---
layout: post
title: Decisions and Logistics
date: 2020-05-29
comments: true
external-url:
tag: Info
toc: true
---

<!-- markdownlint-disable MD004 MD009 MD014 MD024 MD031 MD040 -->

A lot of thought went into how this initiative came up, and here are some of the reasons why we did things, as well as how we went about doing it. It's a cool read to understand how things work behind the scenes, and can act as a resource helping people set up similar things. This might seem simple, but a lot of thought went into all of this.

Feel free to reuse any thing from here. You're welcome to reach out for specific advice as well. 

<!-- Markdown lint? Youtube? Zoom? Google Calendar? Outreach?  -->

## Structure 

We picked a schedule that repeats weekly. This was familiar for most students and allowed enough of a time to dive into another topic before moving on quickly.

### Tuesday Live Session

We picked Tuesday every week to do sessions since it provided some level of sync structure, as well as some amount of human interaction. It was at noon Chicago Time which was mostly picked as a tradeoff between internship lunch breaks and timezones (mostly getting Chicago and Indian time synced).

### Wednesday Idea Form

At the end of Wednesday, people would send in a quick idea form of what they'd want to do. The idea was to identify some [MVP and Sprinkles](https://peterlunch.com/how-to-plan-and-build-a-programming-project/) (interestingly this blog post also inspired a lot of this summer initiatve). This was about 1.5 days after the workshop to let people get an idea of what was the week's focus and do some thinking on the idea.

This part was mostly to give people a starting point for people to work from and pick a scope that's doable quickly. This also gave us an opportunity to give some feedback about the idea and their scoping, plus general encouragement.

### Monday Project Submission 

We picked Monday in the next week since it gave people the weekend as well as some time after that depending on their varied schedules. This also breaks up having Sunday due for most things which can get quite annoying. People could either send their project privately or post it on the forum for everyone. In each case, all projects got detailed feedback (~200+ words) on their strengths and weaknesses in terms of features, code quality and documentation.

### Overall Length

We set it at 8 weeks with 4 weeks per language. We figured a month is enough time for a language and 4 projects each gives quite a strong exposure. In hindsight it's clear that this is a pretty long time, especially during the summer and momentum definitely reduced. Future iterations may take shorter lengths and focus on just one language.

### Requirement to be Open Source

Inspired by UIUC's [Hack Illinois 2019](https://2019.hackillinois.org/), we decided to add a requirement to make all things open source. Many people did not even realize what Licenses were and why they were important at first, but this made everyone learn more about Open Source. We linked around six articles at the bottom of the workshop pages explaining various aspects of the Open Source world. This wasn't the biggest goal so it wasn't too important, but it was nice seeing a mix of licenses used by projects as well as forum discussions trying to understand what these licenses implied.

## Topic List 

We picked the topics based on:

* what we were familiar with - this allowed us to reuse old materials and links we'd saved, and we'd have a deeper knowledge while answering questions
* good programming library/api support - we had to be able to make something interesting looking within an hour, and a days effort could produce an intersting project 
* low entry barriers - the students had _only_ finished some level of introductory computer science
* excitement/flashy factor - we had to make things that had novelty like chat bots or browser extensions
* usefulness - what people learned could be used to make lots of practical topics since many students don't realize they already had the skills to make something useful
* something we wanted to learn more about - teaching is the best way to learn 
* not too focused on by core cs sequences - core cs classes are unlikely to cover how to make a chat bot or browser extension (for good reason though)
* fun

### Python

We picked Python because

* The first year programming sequence at UIUC covered Java and C++ already - we wanted something new
* It's one of the most popular programming languages today for teaching and making quick projects
* While it's also heavily used in industry and academia for all kinds of use cases
* Python has firmly established itself as a jack of all trades langauge - this means one langauge can be used to combine all sorts of areas
* Succint syntax with all sorts of syntax sugar like list comprehensions which is great for prototpying and learning quickly
* Large set of packages available via `pip` that can allow students to build interesting things quickly.

### JavaScript

Likewise JavaScript:

* Not covered in classes too much. There is a strong amount of academic elitism against it too, but it's a very useful langauge for creating projects linked to the web.
* It's very popular today for all sorts of frontend and backend web related use cases, but it's rapidly expanding outside that too.
* Heavily used in industry 
* It's a good early exposure to concurrent and functional programming.
* While it's not as terse as Python, it's still got many neat syntax aspects
* `npm` gives access to a very large set of packages that let people build interesting things.

We also considered putting in TypeScript, but it added on more friction on starting out and isn't too useful for prototype projects. It is quite useful as projects grow, so it was included in the bottom links.

## Tools

We carefully considered the tools we wanted to cover and not during the program. Some things we initially planned but later ended up not deciding on too. The tradeoffs were based on how useful is it for students to know, and trimming down things so that we don't overwhelm people at once.

### What we did 

* Version control via `git` - is pretty useful for progress tracking, cloud sharing and fixing screwups of side projects. It also allowed people to upload their projects on places like `Github` or `sr.ht`

* `pylint` and `eslint` - these style checkers are good for a lot of basic code smells and ensuring quality. We didn't strictly check if people were using them, but they were useful to many people.

* `vscode` - it's a good editor that isn't as complex as many IDEs like Visual Studio or IntelliJ, but not as cutdown as text editors like editors like `nano` or `vim`. It has pretty solid `python` and `js` tooling and many students were likely to already have it.

* Interactive debuggers like python's built in `breakpoint()` - people were familiar with `print` statement debugging, but showing people how to use interactive debuggers in interpreted languages is quite useful and aids teaching stuff like web bots.

* Automated testing via `pytest` - students had seen automated testing in their classes before via assignments, and here we showed them it wasn't that hard to get started with just using built in `asserts`. 

* Web API testing via Postman - when writing backend APIs, we showed people how to use postman to figure out how APIs were being used and how to set up the ins and outs of the requests correctly. 

* Linux/Unix style command line - it's really common in modern development, yet many students didn't have much of an exposure to it yet. It also made for some interesting command line app building later on. 

### What we considered, but didn't do

* Text based editors like `vim` - honestly cool to learn and does teach some habits, but it can be initmidating for people and not critical to learn

* Continous Integration/Deployment - this could have been useful for automatically checking style and test cases, but it's varying configuration and could take more time than it was worth for projects at this stage

* Automated Frontend/Backend `js` testing - while this was quite possible, doing this would take away time from focusing on the more challenging `js` content.

* TypeScript - it's very cool and combines the best of the Java/Haskell and JavaScript worlds, and has massive momentum today, but it was also not critical and distracted away from the frameworks we were focusing on.

## Professional Workshops

We also felt that there were a few soft skill sessions that classes didn't focus on but are very useful for students.

* Imposter Syndrome - It's extremely widespread in Computer Science students yet it's rarely mentioned in class. It's a surprisingly universal feeling, yet rarely acknowledged and we wanted to shed some light on that.
* Exploring CS @ Illinois programs - Hearing from older students in various CS and CS + X majors at UIUC about their experiences navigating through college.
* Branding - Many students here are excellent at technical skills and doing interesting projects, but make basic mistakes while presenting themselves on the internet professionally. We wanted to give our set of tips and personalized feedback.

## Website 

We based our website off `jekyll` since it let us

* quickly update content  - we wrote content right before workshops and let us fix typos quick
* not worry about styling and HTML while writing since it can be distracting
* gave us a good collaborative set up since it was just a collection of different text files, people just had to update their parts and `git` let us sync the rest
* having good code highlighting support since we had a lot of code snippets. We also considered Medium, but it doesn't really have that great support for this.
* allowed us to write in markdown which many of us were familiar with, and we could quickly hammer out content pretty quickly

### Template

Jekyll also gave us a lot of good choice with templates, we initially started with Huge Ferreia's [papyrus theme](https://github.com/hugoferreira/papyrus-theme) but we settled on Abhishek Nagekar's [Elementary](https://github.com/abhn/Elementary). We liked their

* multiple post type support - In the repo you can find a `_news` folder and `_posts` folder. This was a good fit for us because we had different types of pages for side posts as well as workshops.
* light/dark switch - Many people have a strong preference for either, and it does have strong accessibility benefits.
* progress bar - we had fairly long pages, and a progress bar gave people a rough idea how far along a tutorial they were
* lightweight site - many themes take a while to load, and don't dedicate that much space to their content while we wanted focus on just that
* looked pretty tech-like in fonts and overall styling
* had good tags support - improved the site's navigation

One issue we faced was that the syntax highlighting didn't always work well in dark mode for every language, so we forced a bunch of code snippets to be marked with \`\`\`js even though they were not. Another caveat is that it's [no longer maintained](https://www.nagekar.com/2021/01/life-goes-full-circle-blog-back-to-wordpress.html), but we didn't find that to be much of an issue.

### Github

We hosted the site's repo on [Github](https://github.com/harsh183/125-weekly-projects) under the GPLv3 license. 

* The `README` had info on the entire initiative, and initially this was the info post encouraging people to sign up on the interest form.
* The Issue tracker let us track and split our todo tasks pretty well. Each Issue could also contain checklists that was quite useful.
* It was easy to add collaborators since everyone had Github accounts. 
* We wanted something public so that people could see how we did things, and could learn from our workflow.
* A lot of us had past experience with GitHub.

Each of the example code repos were also on Github under the MIT license. 

### Netlify Hosting and DNS

We picked [Netlify](https://www.netlify.com/)

* The free tier was quite adquate
* Their CDN allowed good response times to students all over the world 
* It automatically connected with Github repositories making setup easier.
* It set up a Continous Deployment hook with pushes on the `main` branch, so this made site updates quick since people had to just `git commit` then `git push` and the site got updated automatically. On the GitHub web interface, if you saved something, the site immediately updated.
* It automatically took care of `jekyll` deployment. This let people contribute to the site without ever installing or having to understand how jekyll worked. All they had to do was update markdown files and things just _worked_.
* We had past experience running things with Netlify.

We also set up our DNS server with Netlify as well:

* It automatically set up with the domain quite nicely.
* Their interface was cleaner and much more usable than our domain host.
* It let us map records to the forum quite easily as well.

## Google Forms 

We used [Google forms](forms.google.com). This was convenient because it could:

* collect results in a google drive folder - made management of about ~20 forms+data easier
* output `csv` - good for automatic parsing 
* link to excel sheets (Google Sheets) - let us split work when returning idea and project feedback by ticking off people as we finished (we colored the row green)
* give simple aggregate statistics on questions. We asked a mixed of objective and subjective questions and the forms interface had a _decent_ view that let us know how things were going week to week
* the output also fit into mailchimp exports quite well - let us send specific emails around missing forms as well as those who were initially interested
* it was supported well by the UIUC system, so everyone was familiar with it and it was easy to set up permissions for UIUC student accounts to allow access to the right data
* cloning forms was quite easy, so each week we'd just copy over the idea and project form and update the links

### What Forms Did We Send

* 1 initial interest form - to see if we had any traction and demand
* 7 idea and project submission forms - to create the structure for people
* 1 start and end form - to understand what people were looking for and what people wanted

## Emails

We used [Mailchimp](https://mailchimp.com/) for sending out emails. We had a large crowd to send annoucements and reminder emails to, and it worked quite well for us. We also considered [Google Groups](https://support.google.com/a/answer/9400082?hl=en) but found the set up too be too complicated and the feature set not a very strong fit.

* Their free tier gave us a lot
* It had good automatic import from Google Form output that let us generate lists quickly
* The filtering tools also let us send emails with criteria like "People who sent this week's project idea but did not send a submission who are in the general mailing list"
* It also had a unsubscribe option to let people opt out easily.

After a few weeks, we stopped sending reminder emails, but in the future that's probably something we should do more strongly.

For sending individual feedback on ideas and projects, we just sent emails via UIUC email which worked fine.

## Discourse 

For the forum where people could ask questions and show off their projects. Lots of courses at UIUC use Piazza, Compass, Campuswire and many more, but we leaned towards [Discourse](https://www.discourse.org/) since

* it was heavily used by UIUC CS 125 where all the staff had worked for many semesters. This also let us reuse part of the existing setup from there.
* made by the people behind Stack Overflow, it was oriented towards tech forums which gave nice sytax highlighting, search and many more convinient functions.
* it has a powerful system for admins and their settings/dashboard sections were quite feature complete
* it was self hostable

### Plugins

Discourse had a powerful set of plugins available too. Here is what we used:

* [discourse-canned-replies](https://github.com/discourse/discourse-canned-replies)
* [discourse-checklist](https://github.com/discourse/discourse-checklist)
* [discourse-footnote](https://github.com/discourse/discourse-footnote)
* [discourse-policy](https://github.com/discourse/discourse-policy)
* [discourse-solved](https://github.com/discourse/discourse-solved) - This was really useful since we could mark questions as solved. Once a project was given feedback we could also mark it as solved which helped us filter what projects still needed feedback.
* [discourse-whos-online](https://github.com/discourse/discourse-whos-online)
* [docker_manager](https://github.com/discourse/docker_manager)
* [retort](https://github.com/gdpelican/retort) - Add slack like emoji reactions

## Project Code Hosting

For sharing their projects with us, we allowed any public site, but _everyone_ picked GitHub. This was expected but we thought maybe some people might use something hipster like [sr.ht](https://sr.ht/) or [Gitlab](https://about.gitlab.com/). The reasons were along the lines of:

* Free hosting 
* Earlier exposure in classes to submit assignments
* General popularity of the site
* Easy `LICENSE` setup (which was a requirement for all projects to be open source)
* Good Web UI/UX
* Easy to clone 
* Often treated as a code portfolio by students these days (which was one of the goals for many students)
* Strong community aspect of GitHub

These advantages aren't exclusive to Github, but it seems that all these together make it pretty compelling and most people seem pretty happy with GitHub.

Contributors: Harsh Deep, Monika Para
