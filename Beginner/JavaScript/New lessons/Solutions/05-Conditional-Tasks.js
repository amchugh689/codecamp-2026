// === 05 - Conditional Statements Tasks ===

// Task 1: Traffic Lights
const lightColour = "red";

if (lightColour === "red") {
  console.log("Stop");
} else if (lightColour === "orange") {
  console.log("Get ready");
} else if (lightColour === "green") {
  console.log("Go");
} else {
  console.log("Invalid colour");
}

// Task 2: Temperature Check
const temperature = 22;

if (temperature > 30) {
  console.log("It's hot");
} else if (temperature >= 15) {
  console.log("Nice weather");
} else {
  console.log("Bring a jacket");
}

// Task 3: Quiz Score
const correctAnswers = 8;
const totalQuestions = 10;
const percentage = (correctAnswers / totalQuestions) * 100;

if (percentage >= 90) {
  console.log("Excellent!");
} else if (percentage >= 70) {
  console.log("Good job!");
} else {
  console.log("Keep practicing!");
}
