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

A lot of thought went into how this initiative came up, and here are some of the reasons we did things and how we went about doing it. It's a cool read to understand how things work behind the scenes and can act as a resource to help others set up similar things. This initiative might seem simple, but a lot of thought went into all of this.

Feel free to reuse anything from here. You're welcome to reach out for specific advice as well. 

<!-- Markdown lint? Youtube? Zoom? Google Calendar? Outreach?  -->

## Structure 

We picked a schedule that repeats weekly. This was familiar for most students and allowed enough time to dive into a topic before moving on.

### Tuesday Live Session

We picked Tuesday every week to do sessions since it provided some level of sync structure and some amount of human interaction. It was at noon Chicago Time, mainly picked as a tradeoff between internship lunch breaks and timezones (mostly getting Chicago and Indian time synced).

### Wednesday Idea Form

At the end of Wednesday, people would send in a quick idea form of what they'd want to do. The idea was to an [MVP and sprinkles](https://peterlunch.com/how-to-plan-and-build-a-programming-project/) (interestingly, this blog post also inspired a lot of this summer initiative). This was about 1.5 days after the workshop to let people get an idea of the week's focus and think about the concept.

This part was mainly to give people a starting point to work from and pick a scope that's doable quickly. This also allowed us to provide some feedback about the idea and their scoping, plus general encouragement.

### Monday Project Submission 

We picked Monday next week since it gave people the weekend and some time after that to complete their project, with wiggle room for people's varied schedules. This also avoids having the due date on Sunday, as that is when most things are due and can get quite annoying. People could either send their project privately or post it on the forum for everyone. In each case, all projects got detailed feedback (~200+ words) on their strengths and weaknesses in terms of features, code quality, and documentation.

### Overall Length

We set it at eight weeks with four weeks per language. We figured a month is enough time for a language, and four projects each give quite a substantial exposure. In hindsight, it's clear that this was a pretty long time, especially during the summer, and momentum reduced. Future iterations may take shorter lengths and focus on just one language.

### Requirement to be Open Source

Inspired by UIUC's [Hack Illinois 2019](https://2019.hackillinois.org/), we decided to add a requirement to make all things open source. Many people did not even realize what Licenses were and why they were necessary at first, so this taught the students more about open source. We linked around six articles at the bottom of the workshop pages explaining various aspects of the open source world. This wasn't the most significant goal, but it was nice to see a mix of licenses used by projects and forum discussions trying to understand what these licenses implied.

## Topic List 

We picked the topics based on:

* What we were familiar with - this allowed us to reuse old materials and links we'd saved, and we'd have more knowledge to answering questions
* Good programming library/API support - we had to be able to make something attractive looking within an hour so that a small amount of time was enough to produce an exciting project 
* Low entry barriers - the target audience was students who had _only_ finished some level of introductory computer science
* Excitement/flashy factor - we wanted to make things that had novelty and pizzazz, like chatbots and browser extensions
* Usefulness - what people learned could be used to make lots of practical projects, since many students don't realize they already have the skills to make something useful
* Something we wanted to learn more about - teaching is the best way to learn
* Not too focused on subjects from core CS sequences - core CS classes are unlikely to cover how to make a chatbot or browser extension (for a good reason, though)
* Fun!

### Python

We picked Python because:

* The first year programming sequence at UIUC covered Java and C++ already - we wanted something new
* It's one of the most popular programming languages today for teaching and doing quick projects
* It's also heavily used in industry and academia for all kinds of use cases
* Python has firmly established itself as a jack of all trades language - this means students can use one language to combine all sorts of areas
* Succinct syntax with all sorts of syntax sugar (like list comprehensions), which is great for prototyping and learning quickly 
* Large set of packages available via `pip` allows students to build exciting things quickly

### JavaScript

Likewise JavaScript:

* Not covered in classes too much. There is a substantial amount of academic elitism against it too, but it's an instrumental language for creating projects linked to the web
* It's trendy today for all sorts of frontend and backend web-related use cases, but it's rapidly expanding outside that too
* Heavily used in industry 
* It's a good early exposure to concurrent and functional programming
* While it's not as terse as Python, it's still got many neat syntax aspects
* `npm` gives access to an extensive set of packages that let people build interesting things

We also considered putting in TypeScript, but it added more friction on starting and wasn't useful for prototype projects. However, it is pretty helpful as projects grow, so it was included in the links at the bottom of pages.

## Tools

We carefully considered which tools we wanted to cover during the program. We initially planned some tools, but later ended up not using them. We had to consider how useful each tool was for students, and what we should trim down to avoid overwhelming people with too much new information all at once.

### What we did 

