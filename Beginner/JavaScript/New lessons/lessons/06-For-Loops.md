## For Loops

A for loop lets you repeat code multiple times without writing it out over and over.

```js
for (let i = 0; i < 5; i++) {
  console.log("Hello!");
}
```

Breaking this down:

- `for` — the keyword that starts the loop.
- `let i = 0` — where the count starts (the **initialiser**).
- `i < 5` — the loop keeps running while this condition is true.
- `i++` — adds 1 to `i` after each loop. (You could use `i += 2` to count in twos.)
- `{}` — the code inside the curly brackets runs each time the loop repeats. Keep it **indented** for readability.
