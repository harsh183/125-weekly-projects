---
layout: post
title: Debugging 
date: 2020-05-29
comments: true
external-url:
tag: Tools
toc: true
---

<!-- markdownlint-disable MD004 MD009 MD014 MD024 MD031 MD040 -->

## Why debugging is important

- Usually, we want to debug when we expect our code to act in some way but it acts in a different way instead.
  - Author's Note: This article is still a work in progress, but I wanted to get this up before June 1st, so hopefully this could be of help. I am hoping to expand on the topics written.

## How to use print statements to debug

- The most common way to debug is to use print statements to debug. I recommend using print statements on your variables and methods to produce what you expect them to produce. For example, if there is a for loop that depends on a variable, print out the variable inside the for loop and outside the for loop.

## Using `breakpoint()`  to figure out your next lines of code

- Type ` breakpoint() ` in your code. Then, run your python file. This opens up a console in which you can do things. The console says ` (Pdb) ` at the beginning of each line which stands for Python debugger. In the console, you can test out lines of code. A great way to do this is in web bots to test different lines of code.
- A good example of using `breakpoint()` can be found in the web bot workshop here [CS125 Wacky Web Bots - YouTube](https://youtu.be/07YsSpcDjHI?t=2293) <!-- Could we link a video that has -->

## Use the Interactive Window to develop Python Scripts

- On VSCode, go to the side buttons and click on the sixth button (the button with 4 squares). This is the marketplace where you can download extensions to improve your VSCode experience. Download the Extension named Python. This extension let's you use the interactive window to develop Python Scripts. This is a good way to test short scripts to see if they would run. You can use VSCode in the same way that people normally use Jupyter Notebook.
- You can create cells on a Python file by typing "#%%"
- Use "Shift + Enter " to run a cell, the output will be shown in the interactive window
- If you click on the shell itself, you can also choose options such as "Run Cell", "Run Below" and "Debug Cell". In the picture below, the first cell runs and works. The second cell doesn't work because print is spelled incorrectly.
- ![vscode window](https://remnote-user-data.s3.amazonaws.com/JbQektfjKlrvn-Hk4h_LnGN8WYArjMWGq_Mxdpcoi5dylv0PEOxzimppv-343i4Ds1HeSqWZYtOMbC6PlQ8SnzOTD7zBruELx2UF71_fJxjRqtHNXpW0BqwIYv1PE7MW.png)

## Using the debugger to test your code

- A great way to go about seeing why your code isn't doing what you want it to do is to test your code. Let's use that in conjunction with the debugger.

- The below code works but doesn't produce the result we want. We have a function named `order` that takes in 3 values. We use the function `main` to test the code. To the test the code, we can either input the code each time we run the python file (or python cell) (see the commented out code) or we can manually write in a test case. I put the test case(s) in `main` function and ran the `main` function.

```python
def order(value1,value2,value3):
""""This function takes in 3 values and orders them.
These nested if statements look pretty confusing. 
It is hard to manually trace my variables through the code so using the debugger helps."""
if value1 <= value2: #*1*2* 
if value2 <= value3: ##123
    print(value1,value2,value3)
else:
    if value3 <= value1: ##312
        print(value3,value2,value1) ##incorrect
    else: ##132
        print(value1,value3,value2)
else: #value2 <= value1
if value3<=value2:
    print(value3,value2,value1)
else:
    if value3<= value1:
        print(value2,value3,value1)
    else:
        print(value2,value1,value3)
def main():
#order(int(input("First: ")),int(input("Second: ")),int(input("Third: ")))
order(6,7,1)
main()
```

- `order(6,7,1)` outputs `1 7 6` instead of what we want `1 6 7`  but it's kind of hard to trace through the code to see where we went wrong so we can use the debugger to see which statements in the code we are using.
- If you have typed this into a python cell (using #%%), Click "debug cell" and then click the step into (down arrow) button to step into each line of code. This helps us trace through the code and help us look at which line goes wrong.
- If you have typed this into a python file, you need to add breakpoints into your code. A good place to add a breakpoint is at the line `def order(value1,value2,value3):` and then click the drop down Run > Start Debugging or F5 and use the Step Into button.

Contributors: Alex, Harsh
