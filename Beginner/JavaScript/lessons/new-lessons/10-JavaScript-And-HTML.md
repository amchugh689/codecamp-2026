Now we are going to combine everything we have learnt so far. JavaScript can be combined with HTML and CSS to do some really cool stuff. Like change the text on our webpage, change the style of elements and make elements interactive.

___

### How to add JavaScript to HTML

There are 2 ways to add JavaScript to HTML:
- Inline JavaScript
- External JavaScript

**Inline JavaScript**

This is where we write our JavaScript within the HTML file using script tags that look like so `<script></script>` and we write the JavaScript code between these tags.

This is fine if you are making a small project without much JavaScript. But in larger projects this can become messy and make your project harder to navigate.

**External JavaScript**

This where the JavaScript we write is in a separate external file. That we then link to the HTML file. This keeps our code clean and easily maintainable. This is the option we are going to use.

To link a JavaScript file we also need to use script tags like so:
```html
<script src='script.js'></script>
```

We add this between the `<head>` or `<body>` tags of the HTML file we want to link it to.

