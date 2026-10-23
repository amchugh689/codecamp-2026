## Styling by ID
___
The ID selector uses the id attribute of an HTML element to select a specific element. The ID must be unique within a HTML page and uses # followed by the ID of an element as the selector.

For instance, say in your HTML page you only want to apply a certain style to some of the elements.

HTML:
```html
<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" href="styles.css">
    </head>
    <body>
        <h1 id="makeItRed">The heading is affected by the style</h1>
        <p>This paragraph is not affected by the style</p>
    </body>
</html>
```

CSS:
```css
#makeItRed {
    color: red;
}

```

Useful Tip!
With CSS, selecting by ID can be very helpful when building dynamic web pages or automated web-based application testing!

**Dynamic web pages:** Dynamic web pages are those that can change their content or appearance based on user interactions, data input, or other factors. Selecting elements by ID in CSS can help make these changes more controlled and specific.

**Automated web-based application testing:** Automated testing involves using software to automatically test a web-based application. Selecting elements by ID can be helpful in this context because it allows testers to target specific elements on a web page for validation or interaction.

