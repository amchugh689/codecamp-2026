## What is a conditional statement?

In real life, we need to make a lot of decisions based on different circumstances. For instance, if you're hungry, you might decide to eat something, and otherwise you wouldn't bother.
We do the same in programming: we need to check different variables and make decisions based on the data provided.

## Comparison Operators

To compare values, we use Comparison Operators:

- Less than: <
- Greater than: >
- Less than or equal to: <=
- Greater than or equal to: >=
- Equal to: ===
- Not equal to: !==

You can use these in your conditional statements to perform a wider range of checks.

## Types of Conditional Statement

### If Statements

The if statement takes an input, and if the resulting value is true, it performs whichever task is inside the statement.

```js
if(true) {
    console.log("Hello!");
}
```

### Else Statements

After an if statement, an else can be added to run code if the original condition is false.

```js
if(true) {
    console.log("Hello!");
} else {
    console.log("Goodbye :(");
}
```

You can also add additional conditions using an else if statement.

```js
let a = 4
let b = 2
if(a === b) {
    console.log("A is equal to B")
} else if (a < b) {
    console.log("A is less than B")
}
else {
    console.log("A is greater than B")
}
```

### Switch

If you need to run a lot of checks on one value, instead of writing loads of if statements, you can use the switch keyword.

```js
let fruit = 'orange';

switch(fruit) {
    case 'apple':
        console.log("Apples are red!");
        break;
    case 'banana':
        console.log("Bananas are yellow!");
        break;
    case 'orange':
        console.log("Oranges are orange!");
        break;
    default:
        console.log("Invalid fruit");
        break;
}

// This will print "Oranges are orange!"
```

___
## Logical operators

Sometimes in code you need to check multiple values; maybe two things need to be true, or only one out of a few, or even that something isn't true. To do this, we use logical operators.

- And: &&
- Or: ||
- Not: !

```js
let a = true;
let b = true;
let c = false;

if(a && b) {
    console.log("Success");
}

if(a || c) {
    console.log("At least one success");
}

if(!c) {
    console.log("C is false")
}
```
