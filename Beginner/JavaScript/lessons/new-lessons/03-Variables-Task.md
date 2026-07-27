In JavaScript we can use `console.log()` to display things in browsers console. This is handy if we are trying to fix something that is broken we can console.log the values of variables to see if they are as we expect. But in this exercise we are going to use it learn how variables work!!

___
### Task 1: Hello There

Lets create our first console.log, on the first line of the JavaScript file we are going to want to write:
```js
console.log("Hello There")
```

Then to run this in the "output" window of CodeHS on the Left there is a green "Run" button at the top. If you click that you should see "Hello There" appear. If that works congratulations you have just written some code!!

This may not seem like a very useful program at the moment but these are all fundamental skills in programming.

___

### Task 2: Make a Variable

Now we are going to create a variable, if you cast your mind back to the intro you will remember there are 2 ways to create a variable. Using `let` and `const` if you can remember the difference you get +100 imaginary bonus points.

Lets make a variable called `age` this variable is going to store our... you guessed it age. Because our age is not going to change while this program is running we are going to use `const`. So to define a variable we to use the `const` keyword followed by the name we want the variable to have and then an equals sign (=) and then the value we want it to hold. Like so:

```js
const age = 291;
```

Feel free to add your own age in, mine is 291 because the person writing this is an intergalactic hero. 

Now on your own create another variable called `name`, that is going to store your name. Just as a little hint your name is going to need to be a string so the value you give will need to be surrounded by speech marks ("").

___
### Task 3: Logging a Variable

Now we have 2 variables defined `name` and `age` we can use our console.log to display the value of these variables in the console window.

So if you take a new line underneath your 2 variables like so:

```js
const name = "Rocky";
const age = 291;

console.log("Hi, my name is " + name + " and I am " + age + " Earth years old")
```

And if you hit the green run button you should see that the value of the variables is printed inside the string text we are logging. This is really cool as we could log any name or age if we change the value of the variable. 

___
### Task 4: Let's do some Maths

Take a few lines below the code you have just written and create a new constant variable (using the `const` keyword) and give it the name "pi" and a value of 3.14.

Now create another constant variable called "diameter" and give it a value of 5. Now what we are doing to do is find the circumference of our imaginary circle and store that value in a variable called 'circumference' and display it to the console.

You will be left to your own devices for this but I will give you a few hints:
- To calculate the circumference the equation is pi x diameter
- The result you get should be 15.7
- The symbol to multiply is *




