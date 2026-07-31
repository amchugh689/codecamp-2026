
What is a function I hear you ask? Well that is a great question - A function is a block of code designed to perform a particular task and is executed when something calls it. Functions prevent us from having to re-write the same functionality over and over again. Instead we wrap it up and a function and call it.

So lets take a look at what a function looks like:

```js
function sayHello() {
  console.log("Hello!");
}
```

To create a function we use the `function` key word, that is then followed by the name of the function. In this case it is called 'sayHello'. Then we have some brackets these are used to pass what are called parameters, which are inputs that allow our function to be more flexible. Then finally we have some curly brackets {} inside of which goes the code that gets run when the function is called. In this example, when sayHello is called "Hello!" is outputted into the console. Similar to For loops and If Statements the code block inside the function is indent - This is important to remember.

To call this function we would do the following;

```js
sayHello();
```

This will then output "Hello!" to the console.

___

### Functions with Parameters

Now let's look at a function with a parameter:

```js
function sayHello(name) {
  console.log("Hello, " + name + "!");
}
```

This is the same function as before but it now has a parameter called `name`. In this function name if a variable that holds a value that we can decide when we call the function. This allows our function to be more flexible as we can alter what it is doing under different scenarios. Such as if we want to say hello to people with different names. Instead of having 1 million functions all that output "hello " and someones name to try cover off every name. We can pass the value of the name when we call it.

This changes slightly how our code looks when we call this function like so:

```js
sayHello("Emma");
sayHello("Lucas");
```

Between the brackets we are now passing the value we want used in our function. This would then output:
```text
Hello Emma!
Hello Lucas!
```

___

### Returning Functions

Not all functions output something to the console. Sometimes we need them to return a value. To do that we need to use the aptly named `return` keyword.

This allows us to return a value from a function back to where we called it from.

For example if we had a function that squared a number that looked like so:
```js
function square(number) {
  const squaredNum = number * number;
  return squaredNum
}

let result = square(4);
console.log(result);
```

Notice in the function `square` we set a variable `squaredNum` and we return that so when when we call the function below the value we return is then set to the variable `result`. We can then use this value in our code, in this case we are just outputting it but we could do some more operations if we wanted. 
