___
## Query Selectors

The `querySelector` and `querySelectorAll` methods provide more flexibility and power, allowing you to use CSS selectors to find elements.

- `querySelector` returns the first element that matches the specified selector
- `querySelectorAll` returns a list of all elements that match the specified selector

### Example using querySelector

Before:
```html
<p class="example">Hello!</p>
<p class="example">Para 2</p>
<p class="example">Para 3</p>
```

```js
let element = document.querySelector(".example");
element.style.color = "red";
```

After:
```html
<p class="example" style="color: red;">Hello!</p>
<p class="example">Para 2</p>
<p class="example">Para 3</p>
```

In this example:
- The `querySelector` method is used to access the first element with the class `example`.
- The colour of text is changed to red

### Example using querySelectorAll

Before:
```html
<p class="example">Hello!</p>
<p class="example">Para 2</p>
<p class="example">Para 3</p>
```

```js
let elements = document.querySelectorAll(".example");

elements.forEach(function(element) {
    element.style.color = "blue";
});
```

After:
```html
<p class="example" style="color: blue;">Hello!</p>
<p class="example" style="color: blue;">Para 2</p>
<p class="example" style="color: blue;">Para 3</p>
```

In this example:
- The `querySelectorAll` method is used to access all elements with the class `example`.
- The color of the text for each element is changed to blue using the [`forEach`](https://www.w3schools.com/jsref/jsref_foreach.asp) method.