* Version control via `git`. It's helpful for progress tracking, cloud sharing, and fixing screwups. It also allowed people to upload their projects on places like `Github` or `sr.ht`

* `pylint` and `eslint` - these style checkers are suitable for a lot of basic code smells and ensuring quality. We didn't strictly check if people were using them, but they were helpful to many people.

* `vscode` - it's a good editor that isn't as complex as many IDEs like Visual Studio or IntelliJ, but not as cutdown as text editors like `nano` or `vim`. It has pretty solid `python` and `js` tooling, and many students were likely to have it already.

* Interactive debuggers like python's built-in `breakpoint()` - people were familiar with `print` statement debugging, but showing people how to use interactive debuggers in interpreted languages is quite helpful and aids teaching stuff like web bots.

* Automated testing via `pytest` - students had seen automated testing in their classes before via assignments, and here we showed them it wasn't that hard to get started with just using `pytest` and built-in `asserts`. 

* Web API testing via Postman - when writing backend APIs, we showed people how to use Postman to figure out how APIs were being used and set up the ins and outs of the requests correctly. 

* Linux/Unix style command line - it's ubiquitous in modern development, yet many students didn't have much exposure to it yet. It also made for some exciting command line app-building later on. 

### What we considered but didn't do

* Text-based editors like `vim` - honestly cool to learn and does teach some good habits, but it can be intimidating for people and it's not critical to learn.

* Continous Integration/Deployment - this could have been useful for automatically checking style and test cases, but it has varying configuration and could take more time than it was worth for projects at this stage

* Automated Frontend/Backend `js` testing - while this was quite possible, doing this would take away time from focusing on the more challenging `js` content.

## Professional Workshops

We also hosted some soft skill sessions that classes didn't focus on but are very useful for students.

* Imposter Syndrome - It's rampant in Computer Science students, yet it's rarely mentioned in class. It's a surprisingly universal feeling, yet rarely acknowledged, and we wanted to shed some light on that.
* Exploring CS @ Illinois programs - Hearing from older students in various CS and CS + X majors at UIUC about their experiences navigating through college.
* Branding - Many students are excellent at technical skills and doing exciting projects but make basic mistakes while professionally presenting themselves on the internet. We wanted to give our set of tips and personalized feedback.

## Website 

We based our website on `jekyll` for a variety of reasons:

* Updating content was easy, so typos could be corrected and more information could be added as needed
* We didn't have to worry about styling and HTML while writing
* It gave us an excellent collaborative setup since it was just a collection of different text files, people just had to update their parts and `git` let us sync the rest
* `jekyll` has good code highlighting support, useful since we had a lot of code snippets. We also considered Medium, but it doesn't have that great support for this
* Allowed us to write in markdown, which many of us were familiar with, so we could hammer out content pretty quickly

### Template

