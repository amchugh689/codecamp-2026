## Conditional Statements

In real life we make decisions all the time. Programming is the same — our code often needs to choose what to do based on different conditions.

We do this with an **If Statement**. For example, on a login page we check **if** the password matches. If it does, we let the user in. Otherwise, we show an error.

---

### Comparison Operators

To compare values, we use comparison operators:

|Operator|Meaning|Example|Result|
|---|---|---|---|
|`<`|Less than|`5 < 10`|`true`|
|`>`|Greater than|`10 > 5`|`true`|
|`<=`|Less than or equal to|`7 <= 7`|`true`|
|`>=`|Greater than or equal to|`8 >= 10`|`false`|
|`===`|Equal to|`3 === 3`|`true`|
|`!==`|Not equal to|`4 !== 5`|`true`|

---

### Writing an If Statement

```js
if (condition) {
  // runs if the condition is true
}
```

The condition goes inside `()`. If it's true, the code inside `{}` runs. The code block should be **indented** (spaced in) so it's easy to see what belongs to the if statement.

#### Adding `else`

`else` handles the case where the condition is false:

```js
const score = 45;

if (score > 50) {
  console.log("You Passed");
} else {
  console.log("You Failed");
}
```

#### Adding `else if`

Use `else if` to check multiple conditions:

```js
const score = 45;

if (score >= 90) {
  console.log("A");
} else if (score >= 80) {
  console.log("B");
} else if (score >= 70) {
  console.log("C");
} else {
  console.log("You Failed :(");
}
```

The program works down the list. As soon as a condition matches, that code block runs and the rest is skipped.

---

### Logical Operators

Sometimes you need to check **more than one thing** at once. Logical operators let you combine conditions:


| Operator | Name | Meaning | Example |
| -------- | ---- | ------- | ------- |
| `&&`     | AND  | True only if **both** are true | `age > 13 && age < 18` |
| `\|\|`   | OR   | True if **either** is true | `day === "saturday" \|\| day === "sunday"` |
| `!`      | NOT  | Flips true to false (and vice versa) | `!isLoggedIn` |

Example — checking a username **and** password:

```js
if (username === "Wizard1007" && password === "MyMagicalHat") {
  console.log("Logged In");
} else {
  console.log("Wrong username or password");
}
```
