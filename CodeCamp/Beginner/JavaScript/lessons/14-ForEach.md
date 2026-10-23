## forEach Loops

`forEach` is a cleaner way to loop through an array when you don't need to track the index yourself.

```js
const fruits = ["apple", "banana", "cherry"];

fruits.forEach(function(fruit) {
  console.log(fruit);
});
```

Output:
```
apple
banana
cherry
```

The function inside `forEach` runs once for **each item** in the array. The parameter (`fruit`) automatically takes the value of the current item.

---

### forEach vs For Loop

Both do the same thing, but `forEach` is often easier to read:

```js
// For loop version
for (let i = 0; i < fruits.length; i++) {
  console.log(fruits[i]);
}

// forEach version
fruits.forEach(function(fruit) {
  console.log(fruit);
});
```

Use `forEach` when you just need to do something with each item. Use a regular `for` loop when you need the index or want to break out early.

---

### forEach with Index

If you do need the index, `forEach` provides it as a second parameter:

```js
const colours = ["red", "green", "blue"];

colours.forEach(function(colour, index) {
  console.log(index + ": " + colour);
});
```

Output:
```
0: red
1: green
2: blue
```
