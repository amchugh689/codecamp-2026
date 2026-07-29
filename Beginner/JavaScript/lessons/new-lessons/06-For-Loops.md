___
A for loop allows you to repeat code multiple times without writing it over and over again.

Let's take a look at what a for loop looks like:

```js
for (let i = 0; i < 5; i++) {
  console.log("Hello!");
}

```

Let's break this down - fortunately for you not in the rap sense:

- **for**: this is the keyword that says we are going to make a for loop
- **()**: inside the brackets goes 3 things, where we start, the condition and the update:
	- **where we start**: this is where the count for the for loop begins if I want to count from 0 to 5 then the count starts as 0, and we set that to a variable in most cases called `i`.
	- **the condition**: this is the condition that must be met for the for loop to end, similar to an if statement. In the above example this will repeat while the variable `i` is less than 5.
	- **the update**: This is how much the variable `i` increases by each time the loop goes round. `i++` adds 1 to `i` each time, but if we want to count in 2's we could add 2 each loop.
- **{}**: The code block that we are going to repeat goes inside the curly brackets, similar to If Statements the code we write in here **SHOULD** be indented to make your life easier.
