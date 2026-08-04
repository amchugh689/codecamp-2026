## Query Selectors & DOM — Tasks

These tasks combine query selectors, loops, and styling. You'll need an HTML file with some elements to work with.

---

### Task 1: Change a Heading

Create an HTML file with a `<h1>` that has the ID `"title"`. In your JavaScript file, use `querySelector` to select it and change its text to something else.

---

### Task 2: Style a Button on Click

Add a `<button>` to your HTML. When clicked, use JavaScript to change the button's background colour.

**Hint:** Use `onclick` and `element.style.backgroundColor = "colour"`.

---

### Task 3: Restyle All Paragraphs

Add at least 4 `<p>` elements to your page, all with the class `"info"`.

Use `querySelectorAll` and `forEach` to loop through them and change their text colour to blue and font size to 20px.

---

### Task 4: Highlight on Click

Add 5 `<li>` elements inside a `<ul>`. Add a button that, when clicked, uses `querySelectorAll` to select all the `<li>` elements and gives them a yellow background.

---

### Stretch Task: Toggle Styles

Add a button that **toggles** the style of all `.info` paragraphs — first click makes them red, second click makes them black again.

**Hint:** You could use a global boolean variable to track the current state.
