## Elements
JavaScript can interact with HTML and manipulate its elements in various ways. To do this, JavaScript provides several methods to access elements by their ID, class, tag name, name attribute, or other selectors. This capability is central to making web pages dynamic and interactive.

### Accessing Elements by ID

The `getElementById` method is used to access a single element with a specified ID. Since IDs are unique within a page, this method will return a single element.

Before:
```html
<p id="demo">Hello!</p>
```

```js
let element = document.getElementById("demo");
element.innerHTML = "Hello, this text has been changed!";
```

After:
```html
<p id="demo">Hello, this text has been changed!</p>
```

In this example:
- The getElementById method is used to access the p element with the ID demo.
- The innerHTML property is used to change the text inside the p element.

### Accessing Elements by Class Name

The `getElementsByClassName` method returns a collection of all elements with the specified class name. This collection is an array-like object.

Before:
```html
<p class="myClass">Hello!</p>
<p class="myClass">Para 2</p>
<p class="myClass">Para 3</p>
```

```js
let elements = document.getElementsByClassName("myClass");

for (let i = 0; i < elements.length; i++) {
    elements[i].innerHTML = "Hello, this text has been changed!";
}
```

After:
```html
<p class="myClass">Hello, this text has been changed!</p>
<p class="myClass">Hello, this text has been changed!</p>
<p class="myClass">Hello, this text has been changed!</p>
```

In this example:
- The `getElementsByClassName` method is used to access all `<p>` elements with the class `myClass`.
- The innerHTML property is used to change the text inside the p element.

### Accessing Elements by Tag Name

The `getElementsByTagName` method returns a collection of all elements with the specified tag name.

Before:
```html
<p class="myClass">Hello!</p>
<p class="class2">Para 2</p>
<p id="demo">Para 3</p>
```

```js
let elements = document.getElementsByTagName("p");

for (let i = 0; i < elements.length; i++) {
    elements[i].innerHTML = "Hello, this text has been changed!";
}
```

After:
```html
<p class="myClass">Hello, this text has been changed!</p>
<p class="class2">Hello, this text has been changed!</p>
<p id="demo">Hello, this text has been changed!</p>
```

In this example:
- The `getElementsByTagName` method is used to access all p elements.
- A loop iterates through the collection and changes the text of each element.

### Accessing Elements by Name

The `getElementsByName` method returns a collection of elements with the specified name attribute. This is often used with form elements.

```html
<input type="text" id="demo-input" name="myInput">
```
```js
let elements = document.getElementsByName("myInput");
alert(elements[0].value);
```

In this example:
- The `getElementsByName` method is used to access the input element with the name `myInput`.
- The value of the input element is displayed in an alert box.
