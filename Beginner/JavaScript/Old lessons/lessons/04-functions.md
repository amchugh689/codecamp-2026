## What is a JavaScript function?

A function is a block of code designed to perform a particular task and is executed when something calls it. Let's look at the syntax of a function:

```js
function myFunctionName(parameter){
    // code to be executed
}
```

A JavaScript function is defined with the function keyword, followed by the name of your function, followed by parentheses ().

The parentheses may contain parameters (ie, something in the brackets), but it is not essential (depends on what your function is doing).

The code to be executed (the logic for what your function is meant to do) is placed inside curly brackets {}.

Functions are called by writing the name of the function followed by brackets i.e myFunctionName();

Remember if a function has parameters, they must be passed into the function when called i.e myFunctionName(parameter);

Why Use Functions?

- Reusability: Write once, use multiple times.
- Maintainability: Easier to manage and update code.
- Modularity: Break your code into smaller, manageable pieces.

___
## Return

Sometimes, we don't want the function to print something, but instead we want it to give us back a value. To do this, we use the return keyword.

```js
function rectangleArea(width, height) {
    let area = width * height;
    return area;
}

console.log(rectangleArea(3,5)) // This will print 15
```

## Example:

Here is an example of a function that adds two numbers:

```js
function addNumbers(a, b) {
    return a + b;
}

let sum = addNumbers(5, 10);
console.log(sum); // Outputs: 15
```
