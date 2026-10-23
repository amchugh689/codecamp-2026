## While Loops

A `while` loop repeats code **as long as a condition is true**. Unlike a for loop (where you know how many times to repeat), a while loop is useful when you don't know in advance how many iterations you need.

```js
let count = 0;

while (count < 5) {
  console.log(count);
  count++;
}
```

This outputs `0, 1, 2, 3, 4`. Each time the loop runs, it checks if `count < 5`. When that becomes false, the loop stops.

---

### Be Careful: Infinite Loops

If the condition **never** becomes false, the loop runs forever and crashes your browser. Always make sure something inside the loop changes the condition:

```js
// BAD — this runs forever!
let x = 1;
while (x > 0) {
  console.log(x);
}

// GOOD — x eventually reaches 0
let x = 5;
while (x > 0) {
  console.log(x);
  x--;
}
```

---

### When to Use While vs For

| Use a **for** loop when... | Use a **while** loop when... |
| --- | --- |
| You know how many times to repeat | You don't know how many times |
| Counting through a range | Waiting for a condition to change |
| Looping through an array by index | Repeating until user input is valid |
