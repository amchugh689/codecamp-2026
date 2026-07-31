___
### **What Are Variables in JavaScript?**

Imagine a **variable** like a **box** where you can store something—like a number, a word, or even a list of things. You give the box a name so you can use it later.

In JavaScript, variables are used to **store data** that your code can use and change.

For example:
```js
let score = 10;
```

Here, we’ve created a variable called `score` and put the number `10` inside it.

### **Why Are Variables Useful?**

Variables let your programs **remember** things. You can use them to:

- Keep track of a score in a game
- Store a user’s name after they enter it
- Hold the result of a calculation
- Count how many times a button is clicked

___
### Data Types

When we are working with variables it is important to know that the data they are storing can be different types. In JavaScript we can have:

- **Numbers**: Used for anything with math—whole numbers or decimals.
- **Strings**: A string is a **piece of text**. It must be in quotes.
- **Booleans**: A boolean is either **true** or **false**.
- **Arrays**: An array is a **list** of values stored in one variable.
- **Objects**: An object is a way to store a group of related information.

#### Why is it Important we Know what type our data is?

This is important because different data types act differently. So we need to know what we are working with so we can handle it properly or our code might break or do something weird. Some examples of how different types work differently are:

- You **add** numbers.
- You **combine** strings.
- You **check** booleans.
- You **loop through** arrays.
- You **organise info** with objects.

If we tried to add 2 strings like "4" and "5", we would not get "9" we would get "45" because JavaScript combines strings it does not add them.

___
### **How Do You Create a Variable?**

You use the word `let` or `const`, then give it a name:
```js
let name = "Alex";
const pi = 3.14;
```

There is a difference between using `let` and `const`:
- Use `let` when the value might **change** later.
- Use `const` when the value should **stay the same**.

___

### Mathematical Operators

In JavaScript, you can use variables to **do math** just like on a calculator. These are called **mathematical operators**, and they let your code add, subtract, multiply, divide, and more.

If you’ve used a calculator or done algebra, this will feel familiar!

**Basic Math Operators**

| Operator | What it does        | Example  | Result |
| -------- | ------------------- | -------- | ------ |
| `+`      | Addition            | `5 + 3`  | `8`    |
| `-`      | Subtraction         | `10 - 4` | `6`    |
| `*`      | Multiplication      | `6 * 2`  | `12`   |
| `/`      | Division            | `12 / 3` | `4`    |
| `%`      | Modulus (Remainder) | `10 % 3` | `1`    |
___

In the next section we are going **FINALLY** start programming but everything we have just covered is a very important first step.