Jekyll also gave us a lot of good choices with templates, we initially started with Huge Ferreia's [papyrus theme](https://github.com/hugoferreira/papyrus-theme), but we settled on Abhishek Nagekar's [Elementary](https://github.com/abhn/Elementary). We liked their:

* Multiple post type support - you can find a `_news` folder and `_posts` folder in the repo. This was a good fit for us because we had different types of pages for side posts and workshops.
* Light/dark switch - many people strongly prefer one or the other, and it has substantial accessibility benefits.
* Progress bar - we had pretty long pages, and a progress bar gave people a rough idea how far along a tutorial they were
* Lightweight site - many themes take a while to load and don't dedicate that much space to their content, while we wanted to focus on just that
* Tech-like style in fonts and overall styling
* Good tags support - improved the site's navigation

One issue we faced was that the syntax highlighting didn't always work well in dark mode for every language, so we forced many code snippets to be marked with \`\`\`js even though they were not. Another potential problem is that it's [no longer maintained](https://www.nagekar.com/2021/01/life-goes-full-circle-blog-back-to-wordpress.html), but we didn't find that to be much of an issue.

### Github

We hosted the site's repo on [Github](https://github.com/harsh183/125-weekly-projects) under the GPLv3 license. 

* The `README` had info on the entire initiative, and initially, this was the info post encouraging people to sign up on the interest form
* The Issue Tracker lets us track and split our to-do tasks pretty well. Each Issue could also contain checklists that was quite useful
* It was easy to add collaborators since everyone had Github accounts 
* We wanted something public so that people could see how we did things and learn from our workflow
* A lot of us had experience with GitHub

Each of the example code repos was also on Github under the MIT license. 

### Netlify Hosting and DNS

We picked [Netlify](https://www.netlify.com/)

* The free tier was adequate for our needs
* Their CDN allowed good response times to students all over the world 
* It is automatically connected with Github repositories making setup easier
* It set up a Continous Deployment hook with pushes on the `main` branch, so this made site updates quick since people had to just `git commit` then `git push`, and the site got updated automatically. On the GitHub web interface, if you saved something, the site immediately updated.
* It automatically took care of `jekyll` deployment. This let people contribute to the site without ever installing or having to understand how Jekyll worked. All they had to do was update markdown files, and things just _worked_.
* We had experience running things with Netlify

We also set up our DNS server with Netlify:

* It automatically set up with the domain quite nicely.
* Their interface was cleaner and much more usable than our domain host.
* It let us map records to the forum quite easily as well.

## Google Forms 

We used [Google forms](forms.google.com). This was convenient because it could:

* Collect results in a google drive folder - made management of about ~20 forms + data per project easier
* Output `csv` - good for automatic parsing 
* Link to excel sheets (Google Sheets) - let us split work when returning idea and project feedback by ticking off people as we finished (we colored the row green)
* Give simple aggregate statistics on questions - we asked a mix of objective and subjective questions, and the forms' interface had a decent view that let us know how things were going week to week
* The output fit into Mailchimp exports quite well - let us send specific emails around missing forms as well as those who were initially interested
* It was supported well by the UIUC system, so everyone was familiar with it, and it was easy to set up permissions for UIUC student accounts to allow access to the right data
* Cloning forms was quite easy, so each week, we'd just copy over the idea and project form and update the links

### What Forms Did We Send

* 1 initial interest form - to see if we had any traction and demand
* 7 idea and project submission forms - to create the course structure for people
* 1 start form - to understand what people were looking for and what people wanted

## Emails

We used [Mailchimp](https://mailchimp.com/) for sending out emails. We had a large crowd to send announcements and reminder emails to, which worked quite well for us. We also considered [Google Groups](https://support.google.com/a/answer/9400082?hl=en), but we found the setup too complicated, and the feature set is not a very strong fit. Mailchimp worked because:

* Their free tier gave us a lot
* It had good automatic import from Google Form output that let us generate lists quickly
* The filtering tools also let us send emails with criteria like "People who sent this week's project idea but did not send a submission who are in the general mailing list"
* It also had a unsubscribe option to let people opt-out easily

After a few weeks, we stopped sending reminder emails, but that's probably something we should do more strongly in the future.

For sending individual feedback on ideas and projects, we sent emails via UIUC email, which worked fine.

## Discourse 

For the forum where people could ask questions and show off their projects. Lots of courses at UIUC use Piazza, Compass, Campuswire, and many more, but we leaned towards [Discourse](https://www.discourse.org/) since:

* It was heavily used by UIUC CS 125, where all the staff had worked before. This also let us reuse part of the existing setup from there.
* Made by the people behind StackOverflow, it was oriented towards tech forums which gave nice syntax highlighting, search, and many more convenient functions
* It has a robust system for admins, and their settings/dashboard sections were quite feature-complete
* It was self-hostable

### Plugins

Discourse had a powerful set of plugins available too. Here is what we used:

* [discourse-canned-replies](https://github.com/discourse/discourse-canned-replies)
* [discourse-checklist](https://github.com/discourse/discourse-checklist)
* [discourse-footnote](https://github.com/discourse/discourse-footnote)
* [discourse-policy](https://github.com/discourse/discourse-policy)
* [discourse-solved](https://github.com/discourse/discourse-solved) - This was really useful since we could mark questions as solved. Once a project was given feedback we could also mark it as solved, which helped us filter which projects still needed feedback.
* [discourse-whos-online](https://github.com/discourse/discourse-whos-online)
* [docker_manager](https://github.com/discourse/docker_manager)
* [retort](https://github.com/gdpelican/retort) - Add Slack-like emoji reactions

## Project Code Hosting

We allowed any public site to share their projects with us, but _everyone_ picked GitHub. This was expected, but we thought maybe some people might use something hipster like [sr.ht](https://sr.ht/) or [Gitlab](https://about.gitlab.com/). Some of the reasons to use these were:

* Free hosting 
* Earlier exposure to how UIUC CS classes often have students submit assignments
* General popularity of the site
* Easy `LICENSE` setup (which was a requirement, as all projects had to be open source)
* Good web UI/UX
* Easy to clone repositories
* Often treated as a code portfolio by students these days (which was one of the goals for many students)
* The strong community aspect of GitHub

These advantages aren't exclusive to Github, but it seems that all these together make it pretty compelling, and most people seem pretty happy with GitHub.

Contributors: Harsh Deep, Monika Para, Maaheen Maajed
