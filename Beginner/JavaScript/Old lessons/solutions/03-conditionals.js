/* 
Using the conditional operators tutorial, complete the following tasks:

1. Create a variable containing the name of a colour on a traffic light 
2. Using this variable, write an if-else statement that checks the colour of the light, and prints what it means. Include a check to ensure it always prints something, regardless of input.
3. Create a variable that contains the place of an Olympian in the finals of their sport.
4. Using the switch keyword, check the variable and print what medal they get, if any. 

*/

let trafficLight = 'yellow';

if(trafficLight === 'red') {
    console.log("Stop!")
} else if (trafficLight === 'yellow') {
    console.log('Slow down, or get ready.')
} else if (trafficLight === 'green') {
    console.log("Go!")
} else {
    console.log("That isn't a traffic light colour")
}


let olympianPos = 3;

switch(olympianPos) {
    case 1: console.log('gold'); break;
    case 2: console.log('silver'); break;
    case 3: console.log('bronze'); break;
    default: console.log('no medal'); break;
}