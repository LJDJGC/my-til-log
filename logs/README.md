# Learning-log
## 2025/09/12 Morning
Topic: DOM Manipulation and Events with The Odin Project

- Types of web page manipulation possible with JavaScript
- Realization: Previously, I had an item that I couldn't click on in Python, so I automated the process using JavaScript web page manipulation code, and now I've created something a little familiar.
- Next up: Tonight, I'll continue studying Revisiting Rock Paper Scissors.

## 2025/09/16 Morning
Topic: Event Listeners and DOM Updates with JavaScript

Clarified the difference between event listeners and event handlers.

Understood why textContent is safer and clearer than innerHTML for adding plain text.

Realized that combining DOM manipulation with events is the foundation of making interactive web pages.

Next up: Tonight, I’ll continue with Rock Paper Scissors, this time adding event-driven interactions instead of relying only on prompts.


## 2025/09/16 Evening

What I Did Today

Learning Topic: DOM Manipulation and Event Handling

Based on the "shopping-list.html" starter file, I prepared a state with minimal CSS, labels, input fields, a button, and an empty <ul>.

Stored references to <ul>, <input>, and <button> in variables.

Created a function called handleClick that executes when the button is clicked.

Retrieved the value of the input element and saved it in a variable.

Empty the input field.

Created three new elements: <li>, <span>, and <button>.

Displayed the input value in the <span> and added a delete label to the <button>.

Added a <span> and <button> to the <li> and appended them to the <ul>.

What I Learned

The importance of using document.querySelector to retrieve HTML elements and store them in variables.

createElement and appendChild How to dynamically add elements using CSS.

Using an event listener to execute a function when a button is clicked

Creating a new element within a function allows you to generate a separate <li> element for each click.

Next steps

Add a click event to the added delete button to delete the list item.

Practice applying dynamic styles using CSS classes.


## 2025/09/16 Morning

# Shopping List DOM Practice

**Topic:** Event Listeners and DOM Updates

**What I Did:**
- Prepared starter HTML with minimal CSS, input, button, and empty list.
- Stored references to `<ul>`, `<input>`, and `<button>` in variables.
- Created `handleClick` function for button clicks.
- Retrieved input value and cleared input field.
- Created `<li>`, `<span>`, `<button>` elements.
- Set `<span>` textContent to input value and `<button>` textContent to "delete".
- Appended `<span>` and `<button>` to `<li>`.
- Added `<li>` to `<ul>`.
- Attached click event to delete button to remove the `<li>`.
- Focused input field after adding an item.

**What I Learned:**
- How to dynamically create and append elements using JS.
- Difference between event listeners and handlers.
- Using closures to maintain individual item behavior.

## 2025/09/17 Night

# What I worked on today
- Continuing the Rock Paper Scissors project
- Removed the "logic to play exactly 5 rounds (for loop)" from the `playGame()` function
- Prepared for future UI implementation by making the game progression more flexible.

# What I learned/observed
- When manipulating the DOM with JavaScript, you can add nodes to the element tree using appendChild.
- I understood how adding a child element and then appending it to the parent element reflects the changes in the browser.
- `textContent` is used to insert text into an element and does not affect the tag itself.
- When using Git, it's important to keep in mind the following sequence: "Initialize the repository" → "Add files" → "Commit" → "Push to remote."

# Next steps
- Proceeding with the Rock Paper Scissors UI implementation
- Using HTML and CSS to create buttons that can be clicked to advance the game.
- Creating a branch on GitHub (`rps-ui`) and proceeding with UI development.


## 2025/09/18 Morning
# Top Rock-Paper-Scissors
Overview

This morning, I worked on the Top Rock-Paper-Scissors project. The focus was on JavaScript DOM manipulation and event handling to prepare for an interactive UI version of the game.

What I Did

Set up HTML and references

Prepared the starter HTML with buttons for "Rock", "Paper", and "Scissors".

Stored references to these buttons in JavaScript variables for easier access.

Created event listeners for each button

Defined a function to handle a click on each button.

Each click updates a variable representing the player's choice.

Integrated player choice with existing game logic

Prepared the system to pass the player's selection into the existing playRound function.

The function already exists and calculates round results based on player and computer choices.

Kept console logging for debugging

Console outputs were used to verify that player choices and round results are correct.

Key Learnings

How to attach event listeners to buttons and capture user interaction.

Connecting UI elements to game logic without using prompts.

Understanding asynchronous event handling: the function waits for user clicks rather than executing sequentially.

Reinforcing the separation between data (player choice) and logic (round evaluation).

## 2025/09/18 Evening
Topic: Rock-Paper-Scissors Web Game (DOM Output Edition)
1. Objectives

Create a "Rock-Paper-Scissors" game in the browser

Select the player's move with button presses

The computer's move is random

Display the result and score on the screen

The first player to score 5 points wins the game

2. Learning Content and Progress
a) Initial Implementation

Consistently check the result and score with console.log()

Randomly select the computer's move with getComputerChoice()

Input from the button with getHumanChoice()

Determine the winner of a round with playRound(humanChoice, computerChoice)

b) Modify for DOM Output

Add a <div id="result"></div> to the HTML to display the results

Replace console.log() with resultDiv.textContent = ...

First, check by displaying only the results of the most recent round

Take small steps and change the display destination from console → Practice "changing to DOM"

c) Score Management

Define humanScore and computerScore as global variables

Update the score after determining the winner in playRound()

Call playGame() at the end of the round to determine the winner when the player reaches 5 points

3. Learning Discoveries and Challenges

Calling playGame() at the end of playRound() overwrites the round results

Displaying progress and the final winner requires careful consideration of div usage and display methods

If outputting as a history, it is more appropriate to use appendChild

Currently, we are testing the "overwriting display of the most recent round + score" option

4. Next Challenge

Organize a method for simultaneously displaying round results and scores

Consider using separate divs for the win/loss message and score, or displaying both in a single div

Add a mechanism to stop the game when a final winner is announced

5. Review of Learning

Event Listeners and DOM Learn how to coordinate outputs

Understand the importance of functional separation of responsibilities (deciding whether a game is won or lost, updating the score, and determining the winner)

Realize the effectiveness of iteratively checking and correcting in small increments

## 2025/09/19 Morning
Topic: Rock Paper Scissors UI (DOM Manipulation and Event Listeners)

- I started implementing a button-based rock-paper-scissors game using a combination of HTML and JavaScript.
- I encountered an error where `querySelector` returned `null`. I realized the cause was the timing of script execution and the order of HTML elements.
- Solutions:
- Move `<script>` to the end of the HTML.
- Or use `<script defer>` to execute it after the DOM is constructed.
- I also discovered a spelling mistake: `id="conputerResult"`, which needed to be changed to `computerResult`.
- I learned that small spelling errors and script loading order can quickly lead to "element not found" bugs.

Next, I'll test the UI again after making the corrections to ensure it displays correctly.

## 2025/09/24 Morning  
Topic: Rock Paper Scissors UI – Git, Branch Merge, GitHub Pages Deployment  

