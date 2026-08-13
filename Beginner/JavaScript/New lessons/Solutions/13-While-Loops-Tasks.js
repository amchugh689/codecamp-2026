// === 13 - While Loops Tasks ===

// Task 1: Countdown
let countdown = 10;
while (countdown >= 1) {
  console.log(countdown);
  countdown--;
}
console.log("Liftoff!");

// Task 2: Double Until 100
let num = 1;
while (num <= 100) {
  console.log(num);
  num = num * 2;
}

// Task 3: Guess the Number
const secretNumber = 7;
let guess = 0;
while (guess !== secretNumber) {
  guess++;
  console.log("Guessing: " + guess);
}
console.log("Got it!");
