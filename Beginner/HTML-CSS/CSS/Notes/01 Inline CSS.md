## Inline CSS
___
Inline CSS changes the style property of the tag directly using the style attribute. This way is not recommended as this can become repetitive if you plan on reusing the same structuring for several tags.

For instance, if you want to change the font size of just one of the <p> tags, then you can specify that like this:

```html
<body>
    <p>I am the same size as before</p>
    <p style="font-size: 30px">My font size has increased</p>
</body>
```

You can also apply more than one style property to an element, but in doing so it can be tricky to read as it can become very long...

Here’s an example:

```html
<body>
    <p>I am the same size as before</p>
    <p style="font-size: 30px; color: red; font-family: 'Courier New', Courier, monospace; text-decoration: line-through;">My font size has increased</p>
</body>
```

This is why we recommend using internal or external style sheets instead!