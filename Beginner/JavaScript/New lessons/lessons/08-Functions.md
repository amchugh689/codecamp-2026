## Functions

A **function** is a reusable block of code that performs a specific task. Instead of writing the same code over and over, you wrap it in a function and call it whenever you need it.

```js
function sayHello() {
  console.log("Hello!");
}
```

To create a function: use the `function` keyword, give it a name, add brackets `()`, then put your code inside `{}`. The code inside should be **indented**.

To **call** (run) the function:

```js
sayHello();
```

This outputs `"Hello!"` to the console.

---

### Functions with Parameters

Parameters are inputs that make your function flexible:

```js
function sayHello(name) {
  console.log("Hello, " + name + "!");
}
```

Now you can pass different values when you call it:

```js
sayHello("Emma");
sayHello("Lucas");
```

Output:
```
Hello, Emma!
Hello, Lucas!
```

---

### Returning Values

Not every function prints to the console. Sometimes you need it to **return** a value so you can use it elsewhere:

```js
function square(number) {
  const squaredNum = number * number;
  return squaredNum;
}

let result = square(4);
console.log(result); // 16
```

The `return` keyword sends a value back to wherever the function was called. Here, `square(4)` returns `16`, which gets stored in `result`.
