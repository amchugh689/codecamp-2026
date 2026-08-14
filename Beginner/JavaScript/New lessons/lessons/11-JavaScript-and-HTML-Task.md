## JavaScript and HTML - Tasks

### Task 1: Linking JavaScript to HTML

We have some starter code: a restaurant website with three files (`index.html`, `style.css`, `script.js`).

To link the JavaScript file, open `index.html` and find the comment that says `"Where to add in Script Tag"`. Below it, add:

```html
<script src="script.js"></script>
```

The `src` attribute tells the browser which file to load. If your JS file is in a different folder, you'll need to include the path (e.g. `src="js/script.js"`).

---

### Global vs Local Variables

Variables have **scope** - where they can be accessed from:

- **Global** variables are created outside any function and can be used anywhere in the file.
- **Local** variables are created inside a function and only exist within that function.

```js
const globalVar = "I'm accessible everywhere";

function myFunction() {
  const localVar = "I only exist inside this function";
}
```

Using local variables when possible makes code less confusing and easier to debug.

---

### Task 2: Table Counter

We'll add a table availability checker. Steps:

1. Create a **global** variable for the total number of tables.
2. Create a **global** variable for the number of booked tables.
3. Create a function that checks if there are free tables.
4. Display the result on the page.

#### Calling a Function from HTML

Add an `onclick` attribute to the button below the `<h4 id="availability-counter">` element:

```html
<button onclick="checkAvailability()">Check Availability</button>
```

When clicked, this runs your `checkAvailability` function.

#### Selecting and Updating an Element

Use `document.getElementById()` to grab an HTML element by its `id`:

```js
let counterElement = document.getElementById("availability-counter");
```

Then update its text using `.innerHTML`:

```js
counterElement.innerHTML = "Tables available: 5";
```

Use a variable instead of hardcoded text to show the calculated result.

> **Note:** Other ways to select elements include `getElementsByClassName`, `getElementsByTagName`, and `querySelector`.

---

### Task 3: Book a Table

Allow a user to book a table. Steps:

1. Create a new function (triggered by the Book Now button).
2. Collect the values the user entered in the form.
3. Store them in an **object**.
4. Add that object to a **global array**.
5. Show a confirmation (an `alert()` or update an HTML element).

#### Getting Input Values

Use `getElementById` with `.value` to read what the user typed:

```js
let email = document.getElementById("email").value;
```

#### Creating an Object

Objects store multiple related values in one variable:

```js
let booking = { firstName: fname, lastName: lname, email: email, date: date };
```

Each value has a name (key) followed by a colon and the data.

#### Creating and Adding to an Array

```js
const bookings = [];

bookings.push(booking);
```

`.push()` adds a new item to the end of the array.

---

### Task 4: Search for a Booking

Add the ability to search for a booking by email. Steps:

1. Create a new function (triggered by the Find Booking button).
2. Get the email the user entered.
3. Loop through the bookings array and find a match.
4. Display the booking details (or "Not Found").

#### Accessing Array Elements

Arrays are zero-indexed — the first item is at position `0`:

```js
const myArray = ["cat", "dog", "parrot", "cow"];
console.log(myArray[0]); // "cat"
console.log(myArray[1]); // "dog"
```

#### Searching an Array

Combine a for loop with an if statement. Use `.length` to loop through every element:

```js
let found = false;

for (let i = 0; i < bookings.length; i++) {
  if (bookings[i].email === userEmail) {
    console.log(bookings[i]);
    found = true;
  }
}

if (!found) {
  console.log("Not Found");
}
```

Each time the loop runs, it checks the next booking's `.email` property against what the user entered. If there's a match, it logs the booking and sets `found` to `true`. After the loop, if `found` is still `false`, nothing matched.

Display the result on the page instead of just using `console.log` for a better user experience.
