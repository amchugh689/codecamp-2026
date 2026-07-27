/*
In JavaScript, we're able to add variables into strings more easily by using the following structure:

let name = 'Dave'
console.log(`Hello, ${name}!`) // This will print "Hello, Dave!"

Note that you must use backticks for this to work.

Using this and the previous tutorials, complete the following tasks:

1. Write a function that prints "Hello World" into the console.
2. Write a function that takes in two number parameters and adds them, printing the result in the console. You can use variables for the parameter.
3. Write a function that takes in a person's name and age, and print these in the console in the format "Your name is (name) and you are (age) years old".
4. Write a function that returns the area of a circle, and use this value in another function that prints the area.
*/

function printHello() {
    console.log("Hello World")
}

printHello();

function printSum(a,b) {
    console.log(a+b)
}

printSum(1,3);

function greetUser(name, age) {
    console.log(`Your name is ${name} and you are ${age} years old.`);
}

greetUser('Dave', 19)

const pi = 3.14
function circleArea(radius) {
    return pi * (radius*radius);
}

function printCircleArea(radius) {
    console.log(circleArea(radius))
}

printCircleArea(8);