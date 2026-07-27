## What is a variable?

A variable is a named item that can store data. It can be used elsewhere in your code, which is handy as it can save time and prevent mistakes in entering the same value multiple times.

### What types of Variables are there?

JavaScript is a *weakly-typed* language, meaning you don't need to define the type of a variable when you make it. However, within JavaScript, there are 7 main, or **primitive** types, the most common of which are:

- **String:** A group of characters. These can be letters, numbers, symbols or a mix of all.
- **Number:** Any number, positive or negative, whole or with a decimal point.
- **Boolean:** A true or false value.
- **Undefined:** A type that represents the absence of a value, and can only contain 'undefined'.

## How do I use a variable?

In JavaScript, you can create a variable in a few different ways:

**1. var:** If you want the variable to be accessable from outside the block it was defined in, the **var** keyword is used.

```js
var name = "Dave"; // String
var age = 15; // Number
var isAtCodeCamp = true; // Boolean
var temp; // Undefined
```

**2. let:** If you want the variable to only be accessable from within the block it was defined in, the **let** keyword is used.

```js
let name = "Dave"; // String
let age = 15; // Number
let isAtCodeCamp = true; // Boolean
let temp; // Undefined
```

**3. const:** If you want to make a variable with a value that cannot be changed, the **const** keyword is used.

```js
const name = "Dave"; // String

name = "steve" // This will throw an error as you cannot change a const's value
```

___
## Mathematical Operators

In JavaScript, you can use a variety of operators to perform actions on number variables.

1. **Add:** +
2. **Subtract:** -
3. **Multiply:** *
4. **Divide:** /
5. **Remainder:** %

You can also use ++, --, += and -= to change a variable's value.

```js
let a = 1;
let b = 2;
console.log(a+b); // This will print 3

a++; // This increases the value of a by 1

b += 10; // Shorthand for 'b = b + 10'

let c = a * b; // This creates a new variable which is equal to the product of a and b

console.log(b / a) // This will print '6'

console.log(b % 4) // This will print '0', as 12/4 has no remainder
```

## String Operators

You can also use operators on string variables. The **+** operator can be used to join multiple strings together. This is called **concatenation**.

```js
let a = 'He';
let b = 'llo';
console.log(a+b); //This will print 'Hello'
```
