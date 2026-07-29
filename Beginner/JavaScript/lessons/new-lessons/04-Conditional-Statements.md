___

In real life we need to make a lot of decisions, like am I going to eat 5 donuts or 6 donuts. It's a tough call. When programming it is exactly the same, the programs we write often reflect real life whether it be a process or a behaviour our code will need to make decisions based on different things. 

To make a decision in programming we use something called an If Statement. For example if we had a log in page. We would need to check **IF** the password the user has entered matches the password we have stored. **IF** it does then we let the user log in otherwise we show an error.

___
### How to Compare things:

To compare values in a programming language we use something called a comparison operator. Some of which you may have seen before:

|Operator|What it means|Example|Result|
|---|---|---|---|
|`<`|Less than|`5 < 10`|`true`|
|`>`|Greater than|`10 > 5`|`true`|
|`<=`|Less than or equal to|`7 <= 7`|`true`|
|`>=`|Greater than or equal to|`8 >= 10`|`false`|
|`===`|Equal to|`3 === 3`|`true`|
|`!==`|Not equal to|`4 !== 5`|`true`|

We can use these symbols inside our If Statement to compare 2 or more values and then make a decision.

___

### How to write an If Statement

A basic if statement is written like so:

```js
if (condition) {
  // Do something if the condition is true
}
```

Inside the brackets () is where we put the thing our decision is being made on. So we could put (4 < 5) which would check if 4 is less than 5 which is true so then the code inside the curly brackets {} would be run. Notice the code block that gets run is indented (meaning there are some spaces before the code) this is so we can easily see that the code is apart of this function. Not doing this will not stop your code working but it is **HIGHLY** recommended you do it to make your life easier, and if you don't I will know through the universe and be upset.

We can make more complex if statements to handle more decisions. We can add an `else` clause which handles the scenario where none of the conditions are true. For example:

If we wanted to check test scores we could program:
```js
const score = 45

if (score > 50) {
	console.log("You Passed")
} else {
	console.log("You Failed")
}
```

This code takes the variable `score` which holds our test score and first checks if it is greater than 50 if it is we will console log "You Passed". However, if our score is not above 50 like it is in this example then we console log "You Failed".

We can make this even more complex by adding an `else if` clause. We can add as many `else if` clauses as we want but bear in mind the more we add the more complex our code gets.  `else if` clauses go between the `if` and `else` clauses the work the same as the `if` and allow us to check other conditions like so:

```js
const score = 45

if (score >= 90) {
	console.log("A");
} else if (score >= 80) {
	console.log("B");
} else if (score >= 70) {
	console.log("C");
} else {
	console.log("You Failed : (");
}
```

Here we are able to check multiple conditions for different grades, the program will work down the list checking each if it matches then it will run that code block if not it will use the else statement.

___

### Logical Operators

Sometimes, you want to check **more than one thing** at the same time in an `if` statement.

That’s where **logical operators** come in—they let you combine conditions to create more powerful checks.

| Operator | Name | What it Does                                   | Example                                |
| -------- | ---- | ---------------------------------------------- | -------------------------------------- |
| `&&`     | AND  | True **only if both** conditions are true      | `age > 13 && age < 18`                 |
| \|\|     | OR   | True if either one or both conditions are true | day == "saturday" \|\| day == "sunday" |
| `!`      | NOT  | Flips true to false, or false to true          | `!isLoggedIn`                          |

For example on a log in page we could check the username and password like so:

```js
if (username === "Wizard1007" && password === "MyMagicalHat") {
	console.log("Logged In")
} else {
	console.log("wrong username and password")
}
```