- Implemented **UI for Rock-Paper-Scissors** game (start button, score tracking, reset).
- Fixed issue where final result message disappeared too quickly → added `setTimeout` before reset.
- Controlled game flow with **disable/enable buttons** until "Start Game" is pressed.
- Learned how to **merge feature branch (`rps-ui`) into `main`** using `git checkout main` + `git merge rps-ui`.
- Cleaned up understanding of **committed vs. uncommitted changes** (merge showed "Already up to date" because edits weren’t committed yet).
- Successfully **pushed changes to GitHub**.
- Published project on **GitHub Pages** and confirmed live URL:  
  👉 [Live Demo](https://ljdjgc.github.io/top_rock-paper-scissors/)

Next up: Update README with project description and live preview link.

## 2025/09/24 Evening 

# Etch-a-Sketch Project

- Created a repository on GitHub and confirmed the process of connecting it to a local repository.
- Learned the basic operations of `git init` → `git remote add origin` → `git branch -M main` → `git push`.
- Created a README and completed the first commit and push.

- Reviewed the project assignment instructions.
- The goal was to generate a 16x16 grid using JavaScript.
- Dynamically added elements using a loop instead of directly arranging divs in HTML.
- Understood how easily a square can be created using CSS Grid and `aspect-ratio`.

- Organized implementation tips.
- Created cells using `document.createElement` and `appendChild`.
- Added cells efficiently using `DocumentFragment`.
- Confirmed the idea of ​​coloring cells with the `mouseover` event.

## Next Steps
- Actually created a 16x16 grid. Generate cells and display them in the browser.
- Implement a mechanism for changing cell color on hover and click.
- As a finishing touch, make the number of cells freely adjustable.

## 2025/09/25 Morning

Topic: Creating a 16x16 grid div with JavaScript and displaying it with Flexbox

- Preparing a `.container` div in HTML
- Creating a 16x16 div in `script.js` using `document.createElement` and `appendChild`
- An error occurred with the initial JS code:
- `count` in `console.log(myContainer, count);` was undefined → Changed to `i`
- Corrected `document.body.appendChild(...)` to `myContainer.appendChild(...)`
- Checking the display with CSS:
- Setting `display: flex; flex-wrap: wrap; width: 500px;` to `.container`
- Set `flex: 0 0 calc(100% / 16);` and `aspect-ratio: 1 / 1;` to the `.container div`.
- 0 height issue:
- This can be resolved by removing the `height` from the `.container` or by setting the cell to `height: calc(500px / 16);`.
- Set the background color `lightgray` to ensure the generated div looks correct.
- Currently, the 16x16 square grid is ready to be displayed using a combination of JS and CSS.

Next step:
- Add hover color behavior similar to Etch-a-Sketch.

## 2025/09/25 Night
Topic: 16x16 Grid Generation and Hover Effects with Flexbox

Lessons

Used JavaScript to dynamically generate 16x16 div elements without writing HTML.

Using Flexbox's flex-wrap and flex: 0 0 calc(100% / 16) to create a layout with 16 wrapped squares.

Confirmed that gaps and borders would cause the squares to collapse, and achieved a stable display with gap: 0.

Added mouseover event listeners to each generated div and applied a class to create a "trail" effect that changes the background color.

I learned

Executing document.createElement("div") once outside of a loop reuses the same element, resulting in incorrect generation of 256 divs.

Instead of writing classes directly in the HTML, dynamically using classList.add() in JavaScript is necessary for the "leave a trail" mechanism.

Even with Flexbox, care must be taken when handling gaps. You can include them in the calculation formula if necessary.

Next Steps

Combine mousedown / mouseup to allow drawing by dragging the mouse.

Expand the color from a fixed (black) to random or a gradual change in density.

Create a reset button to refresh the entire grid.

## 2025/09/28 Night

Topic: Creating a Pixel Drawing Grid Using CSS Grid
Learned Content

I created a 16x16 div element in JavaScript and tested a mechanism for changing its color with mouse operation.

I experimented with using flexbox on the .container in CSS to evenly distribute the cells.

I then switched to a grid layout and improved the implementation.

Key Points

The cell arrangement is specified on the container side (e.g., grid-template-columns).

The cell's appearance (background color, aspect ratio) is specified in the CSS for the child element.

flex-wrap is not required for grid.

Next Steps

Consider changing the cell color from fixed black to a random or selected color.

I will try extending it to more pen-like behavior, such as "draw only while clicked."

Make the grid size variable (e.g. 16x16 → 32x32).

## 2025/09/29 Morning 
In today's lesson, we worked through the steps of combining JavaScript and CSS to create an **interactive grid sketchpad**. The basic process was to first create a `.container` in HTML and then create a 16x16 div in JavaScript to create a grid. We maintained the square shape by using `aspect-ratio: 1/1` and managed the color by specifying `background-color` in CSS.

Looking back internally, at first, we realized that all we could see was black lines. We stopped and thoroughly checked the HTML structure, CSS class application, JavaScript variable references, etc. In particular, we noticed that we had incorrectly handled the i and square variables in the for loop, and that a CSS priority issue (a conflict between background and background-color) was preventing the colors from being reflected. We corrected these issues step by step.

By adding !important to the CSS .colored class and confirming that the class was actually added in the browser's developer tools, we were able to complete the color change function on mouseover. In this way, we were able to create a "pen"-like feature that turns black when you trace it with the mouse.

As a next step, we considered adding a button to the top of the screen that would delete the existing grid and generate a new grid with the same total area based on the new grid size entered by the user. Here, we reorganized the flow: obtaining input using prompt, limiting the maximum value (100), clearing using innerHTML = "", dynamically changing grid-template-columns, and again generating divs and attaching events. This resulted in a design that would allow a new sketchpad to be generated without changing the area, even for a 64x64 grid.

Through today's learning, I reaffirmed the importance of not simply writing code, but thoroughly verifying and understanding small elements such as CSS priority, JavaScript variable scope, DOM manipulation, and event firing timing. I found the process of identifying and checking each issue one by one to be extremely effective.

Next time, I plan to implement a button that generates grids based on user input, creating a more flexible and interactive sketchpad.

Today's Achievements

Completed 16x16 grid generation and hover-color change functionality

Understood CSS precedence issues and applied the .colored class

Now I can check class assignments in the developer tools

Refine the design of the dynamically resizable grid generation for next time

## 2025/09/29 Night
Topic: JavaScript Grid Generation and Hover Event Verification
1. Today's Lessons

Creating a system that changes the color of grid cells when hovered using HTML/CSS/JS

Displaying an initial 16x16 grid and allowing it to be resized with a reset button

Creating a div within a for loop and attaching a mouseover event

On reset, deleting existing cells and creating new ones with container.innerHTML = ""

Analyzing the cause of hover issues

Checking whether event listeners are attached correctly

Div size issues when CSS aspect-ratio doesn't work

Tips for isolating the problem:

Check whether events are being fired with console.log

Check the div size and class attachment in DevTools

If aspect-ratio doesn't work, test with a fixed height

2. Today's Lessons Learned and Awareness

If hover isn't working, first check whether an event is attached and whether the div "Does the size of this exist?" is questionable.

Operations on innerHTML must be performed outside the loop, or the grid will disappear.

The initial grid and post-reset grid generation processes are easier to manage if they are created as functions.

## 2025/09/30 Morning

This project uses JavaScript and CSS to create a 16x16 square grid, and creates a sketchpad that changes the mass color according to the user's mouse interaction.

Today's study content

Grid creation

Using JavaScript's document.createElement, create a 16x16 div element and place it inside the .container

Grid viewing using Flexbox

CSS display: flex; flex-wrap: wrap; realizes a grid that wraps side by side

Adjusting the square size

The width and height of each square are calculated and set using JS.

Color change during hovering

Initially, set the fixed color purple in CSS

Next, we will consider how to randomly generate RGB values ​​in JavaScript and change the color for each hover.

Issues and prospects for the next episode

To implement the effect of darkening by 10% in stages, we consider a design that maintains the state of each square with dataset.

Confirmed that random colors and gradual darkening cannot be achieved for each interaction with CSS alone

File configuration

index.html … HTML for grid display

style.css … Flexbox Grid, Mass Initial Style

script.js … Grid generation, color change processing by hover event

How to use

Open index.html in your browser

Create a grid of any size with the Reset button

Hovering the mass with the mouse changes color

## 2025/09/30 Evening
What I did today

Improved the square interaction function in the Etch-a-Sketch project

Implemented a system where each square changes to a random color when hovered, then gradually darkens after 10 hovers, finally reaching black.

Learned how to save the state of each square (base color and hover count) using dataset.

Introduced logic to generate a random color only the first time using if (!square.dataset.base) and darken the color based on the saved base color thereafter.

I confirmed that confusion between dataset.hover and dataset.hovers was the cause of the bug and understood that it needed to be fixed.

What I learned

Dataset makes it easy to store state in DOM elements.

The importance of separating "first-time processing" from "repeated processing" in event handlers.

To "darken the color," calculating it based on RGB values ​​rather than lowering opacity works better than "darkening the color"

What I'll do next

Modify dataset.hovers to use it correctly.

First hover Sometimes I decide whether to "color it as is" or "darken it by 10%."

Code organization (removing unnecessary console.log and standardizing variable names)

## 2025/10/01
Learned

Learned the basics of JavaScript objects

How to create objects, add and reference properties

Manage data for DOM elements using datasets

Dynamically create a 16x16 Flexbox grid using HTML/CSS/JS

Create divs using the createGrid() function

Place the grid within a .container

Arrange elements in a grid using flex-wrap in CSS

Set an event to change the color of each div on mouseover

Each div is initially a random color, then gradually darkens by 10% with each click or mouse action

Create a new grid size with the "Reset" button

Maximum input size is 100x100

Check hover counts in console.log for debugging

Today's Takeaways

Using objects makes it easy to manage information such as hover counts and base color for each div

Direct manipulation of the DOM and datasets You can maintain state by combining these.

Creating a grid with Flexbox makes it easy to arrange elements in rows and columns without using CSS Grid.

Combining clicks and mouseovers allows you to create gradual, pen-like movements.

GitHub Repository Setup Notes

File Structure Example:

/project-root
index.html
style.css
script.js
README.md

Commit messages should be small and frequent.

Example: October 1, 2025, Morning: Created a 16x16 grid, with color changes and gradual darkening on mouseover.

Publishing to GitHub Pages:

index.html must be in the root directory.

Select the branch and root in Settings > Pages.

Note the public URL and add it to the README.

About Live Preview (Live View)

If you're using Visual Studio Code, the Live Server extension is useful.

After installation, right-click index.html and select Open with Live Server.

The browser will launch automatically and reload automatically when changes are made.

You can also publish to GitHub Pages and view it in your browser.

## 2025/10/02 Morning
Today's Lesson: JavaScript Objects
1. Object Basics

Create an Object with let obj = {}

Dot Notation: obj.key = value

Bracket Notation: obj["key"] = value

Use the same syntax to overwrite existing properties

2. Numeric Operations within Objects

Loop through all properties of an object with for...in

Test whether a value is numeric with typeof obj[key] === "number"

If it is numeric, double the value with obj[key] *= 2

3. Benefits of Functions

Reusable functions, such as multiplyNumeric(obj)

The same process can be applied to other objects

Code is organized, improving readability and maintainability

4. Example
function multiplyNumeric(obj) {
for (let key in obj) {
if (typeof obj[key] === "number") {
obj[key] *= 2;
}
}
}

let menu = { width: 200, height: 300, title: "My menu" };
multiplyNumeric(menu);
console.log(menu);
// { width: 400, height: 600, title: "My menu" }

5. Next Lesson Plan

Extending multiplyNumeric to allow arbitrary multiplication

Advanced Object Manipulation Practice

## 2025/10/06 Night
🕓 Started Studying

While using the command line, I encountered the error "-bash: cd: too many arguments" when using the cd command.
→ This was caused by a directory name containing a space.
→ Learned how to enclose the string in quotation marks (" ") or escape spaces with \ .

Example:

cd "my-top_Object Basics-task"

or

cd my-top_Object\ Basics-task

Also practiced renaming directories (using the mv command).

mv "my-top_Object Basics-task" my-top_Object_Basics-task

→ Understand the importance of avoiding spaces in naming.

💻 JavaScript Learning: Understanding Arrays and map()

Topic: "Map to Names"

let john = { name: "John", age: 25 };
let pete = { name: "Pete", age: 30 };
let mary = { name: "Mary", age: 28 };
let users = [ john, pete, mary ];
let names = users.map(item => item.name);
alert(names); // John, Pete, Mary

Learning Points

map() is a method that converts an array into another form and returns a new array.

The callback function item => item.name is a conversion rule that extracts only the name property from each object.

item => item.name is an abbreviation for:

function(item) {
return item.name;
}

Understand the difference between users.name and item.name:

users refers to the entire array.

An item is the single element (object) currently being processed.

🧠 Deepening Understanding

Consider how map() works in terms of humans:

"Extract only the name (name) from each person (item) in a list and create a new list of names."

✅ Today's Achievements

Learned basic Bash file operations and directory naming rules.

Learned how to correctly use JavaScript's map() method.

Understood the structure and shorthand notation of arrow functions.

⏭ Next Schedule (Proposal)

Practice using for...of to mimic the behavior of map().

Expand your understanding by learning about other array methods such as filter() and reduce().

## 2025/10/07 Morning
Learning Content

This morning, we focused on JavaScript and practiced object and array manipulation.

Mapping an object array to another array

Creating a fullName from name and surname

Using map and arrow functions

Understanding why () is used around {}

let usersMapped = users.map(user => ({
fullName: `${user.name} ${user.surname}`,
id: user.id
}));

Sorting array objects by age

Using the sort method

Sort in ascending order using the comparison function (a, b) => a.age - b.age

function sortByAge(arr) {
arr.sort((a, b) => a.age - b.age);
}

Calculating the average age

Learn about both for loops and reduce

Confirming concise syntax using reduce

function getAverageAge(users) {
return users.reduce((sum, user) => sum + user.age, 0) / users.length;
}

Creating a keyed object from an array

id Create an object using the key.

Array → Object Conversion Using Reduce

function groupById(arr) {
return arr.reduce((acc, user) => {
acc[user.id] = user;
return acc;
}, {});
}

Learning Review

I learned how to use the {} and () arrow functions.

I confirmed the basic usage of sort and reduce.

I'm now familiar with combining array and object operations.

This knowledge will be useful for data manipulation and data formatting from the server.

Thoughts for the Day

You can get a feel for array and object operations by practicing them multiple times.
Reduce may seem difficult at first, but it's a powerful tool once you get used to it.

## 2025/10/07 Night
🌙 What I learned

Understanding object generation using reduce()

function groupById(array) {
return array.reduce((obj, value) => {
obj[value.id] = value;
return obj;
}, {});
}

reduce is a method for "combining an array into a single value (in this case, an object)."

First argument: Callback function (receives the accumulated value obj and the current element value).

Second argument: Initial value {} (initially an empty object).

Each element's id is used as a key, and the corresponding object is stored as the value.

The final object is obtained in the format { id1: {...}, id2: {...}, ... }.

💡 What I learned

reduce() is a powerful function that can convert an array into any form (number, string, object, etc.).

Reconfirming the meaning of return:

Return is a "door to bring results out of the function."

Without return, the function returns undefined.

Example:

const add = function(x, y) {
return x + y;
};
console.log(add(2, 3)); // 5

If you omit return, the result will be undefined and not passed anywhere.

🧠 Today's Realization

Even if the code works, it's meaningless if you don't consider how to handle the results.

The more abstract a function is, like reduce(), the quicker it's to understand it by going through it step by step.

From tomorrow onwards, I'd like to delve deeper into "applications of reduce" and "differences from map/filter."

⏭ Next Episode Preview

Practice advanced patterns of reduce()

Creating sums, maximum values, and count objects in arrays, etc.

Create a comparison table of map, filter, and reduce to clarify their usage.

## 2025/10/08 Morning 
🚀 Learning Topic: Coding Test Preparation (Basic Algorithms and JavaScript Functions)
🎯 Materials and Platforms Used
LeetCode (Easy): Two Sum Problem

JavaScript Function Assignment: subtract(), sum(), multiply()

🧠 Main Learning Content and Outcomes
1. Studying the LeetCode "Two Sum" Problem
Item Details Algorithm Learned
Goal: Return two indices from an array whose sum is target. O(N) solution using a hash map (Dictionary)
Learned Points: Since I found it difficult to solve the O(N)
2


On my own, I used the solution as a reference. I learned a pattern for storing array elements as keys and indexes as values ​​in a hash map, and then quickly (O(1)) searching for the required partner (target - num).
Technical Elements: Understand the role of Python's enumerate function (simultaneously obtaining index and element).
2. JavaScript Function Assignment Work
Function Name Achievement Lessons Learned/Improved
subtract() Completed (Correct) I learned that in concise functions, it is preferable to directly return the calculation result without using intermediate variables.
sum() Completed (Correct) While using the for...of loop to perform the summation is correct, I learned a more concise and versatile way to write it using the standard JavaScript function Array.prototype.reduce().
multiply() Initial Value Challenge I understood that when calculating all products, the initial value of the accumulator variable must be set to 1 (the multiplicative identity) rather than 0.
✅ Next Learning Action
I will register the "O(N) Search Pattern Using a Hash Map" I learned today in Anki and begin active recall.

To fully understand JavaScript's reduce() method, I will actively use it in other assignments, including multiplication calculations (multiply).

For the next LeetCode problem, first take 30 minutes to think about it on your own and be conscious of using hash maps.

## 2025/10/08 Night

📝 Overview
Today, we learned about basic JavaScript function implementation and the accompanying fundamentals of test-driven development (TDD). Practice focused on function arguments, variable scope, operators, and string and array manipulation.

🚀 Implemented Functions
multiply(numbers)

Objective: Takes an array of numbers and multiplies all elements.

Learned:

The need to set the initial value of the product to 1 instead of 0.

Iterating over arrays using the for...of loop.

Writing concise code using the *= compound assignment operator.

power(x, y)

Objective: Returns the result of multiplying the base x by the exponent y.

Learned:

How to use JavaScript's built-in exponentiation operator, **.

Directly returning the result allows you to omit unnecessary variables.

factorial(number)

Objective: Calculates the factorial of a given number.

What I learned:

The correct way to write update expressions (i-- and --i) in for loop syntax.

The correct syntax for the *= compound assignment operator and the importance of reassigning the calculation result to a variable.

palindromes(string)

Objective: Determine whether a given string is a palindrome.

What I learned:

The importance of limiting function arguments to only the necessary information.

How to clean up strings using regular expressions (RegExp) to ignore punctuation and whitespace.

A series of steps to convert a string into an array (split), manipulate it (reverse), and reconvert it (join).

🔧 Challenges and Solutions
Syntax Errors: I encountered syntax errors in the for loop update expression (--1) and the compound assignment operator (=*). This was a good opportunity to deepen my understanding of basic JavaScript grammar.

Logic error: Fixed a logic error in the factorial function, where the calculation result was not correctly assigned back to a variable.

⏭️ Carrying on to next time
Complete the implementation of the palindromes function.

Continuing with test-driven development, enable the remaining tests in calculator.spec.js one by one and complete the corresponding functions.

## 2025/10/09 Morning
Palindrome Checker: An Exercise in Algorithmic Efficiency
Overview
This repository features a concise JavaScript function, palindromes, designed to determine if a given string is a palindrome.

A palindrome is a sequence of characters that reads the same forward and backward. The function is engineered to be robust, meaning it automatically handles variations in case, punctuation, and spacing, focusing only on the alphanumeric characters for the check.

The JavaScript Implementation
This solution leverages powerful built-in JavaScript methods to achieve a clean and readable implementation.

JavaScript

const palindromes = function (str) {
    // 1. Clean and normalize the string: convert to lowercase and remove all non-alphanumeric characters.
    // The regular expression /[^a-z0-9]/g targets and removes punctuation and spaces globally.
    const cleanedStr = str.toLowerCase().replace(/[^a-z0-9]/g, "");

    // 2. Reverse the cleaned string using the split-reverse-join pattern.
    const reversedStr = cleanedStr.split("").reverse().join("");

    // 3. Compare the original cleaned string with the reversed string.
    return cleanedStr === reversedStr;
};
Algorithmic Analysis (Inspired by LeetCode) ⏱️
As we practice algorithms, understanding Time Complexity is crucial. This solution has a favorable performance profile:

Operation	Time Complexity	Notes
str.toLowerCase().replace()	O(N)	Iterates through the string once to clean it.
cleanedStr.split('')	O(N)	Creates an array from the string.
.reverse()	O(N)	Reverses the array; the most time-consuming step.
.join('')	O(N)	Joins the array back into a string.
Comparison (===)	O(N)	Compares the two strings character by character.
The overall Time Complexity is O(N) (Linear Time), where N is the length of the input string. This is considered very efficient, as the execution time grows linearly with the size of the input.

Examples
Input (str)	Output	Explanation
'racecar'	true	Simple seven-letter palindrome.
'tacos'	false	Not a palindrome.
'A car, a man, a maraca.'	true	Cleans to "acaramanamaraca".
'Lid off a daffodil.'	true	Cleans to "lidoffadaffodil".
Next Steps / Reflection
The Odin Project Focus: This exercise reinforced the practical use of regular expressions and efficient string manipulation in JavaScript.

LeetCode Challenge: While this solution is O(N), a classic variation is the Two-Pointer approach, which can solve the problem in-place (without creating a second reversed string) to achieve O(N) Time Complexity with O(1) or minimal O(N) Space Complexity. This is a potential optimization to explore.

## 2025/10/09 Night

What I Learned
💻 JavaScript Basics Practice
Reviewed the concepts of function arguments and local variables.

Started implementing a function that returns the Fibonacci sequence (Practice Problem 14).

Progress/Lessons Learned
Note that arguments are used to receive values ​​from outside the function, and that **.length** cannot be used.

Understood that implementing the Fibonacci sequence requires preparing two variables, the "previous number" and the "previous number," and updating them within a **loop (iterative process)**.

The challenges were setting the initial values ​​(1 and 1) and designing the number of iterations.

Next Task
Used a for loop to complete the **"memorize and update values"** process for the Fibonacci sequence.

Consider conditional branching that appropriately handles the first and second base numbers (1 and 1).

## 2025/10/10 Morning

💡 Today's Task
1. Palindrome Number
Problem: Given an integer x, implement a function that returns true if x is a palindrome (reads the same left or right), and false otherwise.

Solution Approach
For this problem, we considered two approaches: a string conversion approach and an approach using only integer arithmetic.

Approach Description Features
String Conversion: Convert the number to a string, reverse it using split(), reverse(), and join(), and then compare it to the original string. This is the simplest and most intuitive implementation.
Integer Arithmetic: After excluding negative numbers, use the modulus operator (% 10) and division (/ 10) in a loop to reverse the number itself. This is memory-efficient and the optimal solution, satisfying the constraint "solve without converting to a string" stated in the problem's appendix.
Implementation Code Example (Integer Arithmetic Approach)
JavaScript

/**
* @param {number} x
* @return {boolean}
*/
var isPalindrome = function(x) {
if (x < 0) {
return false;
}

let reversed = 0;
let original = x;

while (x > 0) {
/ 1. Get the last digit: x % 10
/ 2. Multiply the existing reversed number by 10 and add the new digit.
reversed = (reversed * 10) + (x % 10);

/ 3. Remove the last digit.
x = Math.floor(x / 10);
}

return reversed === original;
};
2. Fibonacci Sequence
Problem: Create a function fibonacci(number) that returns the Nth member of the Fibonacci sequence. (Number sequence used: 1,1,2,3,5,8,...)

Solution Approach
We used an iterative approach, using an array (data) to store the number sequence and continuously calculating new members through a loop.

Key Implementation Points
Initial Value Setup: Set the first two values ​​with let data = [1, 1];

Exception Handling: If number is 1 or 2, return the initial value without performing any calculations.

Loop Condition: Set the loop starting index i = 2, and repeat the calculation until the length of the array becomes N (i < number), completing the process with the correct number of iterations.

Implementation Code
JavaScript

const fibonacci = function(number) {
let data = [1, 1];

/ Process the first (data[0]) or second (data[1]) element.
if (number <= 2) {
return data[number - 1];
}

/ Start at i=2 and repeat until the array length is 'number'.
for (let i = 2; i < number; i++) {
/ Add the previous two elements.
const result = data[data.length - 1] + data[data.length - 2];

/ Add the new Fibonacci number to the end of the array.
data.push(result);
}

/ Return the last element of the array (the Nth member).
return data[data.length - 1];
};

## 2025/10/14 Morning
🎯 Goals
Understand the algorithm for finding the longest common prefix

Understand and practice JavaScript array manipulation methods (reduce, map)

💻 Exercises and Concepts
1. Longest Common Link (Longest Common Prefix)
Topic: Business
Difficulty: Easy
Related Methods: Array.prototype.reduce(), String.prototype.slice()
📝 Learning Points
Processing using reduce(): Learn an approach that processes array elements one by one and carries over the result of the previous processing (a temporary common prefix) to the next processing.

Efficient Comparison: Understand how to efficiently calculate the length of a common part by comparing string indexes one by one using a while loop.

Basic Concept: Using the first string as a base, identify the longest common prefix by comparing it with other strings and keeping only the common parts.

2. Get the title!
Topic: Array Manipulation
Difficulty: Easy
Related Method: Array.prototype.map()
📝 Learning Points
The Role of map(): Learn the basic purpose of the map() method: "Transform each element of an array and create a new array with the results."

Extracting Object Properties: Demonstrate the standard technique of bulk extracting only the values ​​of a specific property (book.title) from an array of objects.

Arrow Functions (=>): Understand how arrow functions (especially the shorthand notation) can be used as callback functions for higher-order functions like map(), and how their argument (book) refers to an element of the array.

🚀 Assignment for Next Time: Practice solving these problems independently using a for loop without using reduce() or map().

Review other built-in methods for array manipulation, such as filter() and forEach().

## 2025/10/14 Night
# My Top JavaScript Exercises (Completed)

# Overview

This repository contains a series of exercises I worked on to solidify my JavaScript foundation and provide intensive practice with array methods (e.g., `map`, `filter`, `reduce`).

I completed all exercises and learned how to implement each function.

# Key Aspects Completed

Through this series, I particularly mastered the following concepts and techniques:

- **Basic data types and operations**
- **Conditional branching and looping**
- **Built-in JavaScript array methods** (e.g., `reduce`, `map`, `filter`, `forEach`)
- **Manipulating objects and properties**
- **Separating logic with helper functions**
- **Calculating the current year and age using the `Date` object** (especially the final exercise)

# Highlights from the Final Exercise

In the final exercise, "Finding the Oldest Thing," I applied the following knowledge:

1. **Creating a Helper Function:** Define a function that accurately calculates a person's age (lifespan), regardless of whether they are deceased or alive.
2. **Applying the `reduce` Method:** Implement logic that traverses the entire array, stores the comparison results in an accumulator, and finally returns the oldest person object.

# Future Plans

Building on this foundation, we plan to move on to more complex projects and the next learning topic (e.g., DOM manipulation).

--

## 2025/10/15 Morning
Calculator Project
Overview
This project is a web calculator being developed as the final assignment of The Odin Project Foundations. It aims to implement a user-friendly interface and accurate calculation logic.

Tech Stack
HTML5

CSS3

JavaScript (ES6+)

🧠 Today's Learning and Technical Work
Before starting work on the project, we reviewed basic data structures and algorithms.

LeetCode 20. Valid Parentheses Solved
Today, we tackled a popular LeetCode problem to gain practical experience using the stack data structure.

Topic: Nesting parentheses and checking for correspondence using a stack (LIFO: Last-In, First-Out).

Learned:

Applying stacks: We learned a typical use of stacks: pushing an open parenthesis, then popping an element from the stack when a closing parenthesis is encountered to check for correspondence.

Using a hash map: Using a mapping (hash map/object) to manage pairs of closing and opening parentheses improved the readability and efficiency of the code.

Implementing the Core Logic of the Calculator Project
We started by implementing the application's core calculation logic.

Implemented Features (Core Logic)
The following functions for basic arithmetic operations were created in a JavaScript file and confirmed to work correctly in the browser console.

add(a, b): Addition

subtract(a, b): Subtraction

multiply(a, b): Multiplication

divide(a, b): Division

🔜 Next Steps
Building the UI with HTML/CSS: Define the structure of the calculator's buttons and display.

Operator Handling: Implement logic to manage the display state and the current operator.

DOM Integration: Integrate JavaScript and HTML/CSS to perform calculations in response to button clicks and display the results on the screen.

## 2025/10/15 Night
📚 Learning Topic
Implementing Basic Calculator Functions Using JavaScript

💡 Goals Accomplished
Implemented the four arithmetic operations (addition, subtraction, multiplication, and division) using JavaScript functions.

Learned how to test functions using the browser console.

Understood and implemented how to manage the basic elements that make up calculator operations (number 1, operator, number 2) as variables.

💻 Implementation Code and Contents
1. Arithmetic Functions
Implemented the four basic functions required for a calculator. Learned how to return results using the return statement.

JavaScript

// Addition
function add(a, b) {
return a + b;
}

// Subtraction
function subtract(a, b) {
return a - b;
}

// Multiplication
function multiply(a, b) {
return a * b;
}

// Division
function divide(a, b) {
return a / b;
}

// Console test example:
// console.log(add(5, 3)); // 8
// console.log(multiply(6, 7)); // 42
2. Managing Calculation Element Variables
The three elements that make up a basic calculator operation (e.g., 3 + 5) are stored as variables. We reaffirmed the use of quotation marks ('') for elements that should be treated as strings.

JavaScript

let operand1 = 3; // First number
let operand2 = 5; // Next number
let operator = '+'; // Operator (stored as a string)
⏭️ Next Step (TODO)
[ ] Create logic (if/else or switch statements) that calls the appropriate arithmetic functions using the three stored variables (operand1, operator, operand2).

[ ] Add safe handling (e.g., returning an error message) to the division function (divide) when dividing by zero (when b is 0).

## 2025/10/16 Night
💡 Theme
Implementing the Core Logic of a Calculator Using JavaScript

✅ What I Accomplished
I completed the functions for performing the four arithmetic operations (addition, subtraction, multiplication, and division), which are the core functionality of a calculator, and the main calculation logic that integrates and utilizes them.

Defining Basic Arithmetic Functions

I defined four functions: add(a, b), subtract(a, b), multiply(a, b), and divide(a, b).

Comparing Operators and Calling Functions

I implemented the operate(op1, op2, op) function, which selects and executes the appropriate arithmetic function based on the input operator (+, -, *, /).

In particular, I correctly used the comparison operator (===) for conditional branching and established logic to determine the operator.

Understanding the Role and Scope of Variables

I understood the need to store the calculation elements (operand1, operand2, operator) in variables and that they serve as initial values ​​for testing.

Understanding and applying safe and clean function design (scoping) by declaring calculateResult as a local variable within the operate function and returning its value with return .

💻 Today's Final Code (Core Logic)
JavaScript

function add(a, b) {
return a + b;
}

function subtract(a, b) {
return a - b;
}

function multiply(a, b) {
return a * b;
}

function divide(a, b) {
return a / b;
}

let operand1 = 3;
let operand2 = 5;
let operator = '+';

function operate(op1, op2, op) {
let calculateResult; // Store the calculation result in a local variable

if (op === '+') {
calculateResult = add(op1, op2);
} else if (op === '-') {
calculateResult = subtract(op1, op2);
} else if (op === '*') {
calculateResult = multiply(op1, op2);
} else if (op === '/') {
calculateResult = divide(op1, op2);

return calculateResult; // Return the result
}

let result = operate(operand1, operand2, operator);

console.log(result); // Output: 8
⏭️ Next Step
Add a process to the operate function to detect division by zero (when operand2 is 0) and return an error message to increase the robustness of the code.

Create HTML/CSS and prepare the buttons and display area on the screen.

Learn DOM manipulation in JavaScript and implement logic to dynamically update the values ​​of operand1 and operator in response to button click events.

## 2025/10/17 Morning

🎯 Goals

Build a prototype calculator that performs basic arithmetic operations and establish the foundation for the logic and layout.

🚀 Accomplishments

1. Defining JavaScript Logic

Defined the basic arithmetic functions that form the core of the calculator and the main functions that integrate them, and completed operational testing in the browser console.

Functions defined:

add(a, b): Addition

subtract(a, b): Subtraction

multiply(a, b): Multiplication

divide(a, b): Division (including exception handling for division by zero)

operate(op, num1, num2): Integration function that calls the appropriate function depending on the operator.

2. Creating and Improving the HTML Layout

Created the basic HTML structure for the calculator, including all required elements.

Elements: Display, number buttons (0-9), decimal point, arithmetic operators (+, -, ×, ÷), equals (=), and clear (C) button.

Improvements: CSS Grid was used to create a standard calculator layout (four-column layout).

Feature Identifiers: Each button was given a data-action attribute (number, operator, equals, clear) in preparation for JavaScript implementation in the next step.

3. Initial Variable Definition

Global variables were defined to manage the calculator's state.

firstNumber: First number

operator: Selected operator

secondNumber: Second number

displayValue: Current value displayed on the display

✅ Next Step (TODO)

Event Handling Implementation: Set up click event listeners for all buttons.

Display Update Logic: Store user input in the firstNumber, operator, and secondNumber variables and implement logic to update the display in real time accordingly.

Calculation execution: When the equals (=) button is pressed, the operate function is called and the result is displayed on the screen.

Support for consecutive calculations: The calculation result can be used as the firstNumber for the next calculation.

The logic defined today is working properly in the console. Next, we'll work on integrating it with the UI.



## 2025/10/20 Night

# 🧑‍💻 The Odin Project: Calculator

This is the learning repository for the "Calculator" project, a challenge in [The Odin Project].
The goal is to create a functional calculator using the basics of web development (HTML, CSS, JavaScript).

# 🎯 Project Goals

1. Implement basic arithmetic operations (addition, subtraction, multiplication, and division).
2. Create a user interface (buttons, display) in the browser.
3. Implement logic to manipulate the DOM using JavaScript, perform calculations based on user input, and display the results.

# 🚀 Current Progress

| Phase | Status | Completed Tasks |
| :--- | :--- | :--- |
| **I. Initial Setup** | ✅ Completed | - Created basic HTML (buttons, display) structure. |
| **II. Calculation Logic** | ✅ Completed | - Defined arithmetic functions (`add`, `subtract`, `multiply`, `divide`). |
| **III. Core Functions** | ✅ Completed | - Defined the `operate` function, including a divide-by-zero check, and fixed a bug. |
| **IV. Input Processing** | ✅ Completed | - Defined the screen state management variable `currentDisplayValue`. |
| **V. Event Processing** | ✅ Completed | - Implemented the `inputDigit` function to process **continuous input** when clicking a number button, and reflected it on the screen. |

## 📅 Future Learning Plan

| Date | Planned Tasks |
| :--- | :--- |
| 2025/10/21 | Implemented input processing for the **decimal point (`.`)**. (Prevents double input) |
| | Implement the functionality of the **Clear (`C`)** button. |
| | Implement the basic click processing for **operators (`+`, `-`, `×`, `÷`)**. (Save the first operand and operator) |
| 2025/10/22 | Completed calculation processing when clicking an operator and calculation processing for **equal (`=`)**. |
| 2025/10/23 | Design (CSS) and implementation of display digit limit. |

## 🔗 References

- [The Odin Project: Calculator Assignment]
- [MDN Web Docs]

## 2025/10/21 Morning
🗓️ What I learned
I refined the JavaScript logic for the calculator project's main functions and built a foundation for basic user interaction.

Improved number button processing (0-9) and decimal point (.):

Implemented logic to prevent duplicate zeros when entering numbers (overwriting a single zero and concatenating zeros).

Implemented conditional processing (using the includes() method) to prevent double entry of decimal points (.).

Building the logic foundation for operator buttons (+, -, ×, ÷):

Implemented a process to save the current displayed value as the first operand when an operator button is pressed.

Saved the selected operator in **operatorValue**.

Set the **waitingForNewInput** flag to reset the screen upon the next number entry and transition to a state where the second operand can be entered.

🚧 Main Issues Resolved
I understood the difference between += (concatenation) and = (assignment/overwrite) when the number or operator button is pressed, and modified the implementation.

I understood the need for global state management variables (firstOperand, operatorValue, waitingForNewInput) to store the calculated value and operator when processing operators, and added them to the code.

⏭️ Next Steps
Modifying the Event Listener: Change the current logic in allButtons.forEach to button.addEventListener('click', ...) so that the logic is executed when the button is clicked.

Performing the Calculation (=): Implemented the logic for the equals button, calling the operate function using firstOperand, operatorValue, and the current display value (second term), and displaying the calculation result.

## 2025/10/21 Night
Summary of Accomplishments
The primary focus of tonight's session was refactoring the calculator's event handling mechanism to ensure all button actions are correctly processed upon a click event. Key logic for handling number inputs and basic operator storage was established.

Refactored Event Handling: The redundant and error-prone structure (which executed logic immediately upon script load) was replaced. All button logic is now properly nested within a single button.addEventListener('click', ...) callback function for each button.

Centralized Number/Digit Input: Consolidated the processing for all number buttons (0-9) by correctly calling the inputDigit(buttonValue) function within the single if block, making the code much cleaner.

Implemented Operator Logic: Implemented the basic logic for handling operator button clicks (+, -, ×, ÷), ensuring the following sequence:

The current display value is stored in the global firstOperand.

The selected operator is stored in operatorValue.

waitingForNewInput is set to true, preparing the display for the second number.

Next Steps (To-Do)
Implement the Equals (=) Logic: Complete the functionality for the = button to perform the calculation using operate(firstOperand, secondOperand, operatorValue).

Implement Clear (C) Logic: Reset all state variables (currentDisplayValue, firstOperand, operatorValue, waitingForNewInput).

Refine Input Functions: Integrate decimal point (.) and waitingForNewInput handling more robustly within the inputDigit function.

## 2025/10/22 Morning

Today's session focused on integrating the core calculation logic into the calculator's state management, addressing several critical functionalities and bug fixes as requested.

🎯 Key Accomplishments and Focus Areas

The main goal was to finalize the functions responsible for full calculation flow (=, Clear, and continuous operations).

Core Functions (add, subtract, etc.): These remain stable.

operate Function: Identified a bug where the Zero Division check was performed after the division. This has been noted for immediate correction to ensure the error handling precedes the potentially crashing operation.

State Management: Variables like firstOperand, operatorValue, and waitingForNewInput are correctly defined.

Incomplete Logic: The initial implementation of handleEquals(), handleOperator(), and updateDisplay() was reviewed and found to be incomplete, specifically missing:

The actual call to operate() within handleEquals().

The logic for chained operations (e.g., 12 + 7 - 1), which requires immediate calculation and result preservation upon pressing a second operator.

Robust rounding/precision logic within updateDisplay().

Full implementation of the Zero Division Error flow (displaying the message and resetting state).

🚧 Next Steps

The next session will involve the final implementation of the complex logic identified during the review:

Refactor the operate function for correct Zero Division precedence.

Implement the complete handleOperator logic to enable seamless continuous calculations.

Finalize handleEquals to correctly conclude the calculation and reset the necessary state.

Complete the updateDisplay function, including result rounding and displaying the sarcastic error message for zero division.

Connect all functions to the HTML event listeners using the provided suggestions (especially mapping button IDs to operator symbols).


## 2025/10/22 Night
# Simple JavaScript Calculator Project

This project is a simple implementation of a four-function calculator built using vanilla JavaScript, HTML, and CSS. It is a fundamental learning exercise for practicing DOM manipulation, event handling, and managing application state in JavaScript.

## 🛠️ Features

* **Basic Arithmetic Operations:** Supports addition (`+`), subtraction (`-`), multiplication (`*`), and division (`/`).
* **Sequential Operations:** Allows for continuous calculations (e.g., `3 + 5 * 2`).
* **Error Handling:** Includes protection against division by zero.
* **Display Management:** Manages the display of inputs and results, including basic rounding/precision control for long numbers.
* **Clear Function:** A "Clear" button to reset the calculator state.

## 💻 Project Structure

The core logic resides in a single JavaScript file.

* `calculator.js`: Contains all the logic for the calculator, including arithmetic functions, state variables, event listeners, and display update functions.
* *(Note: HTML/CSS files are assumed to be present to provide the calculator interface and buttons, but the logic is focused on the JS file.)*

## 💡 Key Learning Points

The development of this calculator focused on:

1.  **Function Composition:** Creating small, reusable functions for each arithmetic operation.
2.  **State Management:** Implementing and managing state variables (`currentDisplayValue`, `firstOperand`, `operatorValue`, `waitingForNewInput`) to control the flow of the calculation.
3.  **Event Delegation/Handling:** Attaching event listeners to all button elements and determining the appropriate action (digit input, operator selection, equals, or clear) based on the button clicked.
4.  **Error Prevention:** Implementing a check to prevent "Zero Division Error".

## 🚀 How to Run

1.  Clone this repository.
2.  Open the `index.html` file (or the main HTML file) in your web browser.
3.  The calculator interface should appear, and you can begin testing the functions.

## 2025/10/23 Morning

Project: Basic Calculator App
This project implements the core functionality of a basic desktop calculator using HTML, CSS (implied, for structure), and JavaScript. The goal is to manage the calculator's state (operands, operator, display value) and handle complex operational sequences, such as continuous calculations and error handling.

🎯 Current Goals Achieved:
Core Arithmetic Functions: Implemented functions for add, subtract, multiply, and divide.

operate() Function: A central function that takes two numbers and an operator string, and calls the appropriate arithmetic function.

State Management: Utilizes global variables (currentDisplayValue, firstOperand, operatorValue, waitingForNewInput) to track the calculator's state.

Basic Input Handling: inputDigit() correctly manages single-digit input and prevents leading zeros.

Equality Handling (=): handleEquals() initiates the final calculation based on the stored state.

Clear Function: clearCalculator() resets the entire state.

Initial Continuous Calculation Logic: handleOperator() contains logic to store the first operand and manage subsequent operator presses.

🚧 Key Areas for Immediate Improvement (To be addressed next):
DOM Reference Fixes: Correct several variable and ID mismatch issues (buttonID vs buttonId, HTML IDs like equal and period).

updateDisplay() Fix: The updateDisplay() function is critically flawed:

It doesn't accept the required value argument.

It references an undefined result variable inside its logic.

The Zero Division Error message needs to be correctly displayed.

Operator Handling Logic: The handleOperator() function references an undefined inputValue variable. It needs to correctly use parseFloat(currentDisplayValue) as the second operand for continuous calculations.

Period/Decimal Input (.): The inputPeriod() function is defined but empty. The logic to handle the decimal point (and prevent multiple periods) must be implemented.

Zero Division Error Handling: The check for division by zero should be robustly implemented in the divide function or operate function, and the handling in handleEquals() and handleOperator() needs to be consistent. (The current operate function checks for a string '0', which may be incorrect if the input is converted to a number).

Continuous Operations: Refine the logic for sequences like 12 + 7 - 1 = to ensure the intermediate result (19) is correctly used as the new firstOperand.

## 2025/10/23 Night
Calculator Project - Progress Snapshot 

Goal
To build a functional web calculator using HTML and Vanilla JavaScript, fulfilling all advanced logic requirements (e.g., chained operations, precision, error handling).

Implemented Features
Core Arithmetic Functions: Defined add(), subtract(), multiply(), and divide().

operate Function: Implemented the central logic function to execute the chosen arithmetic operation based on the operator symbol.

DOM Structure: Completed the basic HTML structure (calculator.html) with all necessary buttons (0-9, ., C, +, -, ×, ÷, =).

Script Linking: calculator.js is correctly linked at the end of the <body> in calculator.html (Best Practice).

State Management Setup: Initialized global variables for calculator state: currentDisplayValue, firstOperand, operatorValue, and waitingForNewInput.

Basic Event Handling: Event listeners are attached to all buttons to call corresponding functions (inputDigit, handleOperator, handleEqual, clearCalculator).

Known Issues & Next Steps (Bugs & Incomplete Features)
The following critical issues must be addressed in the next session to make the calculator fully functional and meet all project requirements:

Logical Flaws in JS:

Undefined Variables: Several functions (e.g., updateDisplay, handleOperator, initial console.log) reference variables that are not defined in their scope (e.g., value, result, inputValue).

Broken updateDisplay(): The function is missing its required value argument and contains incorrect logic for zero division error checks and rounding.

Chained Calculation Logic: The logic in handleOperator is incomplete and flawed, preventing continuous operations (e.g., 12 + 7 - 1 =).

Zero Division Check: The check in operate is incorrect (op2 === '0', comparing a number to a string).

Missing Features:

Decimal Input: The inputPeriod() function is currently empty and needs full implementation.

Display Clearing: The logic to clear the display after a calculation result is shown (when a new digit is pressed) is missing.

HTML Improvement (Recommended):

The buttons in calculator.html should be updated with data-* attributes (e.g., data-type="digit", data-operator="*") to simplify the event listener logic in calculator.js.

## 2025/10/24 Morning
# Simple JavaScript Calculator Project

This repository contains a simple calculator built with plain JavaScript, HTML, and CSS. The goal of this project is to practice fundamental programming concepts, DOM manipulation, and logical flow control.

## Current Features

- **Basic Arithmetic Operations:** Supports addition, subtraction, multiplication, and division.
- **In-place Operator Handling:** Handles operator chaining (e.g., `5 + 3 + 2`) correctly.
- **Clear Functionality:** A clear button resets the calculator state.
- **Display Limit:** Numerical display is limited to a maximum of 9 significant digits (`MAX_DIGITS = 9`), using precision logic to handle long results.
- **Error Handling:** Displays a specific message for division by zero.

## Key Learning Points

### 1. Handling Array/List Manipulation (Separate Exercise)

- Practiced the "two-pointer" technique for in-place element removal (`removeElement` problem). This technique is crucial for optimizing space complexity.

### 2. Calculator Logic

- **State Management:** Maintaining the calculator's state using variables like `firstOperand`, `operatorValue`, and `waitingForNewInput`.
- **Operator Logic (`handleOperator`):** Ensures that the displayed value (`currentDisplayValue`) is converted to a number (`parseFloat`) and used as the second operand for chained calculations.
- **Display Truncation (`updateDisplay`):** Implemented logic to limit the displayed number to `MAX_DIGITS` using `toPrecision()` to maintain mathematical accuracy while fitting the screen.
- **Event Handling Refinement:** Improved button event handling to use an `if/else if` chain, ensuring that a single button click triggers only one action (e.g., a number button is not also treated as an operator).

## Next Steps

- [ ] Add support for the decimal point (`.`) input and logic.
- [ ] Implement the backspace/delete functionality.
- [ ] Refine keyboard support.
- [ ] Address edge cases for negative numbers and display formatting.

## 2025/10/27 Night

# JavaScript Calculator Project

This project is a functional, browser-based calculator built using HTML, CSS, and vanilla JavaScript. It is primarily a learning exercise focusing on handling complex UI logic, state management, and basic arithmetic operations in JavaScript.

## 🎯 Project Goals and Learning Objectives

1.  **Basic Arithmetic Functions:** Implement the core functions for addition, subtraction, multiplication, and division.
2.  **`operate` Function:** Create a function to take two numbers and an operator, and call the correct arithmetic function.
3.  **DOM Manipulation:** Connect the HTML buttons to the JavaScript logic to capture user input.
4.  **State Management:** Successfully manage the calculator's state using key variables:
    * `currentDisplayValue`: The number currently shown on the screen.
    * `firstOperand`: The first number in a calculation (e.g., the '3' in '3 + 5').
    * `operatorValue`: The chosen operation (e.g., '+', '-', etc.).
    * `waitingForNewInput`: A boolean flag to handle when the next digit should clear the display or continue the current number.
5.  **Chained Operations Logic:** Implement the tricky logic for continuous calculations (e.g., `12 + 7 - 1 =`). The calculator must evaluate the preceding operation when a new operator is pressed.
6.  **Edge Case Handling:** Address potential issues to make the calculator robust:
    * **Zero Division Error:** Display a humorous error message instead of crashing.
    * **Display Overflow:** Round long results to fit the display (e.g., max 9 digits).
    * **Decimal Input (Bonus):** Allow users to input floating-point numbers while preventing multiple decimal points (e.g., `1.2.3`).
    * **Keyboard Support (Bonus):** Add functionality to use the computer keyboard for input.

## ✅ Current Progress (as of 2025/10/27 Night)

* [x] Basic HTML structure and button layout.
* [x] Core arithmetic functions (`add`, `subtract`, `multiply`, `divide`).
* [x] `operate` function implemented with Zero Division Error check.
* [x] Event listeners for digits, operators, equals, and clear.
* [x] Logic for basic two-number calculations (`A operator B =`).
* [x] Logic for chained operations (`A operator B operator C...`).
* [x] `clear` function implementation.
* [ ] **In-Progress:** Implementing the decimal point (`.`) input function.
* [ ] **To Do:** Finalizing number rounding and display overflow logic.
* [ ] **To Do (Bonus):** Implementing backspace and keyboard support.


## 2025/10/28 Morning
# Simple JavaScript Calculator

This is a basic, fully functional calculator implemented using HTML, CSS (not included in this file but assumed), and JavaScript. It handles standard arithmetic operations and follows typical calculator logic for chained operations and display precision.

## Features

* **Basic Arithmetic:** Supports addition (+), subtraction (-), multiplication (×), and division (÷).
* **Chained Operations:** Allows for continuous calculations (e.g., `10 + 5 * 2 =` should evaluate `10 + 5` first, display 15, then calculate `15 * 2`).
* **Display Precision:** Rounds results with many decimal places to a maximum of 9 digits, using scientific notation (`e`) for extremely large or small numbers when necessary.
* **Zero Division Handling:** Displays a humorous error message ("OMG:(") when attempting to divide by zero and resets the calculator state.
* **Clear Functionality:** The 'C' button resets all internal states and the display.
* **Decimal Support:** Allows input of decimal numbers using the '.' button.
* **Input Handling:** Ensures that new input clears the previous result after an operation is complete.

## Technologies Used

* HTML5
* CSS3 (for styling)
* JavaScript (ES6+)

## How to Run

1.  Save the provided HTML (`calculator.html`) and JavaScript (`calculator.js`) files in the same directory.
2.  Open `calculator.html` in your web browser.
3.  (Optional) Add CSS to style the calculator interface.

## Project Structure

* `calculator.html`: The structure of the calculator interface.
* `calculator.js`: Contains all the calculator's core logic and functionality.

## Core Logic Highlights

The calculator manages its state using three key variables:
1.  `currentDisplayValue`: The number currently shown on the screen.
2.  `firstOperand`: Stores the first number in the operation (or the result of a previous chained operation).
3.  `operatorValue`: Stores the pending arithmetic operator (+, -, *, /).

The logic ensures that when a second operator is pressed, the pending operation (`firstOperand` and the current `currentDisplayValue`) is immediately evaluated before setting the new operator, enabling correct chained calculation flow.


## 2025/10/28 Night

# Simple JavaScript Calculator

This is a web-based calculator application built using HTML, CSS (not shown in the provided files, but implied for styling), and pure JavaScript.

## Features

This calculator includes all standard basic arithmetic operations and handles typical edge cases found in calculator design.

### Core Functionality
* **Basic Operations**: Addition (`+`), Subtraction (`-`), Multiplication (`×`), and Division (`÷`).
* **Chained Operations**: Supports continuous calculations (e.g., $12 + 7 - 1 = 18$).
* **Display Management**: Clears the display when a new number is pressed after an equals operation.
* **Clear Function**: A 'C' button to reset all current calculation states.

### Error Handling & Precision
* **Zero Division Error**: Displays a custom error message (e.g., "OMG:(" or "Zero Division Error") when attempting to divide by zero, and resets the calculator state.
* **Display Limit**: Automatically rounds or uses precision for results with too many decimal places to prevent display overflow.

### Added Features (To be implemented or already present)
* **Decimal Support**: Allows inputting decimal numbers using the `.` button.
* **Back Space / Delete**: (Planned or Implemented) A function to remove the last digit entered.
* **Keyboard Support**: (Planned or Implemented) Full calculator control via the keyboard.

## Files

* `calculator.html`: The structure of the calculator interface (buttons and display).
* `calculator.js`: The JavaScript file containing all the calculator's core logic and functionality.

## Usage

1.  Open the `calculator.html` file in your web browser.
2.  Use the on-screen buttons or your keyboard to perform calculations.


## 2025/10/29 Morning 

# Simple Calculator
This is a fully functional calculator application built using HTML, CSS, and vanilla JavaScript. The design is inspired by the clean, modern aesthetic of the Apple iOS calculator.

# Features
Basic Arithmetic: Supports addition (+), subtraction (-), multiplication (×), and division (÷).

Chained Operations: Correctly handles continuous calculations (e.g., 12 + 7 - 1).

Zero Division Error: Displays a custom error message ("OMG:(") when attempting to divide by zero.

Decimal Support: Allows input of floating-point numbers using the decimal point (.), preventing multiple decimals in one number.

Backspace Functionality: The backspace button (←) and keyboard 'Backspace' key correctly remove the last digit.

Keyboard Support: The calculator is fully operable using number keys, operator keys (+, -, *, /), Enter/Equal, and Escape/Clear.

Digit Limiting: Long results are rounded to a maximum of 9 digits to fit the display.

# Technologies Used
HTML: Structure and button elements (calculator.html).

CSS: Styling for an Apple-inspired dark/orange theme (style.css).

JavaScript (Vanilla): Core calculation logic and DOM manipulation (calculator.js).

# How to Run
Clone this repository or save the files locally.

Ensure the three files (calculator.html, style.css, and calculator.js) are in the same directory.

Open calculator.html in any web browser.

# Future Enhancements
Implement operator highlighting (inverting colors) to show the currently selected operation.

Add functionality for percentage (%) and sign change (+/-).

Improve error display handling.

## 2025/11/04 Night
# 🧮 Calculator

This is a web-based calculator application developed as part of **The Odin Project's** curriculum. The project focuses on building a functional calculator using HTML, CSS, and JavaScript.

## ✨ Features

* **Basic Arithmetic:** Supports addition, subtraction, multiplication, and division.
* **Clear and Backspace:** Functionality to clear the display (`C`) and remove the last entered digit (`←`).
* **Responsive Design:** Styled with the intention of mimicking the look and feel of a **mobile calculator interface, specifically inspired by an iPhone calculator's aesthetic** (currently only basic dark-mode styling is implemented, with further CSS enhancements planned).

## 🛠️ Technologies Used

* **HTML5:** Structure and content.
* **CSS3:** Styling (currently includes basic dark background and white text).
* **JavaScript:** Logic for calculator operations (to be implemented in `calculator.js`).

## 📁 File Structure

* `calculator.html`: Main HTML file containing the calculator layout.
* `style.css`: CSS file for styling the calculator.
* `calculator.js`: JavaScript file for handling the calculator's logic (input, calculations, and display updates).

## 🚀 Getting Started

1.  Clone this repository.
2.  Open `calculator.html` in your web browser.

---

## 2025/11/05 Morning
🚀 Today's Changes
The focus of today's session was on restructuring the CSS and refining the HTML to achieve a more authentic iPhone calculator look and feel, particularly in terms of layout and sizing.

CSS (style.css)
Layout Refinement: Replaced the previous flex-basis logic with a more robust Flexbox structure to correctly align buttons into four columns.

The .buttons container is now a full Flex container.

Each row (.first-row through .fifth-row) is set as a flex-direction: row container to correctly distribute the buttons horizontally.

Aesthetic Improvements:

Updated the body background to white (#ffffff).

The display now has a white background (#ffffff) and black text (#000000), a deviation from the previous dark theme, moving towards a style that resembles the classic iPhone calculator display field.

The container now uses justify-content: space-evenly to ensure all button rows and the display have appropriate vertical spacing.

Sizing and Spacing:

Set a fixed height for the display and buttons (height: 75px) for a more consistent, block-like appearance.

The button sizing logic (flex-basis: calc(25% - 7.5px)) has been standardized for most buttons to create equal-width columns.

HTML (calculator.html)
Added ID/Class for Custom Styling: Added the class bottom to the 0 and = buttons to potentially facilitate their unique sizing/positioning in the last row.

Button Reordering: The "C" (Clear) and "←" (Backspace) buttons were reordered in the .first-row.


## 2025/11/05 Night
# 🧮 Calculator Project: iOS Aesthetic

This project is the **Calculator assignment** from **The Odin Project's Foundations curriculum**. The goal was to build a fully functional web calculator using basic web technologies, with a specific focus on replicating the clean, modern look and feel of an **iPhone calculator**.

## ✨ Features Implemented

* **Core Arithmetic Operations:** Supports addition (+), subtraction (-), multiplication (×), and division (÷) using an `operate` function.
* **Chained Operations:** Allows continuous calculation without pressing the equals button after every operation.
* **Input Handling:**
    * Digit and Operator input via on-screen buttons.
    * Keyboard support for digits, operators (`+`, `-`, `*`, `/`), Enter (for `=`), Backspace, and Escape/C (for Clear).
* **Display Logic:**
    * Handles decimal input (`.`).
    * Includes a **Backspace** (`←`) function to delete the last entered digit.
    * Implements a **Clear** (`C`) function to reset all calculations.
    * Includes a logic to handle and visually represent large numbers using `toPrecision` up to 9 digits.
* **Error Handling (with Humor!):** Displays a custom message ("OMG:(") when attempting division by zero, preventing program crash.

## 🎨 Design and Styling

The calculator is styled to closely mimic the **dark mode iOS/iPhone aesthetic**:

* **Layout:** A compact, mobile-friendly container with distinct vertical spacing for the display and button grid.
* **Button Grid:** A robust 4-column Flexbox layout ensures buttons are uniformly sized and correctly positioned across all rows.
* **Color Scheme:** Uses the standard dark theme:
    * Number Buttons (`btn-num`): Dark gray (`#1a1a1a`).
    * Operator Buttons (`btn-op`): Signature orange (`#FFAA33`).
    * Function Buttons (`btn-func`): Gray (`#808080`).
* **Zero Button:** Special styling is applied to the '0' button for an elongated, oval appearance (though not fully finalized in the provided CSS, the structure is ready).

## 🛠️ Tech Stack

* **HTML5:** Structure (`calculator.html`).
* **CSS3:** Styling and layout using Flexbox (`style.css`).
* **JavaScript (ES6+):** Core logic, operation handling, and DOM manipulation (`calculator.js`).


## 2025/11/06 Morning

## 🚀 Learning Progress and Context (2025/11/06)

This project has served as a capstone for the Foundations path, demonstrating proficiency in core web development.

* **HTML/CSS Milestone:** Completed the essential styling and layout (including complex Flexbox arrangement for the buttons) for the calculator interface.
    * *Note:* The design, closely mimicking the requested iPhone aesthetic, is now considered finalized.
* **JavaScript Implementation:** Successfully implemented the full calculation logic in `calculator.js`, including chained operations, error handling, and keyboard support.
* **Current Focus:** The developer has officially moved on to **The Odin Project's JavaScript Full Stack path**, starting with the Introduction/Intermediate HTML & CSS course materials. This repository marks the successful completion of the Foundations final project.

## ✨ Features Implemented

* **Core Arithmetic Operations:** Supports addition (+), subtraction (-), multiplication (×), and division (÷).
* **Chained Operations:** Allows continuous calculation without pressing the equals button after every operation.
* **Input Handling:** Digit, Operator, and **full Keyboard support** for calculation.
* **Display Logic:** Handles decimal input (`.`), **Backspace** (`←`), and a **Clear** (`C`) function to reset calculations.
* **Error Handling (with Humor!):** Displays a custom message ("OMG:(") when attempting division by zero, preventing program crash.

## 🛠️ Tech Stack

* **HTML5:** Page structure definition.
* **CSS3:** Style and layout using Flexbox.
* **JavaScript (ES6+):** Calculation logic and DOM manipulation.


## 2025/11/06 Night
# 🧮 The Odin Project: Calculator (Foundations Capstone)

This project serves as the final capstone assignment for **The Odin Project's Foundations curriculum**. It is a fully functional web calculator built using core web technologies, meticulously styled to replicate the clean, dark-mode aesthetic of an iPhone calculator.

## ✅ Project Status & Learning Milestones

The Calculator project is **100% complete** and successfully deployed via GitHub Pages, marking the successful conclusion of the Foundations path.

### 🚀 Current Learning Focus: JavaScript Full Stack

The developer has transitioned to the **JavaScript Full Stack path** and is actively working through its initial modules.

* **Course:** Introduction: Intermediate HTML and CSS Course
* **Progress:** **4% Complete** (as of 2025/11/06)
* **Significance:** This stage involves deepening the understanding of advanced CSS topics (e.g., Flexbox, Grid, Responsive Design) and preparing for the complex JavaScript projects ahead.

## ✨ Key Features (Calculator Project)

* **Full Arithmetic:** Supports addition, subtraction, multiplication, and division.
* **Chained Operations:** Allows continuous calculations (e.g., `5 + 3 - 2 =`).
* **Keyboard Support:** Fully operable using the numeric keypad and standard operator keys.
* **Error Handling:** Custom error message ("OMG:(") for division by zero scenarios.

## 🛠️ Tech Stack

* **HTML5:** Structure.
* **CSS3:** Styling and precise layout using Flexbox.
* **JavaScript (ES6+):** Core operation logic and DOM interaction.



## 2025/11/07 Morning
### 🚀 Current Learning Focus: JavaScript Full Stack

Developer has transitioned to the JavaScript Full Stack path and is currently actively working on its initial modules.

* **Course:** Introduction: Intermediate HTML and CSS Course
* **Today's Progress (2025/11/07 AM):** Progressed through the **Emmet** section. This will improve the speed and efficiency of writing HTML and CSS.
* **Overall Progress:** 4% complete (progress compared to the previous day).
* **Significance:** This stage deepens understanding of advanced CSS topics like Flexbox and Grid, laying the groundwork for more complex JavaScript projects.

## ✨ Main Features (Calculator Project)

* **Full Arithmetic:** Supports addition, subtraction, multiplication, and division.
* **Chaining:** Allows consecutive calculations (e.g., `5 + 3 - 2 =`) without pressing the equals key.
* **Keyboard Support:** Full usability using the numeric keypad and standard operator keys.
* **Error Handling:** Custom error message for division by zero scenarios ("OMG:(").

## 🛠️ Tech Stack

* **HTML5:** Structure.
* **CSS3:** Styling and precise layout using Flexbox.
* **JavaScript (ES6+):** Core math logic and DOM manipulation.


## 2025/11/10 Morning
# 🚀 The Odin Project: Learning Log Update

## 🗓️ Today's Progress (2025/11/10 Morning)

| Course | Topic | Status | Note |
| :--- | :--- | :--- | :--- |
| **Intermediate HTML and CSS Course** | **Emmet** | **Completed** | Mastered **Emmet abbreviations** and syntax for rapid HTML structure and CSS property generation, which will significantly speed up coding efficiency in future projects. This marks a continued progression into the Full Stack path. |


## 2025/11/11 Morning
# 🚀 The Odin Project: Learning Log Update

## 🗓️ Today's Progress (2025/11/11 Morning)

This morning focused on a dual approach: deepening core development skills via The Odin Project and improving algorithmic problem-solving via NeetCode.

| Platform | Course/Topic | Status | Note |
| :--- | :--- | :--- | :--- |
| **NeetCode** | **Contains Duplicate** (Array/Hash Map) | **Completed** | Successfully solved this fundamental problem, reinforcing concepts of efficient data structure use (Hash Maps) for time complexity optimization. |
| **The Odin Project** | **Emmet** (Intermediate HTML and CSS Course) | **Completed** | Finalized the review and practice of Emmet abbreviations, ensuring maximum efficiency for future HTML/CSS coding. |
| **The Odin Project** | **Tables** (Intermediate HTML and CSS Course) | **In Progress** | Started the module on semantic HTML tables, including structure, styling, and accessibility best practices. |

---

## ✅ Previous Milestones (Summary)

* **Calculator Project:** **100% Complete** (Foundations Capstone).
* **Current Path:** JavaScript Full Stack (Intermediate HTML/CSS module).

## 🛠️ Project Tech Stack

* **HTML5 / CSS3:** Structure and Layout (Flexbox).
* **JavaScript (ES6+):** Core operation logic and DOM interaction.


## 2025/11/11 Night
# 🚀 The Odin Project: Learning Log Update

## 🗓️ Today's Progress (2025/11/11 Night)

This evening was dedicated to deepening intermediate front-end knowledge via The Odin Project.

| Platform | Course/Topic | Status | Note |
| :--- | :--- | :--- | :--- |
| **The Odin Project** | **Tables** (Intermediate HTML and CSS Course) | **Continued** | Focused on the structural and semantic aspects of HTML tables. Currently progressing through the module covering `<thead>`, `<tbody>`, `<tfoot>`, and accessibility features. |

---


## 2025/11/12 Morning
# 📚 Learning Log - 2025-11-12 Morning

## 📅 Date & Time
**Date:** November 12, 2025 (Wednesday)
**Time:** Morning Session

---

## 🎯 Focus Areas

| Course/Topic | Status | Details |
| :--- | :--- | :--- |
| **HTML & CSS Course** | In Progress | Tables Intermediate |
| **Algorithm Practice** | Completed | NeetCode - Valid Anagram |

---

## 💻 Detailed Notes

### 1. HTML & CSS Course: Tables Intermediate

* **Objective:** Deepen understanding of advanced table structuring and styling.
* **Key Concepts Covered:**
    * Using the `colspan` and `rowspan` attributes to merge cells.
    * Implementing table semantically with `<thead>`, `<tbody>`, and `<tfoot>`.
    * Styling tables effectively using CSS properties like `border-collapse`, `caption-side`, and `:nth-child()`.
* **Next Steps:** Move on to **Forms** or **Layout techniques** in the course.

### 2. Algorithm Practice: Valid Anagram (NeetCode)

* **Problem:** Given two strings, *s* and *t*, return `true` if *t* is an anagram of *s*, and `false` otherwise.
* **Solution Approach Used:** **Hash Map (Frequency Counting)**
    * Created two frequency maps (or a single map and decrement approach) to store the character counts for both strings *s* and *t*.
    * Confirmed that both strings have the same length initially (a necessary condition).
    * Iterated through the map to check if all character counts match (i.e., all counts are zero in the single map approach).
* **Complexity:**
    * Time Complexity: $O(n)$, where $n$ is the length of the string (due to iterating through the string once and the alphabet once).
    * Space Complexity: $O(1)$, since the map size is capped at 26 (the number of lowercase English letters).

---

## ✅ Summary & Reflection

Today was a balanced session focusing on both **web development fundamentals (HTML tables)** and **core algorithmic thinking (Anagrams)**. The frequency counting method for the Anagram problem was a good refresher on efficient string manipulation.

**What went well:** Successfully implemented the core concepts of table structure and solved the algorithm problem efficiently.

**Areas for improvement:** Practice more complex table layouts, especially those involving responsive design considerations.

---

## ⏭️ Plan for the Next Session

* Review solutions for **Valid Anagram** using the **Sorting** method for comparison.
* Start the **Forms** section of the HTML/CSS course.

## 2025/11/12 Night 
🌙 Evening Study Session: November 12, 2025
📚 Course/Topic: Intermediate HTML and CSS Course - Tables
🎯 Goal for the Session:
To continue studying the technical documentation/site for the Tables section of the course.

✅ Progress Achieved:
Continued reading and reviewing the technical content related to creating and styling tables in HTML and CSS.

(Add specific sub-topics here if you recall any, e.g., Reviewed colspan and rowspan properties or Explored CSS Grid for table-like layouts.)

🛑 Current Status:
Stopped partway through the reading material for the night.

Next step: Will resume the course/reading material from where I left off tomorrow.


## 2025/11/13 Morning
💻 Morning Learning Log - November 13, 2025
Overview
Finished my morning programming session. Today's focus was on algorithmic practice using NeetCode and intermediate HTML/CSS with The Odin Project.

Algorithm Practice (NeetCode) 💡
Problem: Two Sum (Easy)

Status: Completed.

Reflection: Although it's an "Easy" problem, I found it challenging, which reinforced the need for continued practice. My goal is to keep working on these types of problems to strengthen my algorithmic thinking and implementation skills (実装できるようになりたい).

Web Development (The Odin Project) 🌳
Course/Section: Intermediate HTML and CSS Course

Topic: Tables

Activity: I was in the middle of attempting the MDN Table Assessment when the session concluded.

Status: In progress (Paused mid-assessment).

Next Step: Complete the MDN Table Assessment.

Personal Goal ⭐
Consistency is key. I am committed to daily practice, even when the problems (like those on NeetCode) feel difficult, to improve my overall problem-solving and coding abilities.


## 2025/11/13 Night 
# 🪐 Web Development Learning Log: Planet Data Table Challenge

This repository contains my work-in-progress solution for a table structuring challenge, primarily focusing on advanced HTML table markup and corresponding CSS styling.

## 📅 Log Date

**November 13, 2025 (Night Session)**

## 🎯 Current Challenge

The challenge is to correctly structure and style an HTML table that displays various data points for the planets in our solar system.

* **Source:** The task is linked from The Odin Project's "Tables Intermediate HTML and CSS Course," which points to the **MDN Web Docs** challenge: [https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/Planet_data_table](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/Planet_data_table)

## 💻 Progress

I have successfully created the initial `index.html` file with the basic table structure for the "Terrestrial planets" section (Mercury and Venus) and implemented a corresponding `style.css` file.

### Key Accomplishments:

* **HTML Structure (`index.html`):**
    * Used the `<table>`, `<caption>`, `<tr>`, `<th>`, and `<td>` elements.
    * Successfully added the table caption with a hyperlink.
    * Implemented `<th>` elements for column headers.
    * Used the `<sup>` tag for the exponents in the "Mass" column (`10<sup>24</sup>kg`).
* **CSS Styling (`style.css`):**
    * Defined basic table styling (`border-collapse`, borders).
    * Styled table cells and headers (`padding`, `text-align`, `background-color`).
    * Applied basic **zebra striping** using the `:nth-child(even)` and `:nth-child(odd)` selectors for better readability.

### Pending Tasks:

The table structure is currently incomplete and needs to be extended to include the remaining sections as required by the challenge:

1.  **Complete Terrestrial Planets:** Add Earth and Mars data.
2.  **Add Jupiter and Saturn:** Structure and add data for the "Gas giants."
3.  **Add Uranus and Neptune:** Structure and add data for the "Ice giants."
4.  **Implement Advanced Semantics:** Correctly use `<thead>`, `<tbody>`, `<tfoot>`, `<th>` with `scope`, and implement `rowspan` and `colspan` to semantically group the planets (Terrestrial, Gas, Ice). *This is the primary remaining structural challenge.*

## 💡 Reflection

Working through this practical challenge is significantly deepening my understanding of how to correctly use advanced HTML table elements (like `rowspan` and `colspan` which are required next) and how to apply CSS selectors to structure and style data effectively. This hands-on approach is very valuable.


# 2025/11/14 Morning
🚀 Learning Log for The Odin Project
Date
November 14, 2025 (Morning)

Course
The Odin Project: Tables Intermediate HTML and CSS Course

Progress
Successfully completed the majority of the Tables Assessment from MDN exercise. All core table structures, spans, and accessibility features (scope, <caption>) have been implemented.

Current Challenge & Solution Focus
I am currently working on the final styling task:

Challenge: Add a black border around the columns that contain the planet names, using the appropriate <colgroup> / <col> structure and the provided CSS class style: .column-border.

Plan to Resolve
The solution requires two steps:

HTML Structure: Identify the columns to be bordered (the planet names are likely in the first column, or a specific range of columns) and wrap the corresponding <col> elements within a <colgroup> element placed immediately after the <caption> tag.

CSS Application: Apply the provided .column-border class to the appropriate <col> or <colgroup> element to activate the styling.

Example HTML Structure for the Solution:

HTML

<colgroup>
    <col class="column-border">
    <col>
    <col>
    </colgroup>
Next Steps
Complete the MDN Tables Assessment by implementing the <colgroup> and .column-border class.

Move on to the next topic in The Odin Project Intermediate HTML and CSS Course.


# 2025/11/14 Night

📚 Learning Log: Intermediate HTML & CSS
Date
November 14, 2025 (Night Session)

Course
Intermediate HTML and CSS Course

Completed Task
MDN Tables Assessment

Details
I successfully completed the designated Tables Assessment from MDN (Mozilla Developer Network). This hands-on exercise was an excellent opportunity to put my newly acquired skills in HTML table creation and CSS styling into practice.

Reflection
Finishing the assessment felt incredibly satisfying. I got a huge rush of accomplishment from seeing the completed work. I feel myself getting more and more hooked on programming! I'm ready for the next challenge.


## 2025/11/17 Morning
📅 November 17, 2025 (Morning) Learning Log💻 Computer Science (NeetCode)✅ Completed Understanding of Top K Frequent ElementsTopic: Top K Frequent ElementsProgress: Completed understanding of the problem's solution (bucket sort approach).Achievement: Learned a highly efficient method that can process in $O(N)$ time complexity, faster than standard sorting or heap-based $O(N \log N)$ methods.🌐 Web Development (The Odin Project)📘 Intermediate HTML and CSS CourseStatusModuleContentCompletedTables* Learned how to structure data using appropriate semantic HTML elements (<table>, <thead>, <tbody>, <tr>, <th>, <td>).* Understood how to use the colspan and rowspan attributes to span cells.In ProgressDefault Styles* Started learning about default styles provided by browsers. * This is important as a foundation for resetting or normalizing styles before applying custom CSS.


## 2025/11/17 Night
Learning Log – 2025/11/17 Night
Topic: CSS Units (Intermediate HTML & CSS Course)
Overview

Tonight’s session was dedicated to reading and completing the section on CSS Units from the Intermediate HTML and CSS Course. The focus was on understanding how different measurement units behave, and how to choose the right one depending on layout or design needs.

What I Studied
CSS Units Overview

I reviewed both absolute and relative units used in CSS and gained clarity on their practical applications.

Absolute Units

px

cm, mm

in, pt, pc
Used when consistent, non-scaling sizing is required.

Relative Units

em – relative to the font size of the element

rem – relative to the root (html) font size

% – relative to the parent element

vw, vh – viewport width/height units

vmin, vmax – relative to the smaller/larger viewport dimension

These units are essential for responsive layouts and scalable typography.

Key Takeaways

Relative units provide far better flexibility for modern, responsive design.

rem is ideal for consistent typography scaling.

Viewport units such as vw/vh help create full-screen sections and adaptive UI components.

Understanding the relationship between parent and child elements is crucial when using % or em.

Reflection

Finishing this section strengthened my understanding of how CSS controls layout sizing. Building intuition for choosing the proper unit feels like a foundational skill that will directly impact future projects, especially as I work toward more advanced frontend development.


## 2025/11/18 Morning
Learning Log – HTML/CSS & Algorithm Practice

Date: 2025-11-18

Overview

Today’s session focused on strengthening frontend fundamentals through CSS units and improving algorithmic thinking with string encoding/decoding logic. The goal is to build a consistent habit of learning both practical web development skills and core computer science concepts.

Topics Covered
1. CSS Units

From the Intermediate HTML and CSS Course, I reviewed and practiced multiple CSS measurement units, focusing on when and why to use each.

Key Concepts Learned

Absolute units: px, pt, cm, etc.

Relative units:

em – relative to the font size of the element

rem – relative to the root font size

% – relative to the parent element

vw, vh – relative to viewport dimensions

vmin, vmax – responsive behavior based on the smallest/largest viewport dimension

Practical understanding of when to use responsive units (e.g., rem, vw) vs fixed units (e.g., px).

2. NeetCode – Encode and Decode Strings

Worked on the classic “Encode and Decode Strings” problem from NeetCode, focusing on reliable string packing and parsing.

Key Takeaways

Encoding strategy: <length>#<string>

Decoding logic:

Parse the length prefix

Skip the # delimiter

Extract exactly length characters

Learned the importance of avoiding ambiguous encodings and handling variable-length strings safely.

Example (JavaScript)
class Solution {
  encode(strs) {
    let res = '';
    for (let s of strs) {
      res += s.length + '#' + s;
    }
    return res;
  }

  decode(str) {
    let res = [];
    let i = 0;
    while (i < str.length) {
      let j = i;
      while (str[j] !== '#') {
        j++;
      }
      const length = parseInt(str.slice(i, j));
      const value = str.slice(j + 1, j + 1 + length);
      res.push(value);
      i = j + 1 + length;
    }
    return res;
  }
}

Reflection

Today’s study combined practical UI skills with algorithm problem-solving. Understanding CSS units improved my ability to write responsive layouts, while the encode/decode exercise strengthened string manipulation and parsing skills. Both areas support my long-term goal of becoming a strong software engineer with solid fundamentals.


## 2025/11/18 Night

Learning Log - November 18, 2025 (Night Session)
Course Progress
Continued studying The Odin Project's Intermediate HTML and CSS Course
What I Studied

Progressed through the Intermediate HTML and CSS course materials
Read up to a certain point in the curriculum at　intermediate html and css
Took a quick read-through approach with plans for deeper review later

Study Strategy

Initial approach: Quick reading to get an overview of the concepts
Planned review method: Active recall sessions scheduled for weekends
This two-phase approach allows for initial exposure followed by deeper retention through active recall practice

Next Steps

Continue with the remaining sections of the Intermediate HTML and CSS course
Implement active recall review sessions on upcoming weekends to reinforce learned concepts
Practice applying the HTML and CSS techniques covered in the course


Study Method: Quick reading + Active recall review
Course: The Odin Project - Intermediate HTML and CSS
Date: November 18, 2025 (Night)


## 2025/11/19 Morning 
📘 Learning Log — 2025/11/19 Morning
Overview

This morning, I continued working through the Intermediate HTML and CSS Course. I completed the section on CSS Units and made progress into More Text Styles.

What I Learned
✅ CSS Units

Reviewed the differences between absolute units (px, pt) and relative units (em, rem, vw, vh).

Practiced choosing appropriate units based on context, such as fluid layouts, accessibility, and scalability.

Strengthened understanding of how em and rem propagate and how they affect component design.

🚧 More Text Styles (In Progress)

Started exploring additional text-related properties beyond the basics.

Practiced working with line height, letter spacing, and advanced font-related techniques.

Began applying these styles to improve readability and hierarchy in sample layouts.

Next Steps

Finish the More Text Styles section.

Move on to more complex layout and design topics in the Intermediate Course.

Apply what I learned to small personal projects to reinforce unit selection and typographic control.


## 2025/11/19 Night 
2025/11/19 Night — Learning Log
More Text Styles (Intermediate HTML and CSS Course)

Today I continued working through the Intermediate HTML and CSS Course, focusing on the More Text Styles section. This session covered several styling techniques that improve readability, visual hierarchy, and overall typography in web pages.

What I Studied
1. Text Decoration & Transformation

Learned how to apply text-decoration (underline, line-through, overline).

Practiced text-transform to control capitalization (uppercase, lowercase, capitalize).

2. Line Height & Letter Spacing

Adjusted line-height to improve text readability.

Used letter-spacing to create subtle visual differences in headings and body text.

3. Font Styling

Reviewed font-style, font-weight, and how to choose appropriate font combinations.

Experimented with making text bold, italic, or lighter for emphasis.

4. Text Alignment

Practiced using text-align to position text (left, right, center, justify).

Observed how alignment affects layout depending on container width.

5. Combining Multiple Text Rules

Applied multiple styling rules to create clean, readable sections of content.

Improved understanding of how small typographic adjustments change the feel of the page.

What I Gained Today

A deeper understanding of typographic control using CSS.

More confidence in creating readable, visually balanced text layouts.

A stronger foundation for building polished web interfaces moving forward. 


## 2025/11/20 Night
2025/11/20 Night — Learning Log
More Text Styles (Intermediate HTML and CSS Course)

This evening, I continued studying the More Text Styles section of the Intermediate HTML and CSS Course. My focus was on understanding how to enhance typography using various CSS properties.

What I Learned

How to apply advanced text-style properties to improve readability and visual hierarchy.

Techniques for adjusting text appearance, such as:

text-transform

text-decoration

line-height and spacing adjustments

font-weight and font-style refinements

The importance of consistent typography across a webpage.

Progress

Completed reading through part of the More Text Styles module.

Strengthened my understanding of how CSS controls text presentation.

Gained more confidence with intermediate-level HTML/CSS concepts.

Next Steps

Continue the remaining sections of More Text Styles.

Practice applying these styles in a small project or demo page.

Move forward to the next module in the Intermediate HTML and CSS curriculum.


## 2025/11/21 Morning
2025/11/21 Morning — Learning Log
More Text Styles (Intermediate HTML and CSS Course)
NeetCode — Valid Sudoku

This morning, I continued studying the More Text Styles section of the Intermediate HTML and CSS Course and worked through the Valid Sudoku problem from NeetCode.

What I Studied
1. More Text Styles — HTML & CSS

Continued learning advanced text styling options in CSS.

Reviewed how typography affects readability and overall page design.

Practiced using properties like text transformation, decoration, spacing, and font adjustments.

2. NeetCode — Valid Sudoku

Completed a walkthrough of the Valid Sudoku problem.

I was able to follow the logic and understand how the solution works.

However, I noticed that I cannot fully recall the solution from memory yet.

This likely means that my understanding is not fully solid, and I need more active practice.

Reflections

The CSS material felt straightforward and enjoyable to continue.

For NeetCode, I realized that understanding once is not the same as being able to reproduce the solution without looking.
I need more repetition, deeper reasoning, and active recall to truly master it.

Next Steps

Continue the rest of the More Text Styles module.

Revisit the Valid Sudoku problem and rewrite the solution from scratch.

Use active recall: try explaining the algorithm in my own words and implement it without hints.

Move on to the next NeetCode problem once I feel comfortable reproducing the solution reliably.

## 2025/11/25 Morning

📚 Learning Log: More Text Styles (System Font Stacks)Here is a summary of the concepts covered while working through the System Font Stack section of the Intermediate HTML and CSS Course.📝 Key Concepts Learned1. The System Font Stack (Native Fonts)A System Font Stack is a list of font-family values that directs the browser to use the default user interface (UI) font of the operating system (OS) or device being used.Goal: To make the text on a website look native to the user's OS, resulting in a clean, fast-loading, and comfortable reading experience.Performance Benefit: Since these fonts are already installed locally on the user's device, the browser does not need to download any web font files, leading to zero latency and instant rendering.2. Standard CSS Stack for System FontsThe modern standard system font stack is complex because it must account for the default UI fonts used across all major operating systems, which have different default fonts (e.g., Apple uses San Francisco, Windows uses Segoe UI, Android uses Roboto).The typical CSS declaration looks like this:CSSfont-family:
    -apple-system, 
    BlinkMacSystemFont, 
    "Segoe UI", 
    Roboto, 
    Helvetica, 
    Arial, 
    sans-serif;
Breakdown of the Stack:Font/KeywordTarget OS/Use-apple-systemTargets Safari and Firefox on macOS/iOS. This ensures the proprietary San Francisco font is used correctly.BlinkMacSystemFontTargets Chrome on macOS. It's necessary for handling the San Francisco font specifically in Blink-based browsers."Segoe UI"The default UI font for Windows (7 and later).RobotoThe default system font for Android devices and many ChromeOS devices.Helvetica, ArialFallbacks for older macOS/iOS versions and older Windows/Linux systems that might not recognize the modern UI fonts.sans-serifThe generic family fallback; ensures some non-serif font is used if all else fails.💡 Practical Implementation NoteTo implement this, you simply apply the full stack to the body or html selector in your CSS to affect all primary text on the page:CSSbody {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
}
This ensures that the text renders using the most appropriate native font available on the user's device, prioritizing speed and familiarity.


## 2025/11/25 Night
🚀 Intermediate HTML and CSS: Typography Progress
Today, I focused on the following resources to deepen my understanding of web typography best practices and font implementation:

More Text Styles (Intermediate HTML and CSS Course)

Completed the module on Font Best Practices. This covered essential techniques for ensuring text is readable, accessible, and visually appealing across different devices.

MDN's article on web fonts

Reviewed the article to understand the technical details of using web fonts, including performance considerations, the @font-face rule, and different font formats (e.g., WOFF2, TTF).

web.dev Typography guide

Studied this comprehensive guide, which emphasizes the impact of typography on website performance and user experience (UX). Key topics included font loading strategies, font-display, and techniques to mitigate layout shift (FOUC/FOIT).

🧠 Key Takeaways
Performance is crucial: Optimizing font loading (e.g., preloading, subsetting, and using WOFF2) is essential for faster page loads.

Accessibility First: Using sufficient contrast and appropriate line-height and font-size is non-negotiable for readability.

The Power of @font-face: Understanding how to properly define font families and sources is fundamental to using custom web fonts effectively.


## 2025/11/26 Morning

📚 Learning Log: Intermediate Web Development & Algorithms
Intermediate HTML and CSS Course: More Text Styles & CSS Properties
This week, I continued my studies in the Intermediate HTML and CSS Course, focusing on advanced text styling and a broader range of CSS properties.

More Text Styles: I learned how to use more granular control over text presentation, including:

Using the font-variant property, specifically font-variant: small-caps;.

Controlling text overflow and wrapping with properties like white-space and text-overflow.

Implementing custom fonts using the @font-face rule.

More CSS Properties: I explored additional essential CSS properties that enhance layout and design capabilities:

Deeper dive into CSS Box Model properties, focusing on how padding, border, and margin interact.

Utilizing CSS variables (Custom Properties) for maintaining consistency and making global style changes easier. For example: body { --main-color: blue; } and using it via color: var(--main-color);.

Understanding and applying different box-shadow effects for depth.

NeetCode: Valid Palindrome (Algorithm Practice)
I also tackled a fundamental algorithm problem from the NeetCode platform: Valid Palindrome.

Problem: Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Approach: The most efficient solution I practiced involved the Two-Pointer technique.

Preprocessing: First, I focused on filtering the string to include only alphanumeric characters and converting it to a consistent case (e.g., lowercase).

Two Pointers: I initialized a left pointer at the start and a right pointer at the end of the processed string.

Iteration: The pointers moved inward (left++, right--) until they crossed. At each step, I compared the characters at both pointers. If the characters didn't match, the string was not a palindrome.

Learning Outcome: This exercise reinforced the importance of string preprocessing and demonstrated the efficiency of the Two-Pointer pattern for sequence-based problems.

Next Steps
Continue the HTML and CSS course to cover Flexbox and Grid.

Practice more string and array manipulation problems using the Two-Pointer technique.


## 2025/11/26 Night
📚 Learning Log: Progress in the Intermediate HTML and CSS Course
Intermediate HTML and CSS Course
This week, we continued our study of the **Intermediate HTML and CSS Course**, particularly diving deeper into the area of ​​advanced CSS selectors.

More CSS Properties
Going further from last time, we learned about important properties that give you greater control over your web design.

Advanced Properties: Continuing from last time, we learned how to apply various properties to achieve more granular control over layout and design.

Practical Use: We gained a practical understanding of how combining properties can achieve complex layout requirements and interactive effects.

Advanced Selectors
We focused on more powerful selectors, essential for precisely targeting elements.

Combinators:

Descendant Selector ( ): Selects all elements that are descendants of an element.

Child Selector (>): Selects only the direct children of an element.

Adjacent sibling selector (+): Selects a single sibling element that immediately follows an element.

General sibling selector (~): Selects all sibling elements following an element.

We studied these selector combinations in detail, referring to MDN articles, to gain a deeper understanding of how to select specific elements in complex document structures.

Pseudo-classes:

Dynamic selectors that select elements based on user actions or element state.

Examples: **:hover**, **:focus**, **:nth-child()**, **:first-child**, etc. We learned that they are powerful tools for selecting form states and specific items in lists.

Pseudo-elements:

Used to style specific parts of elements that don't exist in the DOM tree.

Examples: **::before**, **::after** (to add content), **::first-line**, **::selection**, etc. We learned how to add decorative content and apply styles to specific parts of text.

We've seen that mastering these advanced selectors will enable you to write more flexible and maintainable CSS without changing your HTML structure.

Next Steps
Continue the course and learn the full-scale layout modules: Flexbox and CSS Grid.

Actively apply and solidify the combinators and pseudo-classes you've learned so far in real-world projects and coding practice.



## 2025/11/27 Morning
💻 Learning Log: Intermediate HTML and CSS
I've made good progress through the Intermediate HTML and CSS Course, supplemented by a coding challenge focusing on fundamental algorithms.

🚀 Coding Challenge
Platform: NeetCode

Problem: Two Integer Sum II

Focus: Practiced problem-solving and algorithm implementation (likely involving sorting or hash maps/pointers for efficient look-up).

🎨 Intermediate HTML and CSS Course Topics
I have completed the following major sections of the course:

1. More CSS Properties
This section expanded my understanding of essential layout and styling properties.

Box Model Review: Reinforced the concepts of content, padding, border, and margin.

Backgrounds: Learned about advanced background properties, including using background-image, background-repeat, and background-size.

Text and Fonts: Explored deeper controls over typography, such as using font-weight, font-style, and implementing custom fonts via @font-face or external libraries.

Visibility and Opacity: Mastered using the opacity property and the distinction between display: none; and visibility: hidden;.

2. Advanced Selectors
This module focused on writing more specific, efficient, and maintainable CSS by utilizing a wider range of selectors.

Attribute Selectors: Learned how to select elements based on the presence or value of an attribute (e.g., [type="text"] or [data-id]).

Pseudo-classes: Studied selectors that target elements based on their state or position (e.g., :hover, :nth-child(), :focus, :first-of-type).

Pseudo-elements: Gained experience with selectors that style specific parts of an element (e.g., ::before and ::after for content generation).

Combinators: Practiced using the various combinators:

Descendant Selector (space)

Child Selector (>)

Adjacent Sibling Selector (+)

General Sibling Selector (~)


## 2025/11/27 Night
thank you for your hard work! It's hard to concentrate when you're tired.

Based on what you have learned, create a README for the Intermediate HTML and CSS Course that focuses on Advanced Selectors.

This README is a concise summary of the course objectives, what you will learn, and who it is intended for.

📚 Intermediate HTML and CSS Course: Advanced Selectors
💡Course overview
This course is designed for those with basic knowledge of HTML and CSS to learn more advanced and efficient styling techniques. In particular, we will focus on the detailed use of CSS selectors and develop the ability to write accurate and maintainable CSS even for web pages with complex DOM structures.

🚀 What you can learn (Advanced Selectors)
By completing this course, you will understand and be able to use the following advanced selectors in practice:

Attribute Selectors: A method of selecting elements based on specific attributes or values ​​of attributes.

Example: [type="text"], [class^="btn-"]

Pseudo-classes: A method of selecting elements based on their state or position in the DOM.

Examples: :nth-child(), :first-of-type, :hover, :focus

Pseudo-elements: A way to style parts of an element (first character, first line, surrounding content, etc.).

Examples: ::before, ::after, ::first-letter

Combinators: A method of selecting elements using relationships between elements (parent-child, siblings, etc.).

Example:

child selector (>)

Adjacent sibling selector (+)

General sibling selector (~)

🎯 Target audience
Those who understand the basic syntax of HTML and CSS (elements, classes, ID selectors, etc.).

Those who want to acquire more sophisticated CSS writing skills that target many elements with less code.

Anyone who wants to improve the maintainability and efficiency of their website.

## 2025/11/28 Morning
📚 Intermediate HTML and CSS Course: Advanced Selectors
💡 Course Overview
This course is intended for those who already have a basic knowledge of HTML and CSS. It delves deeper into more advanced and flexible selectors that go beyond simple element, class, and ID selectors. This will help you acquire the skills to efficiently write accurate, maintainable CSS, even for complex web page structures.

🚀 What You'll Learn (Advanced Selectors)
By completing this course, you will understand the following **Advanced Selectors** and be able to use them in practical web development.

1. Attribute Selectors
This method selects elements based on specific attributes or their values. It is very useful for forms and elements that contain specific data.

[attribute]: Elements where the attribute exists

[attribute="value"]: Elements with an exact match

[attribute^="value"]: Elements whose attribute value starts with the specified string

2. Pseudo-Classes
Select elements based on their state (e.g., hover, click) or their position in the DOM (e.g., the first child in a list).

Structural Pseudo-Classes: :nth-child(), :first-of-type, :only-child, etc., for selection based on parent-child relationships or order.

User Action Pseudo-Classes: :hover, :active, :focus, etc., for selection based on user interaction.

Form-Related Pseudo-Classes: :checked, :disabled, etc., for selection based on the state of a form element.

3. Pseudo-Elements
Used to style specific parts of an element (e.g., the first line) or additional content generated by CSS, rather than the entire element.

::before / ::after: Add and style content before or after an element.

::first-line: Style only the first line of an element.

4. Combinators
Combines multiple selectors to select elements based on their relationship (parent-child, sibling, etc.).

Child selector (>): Selects only direct child elements.

General sibling selector (~): Selects all subsequent sibling elements with the same parent.

🎯 Audience
Familiarity with HTML and CSS (element, .class, #id selectors).

Those who want to accurately style more complex layouts with less code.

Those who want to improve the reusability and maintainability of their website code.


## 2025/12/01 Morning
📅 Learning Log: December 1, 2025
💻 Computer Science & Algorithms
Platform: NeetCode

Topic: 3Sum (LeetCode problem)

Notes: Continued practice with Two Pointers technique within a larger problem context. The key challenge was efficiently handling duplicate triplets and establishing the initial sort to enable the two-pointer approach.

🌐 Web Development
Platform: The Odin Project

Course: Intermediate HTML and CSS Course

Topics Covered:

Advanced Selectors: Focused on mastering more specific and powerful CSS selectors, including attribute selectors ([attr], [attr="value"]), pseudo-classes (:nth-child(), :first-of-type, :not()), and pseudo-elements (::before, ::after).

Intermediate HTML and CSS: Deepened understanding of layout properties and semantic HTML structure.

🧠 Reflection & Strategy
I've been encountering difficulty in quickly moving through new material, especially in areas that require deeper understanding before they "click."

Observation: Areas requiring time for initial comprehension (like complex algorithms or advanced CSS rules) are slowing down my pace.

Challenge: Balancing the urge to read quickly and rely on active recall later with the need to fully grasp the current concept to proceed effectively.

Potential Strategy: For difficult topics, I will try a "skim-then-deep-dive" approach:

Skim: Read through once to get the high-level overview.

Immediate Deep-Dive: Focus on a small, specific segment (e.g., one selector type, one part of the 3Sum solution) and implement a small example or write down the logic immediately to ensure initial comprehension before moving on. This blends initial reading with immediate practical application/recall.



## 2025/12/01 Night

📚 Learning Log: Advanced Selectors in CSSProject/Course Title: Intermediate HTML and CSS Course - CSS DinerDate: December 1, 2025Topic Covered: Advanced CSS SelectorsOverview & GoalThis session focused on practicing advanced CSS selectors by working through the levels of CSS Diner. The primary goal was to gain a deeper understanding and practical application of various selector types, including:Attribute selectors (e.g., $[attr], $[attr=value], $[attr^=value] )Pseudo-classes (e.g., $:nth-child(), $:only-of-type, $:not() )Combinators (e.g., General Sibling Combinator $`\sim`$, Adjacent Sibling Combinator $`+`$ )Key Takeaways & ChallengesStruggles with Retention: I found it challenging to retain the specific syntax and behavior of all the advanced selectors. While I could solve the puzzles with the help of references, the knowledge is not yet solidified in my long-term memory.Example of a challenging concept: Distinguishing between $`:nth-child()`$ and $`:nth-of-type()`$.Need for Active Recall: I recognize that passive learning isn't sufficient for these complex rules. Active recall is essential for true retention and fluency.The Scope of Programming: I'm struggling with how to apply effective active recall techniques to the vast and ever-expanding scope of programming knowledge. The sheer volume of concepts makes focused review difficult.Next Steps for RetentionFocused Review: Create flashcards (or use a similar spaced repetition system) specifically for the selectors covered in CSS Diner to enforce active recall.Implementation: Immediately apply these selectors in a small, practical personal project to move the knowledge from theory to application.

## 2025/12/02 Morning
📖 Learning Log: Advanced Selectors
Course & Topic
Course: Intermediate HTML and CSS Course

Platform: CSS Diner

Topic: Advanced Selectors

Progress & Current Challenge
I've been working through the CSS Diner exercises, focusing on Advanced Selectors.

My current challenge is with Attribute Selectors.

The Goal: To select all elements that possess a specific attribute.

An attribute is written inside the element's start tag (e.g., <span attribute="value">). Attributes don't always need to have a value; they can also be blank.

Attribute Selector Syntax
[attribute]

Examples
a[href] selects all <a> elements that have an href="anything" attribute.

[type] selects all elements that have a type="anything" attribute.

I'm currently struggling to grasp the nuances and proper application of this type of selector in the exercises.