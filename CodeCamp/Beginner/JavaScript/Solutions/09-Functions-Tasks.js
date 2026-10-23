// === 09 - Functions Tasks ===

// Task 1: Name and Age
function displayInfo(name, age) {
  console.log("Your name is " + name + " and you are " + age + " years old");
}
displayInfo("Alex", 16);

// Task 2: Adding Two Numbers
function add2Numbers(num1, num2) {
  return num1 + num2;
}
console.log(add2Numbers(3, 7)); // 10

// Task 3: Circle Circumference
function calculateCircumference(diameter) {
  const pi = 3.14;
  return pi * diameter;
}
console.log(calculateCircumference(5)); // 15.7
