// === 15 - forEach Tasks ===

// Task 1: Log Each Item
const animals = ["cat", "dog", "rabbit", "parrot", "hamster"];
animals.forEach(function(animal) {
  console.log(animal);
});

// Task 2: Multiply Each Number
const numbers = [2, 4, 6, 8, 10];
numbers.forEach(function(num) {
  console.log(num * 3);
});

// Task 3: Numbered List
const foods = ["Pizza", "Tacos", "Ice cream"];
foods.forEach(function(food, index) {
  console.log((index + 1) + ". " + food);
});
