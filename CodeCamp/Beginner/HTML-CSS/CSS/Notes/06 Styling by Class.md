## Styling by Class
___
Similar to ID, you can also use the **class selector** to select HTML elements with specific class attributes.

To select a class use ‘.’ Followed by the name of the class. 
You can also specify which tags within a class to apply the styling to:

HTML:
```html
<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" href="styles.css">
    </head>
    <body>
        <h1>The heading is not affected by the style</h1>
        <p class="center">This paragraph is affected by the Class selector style </p>
        <p>This paragraph is not affected by the style</p>
    </body>
</html>
```


CSS:
```css
.center {
    text-align: center;
    color: red;
}

p.center {
     text-align: center;
     color: red;
}
```
 
Useful Tip!
HTML elements can have more than one class, for example: 
```html
<p class="center large">This paragraph refers to two classes.</p>
```

You can also use frameworks such as Bootstrap (https://getbootstrap.com/) which already has specific styling rules applied which you can also link to your HTML page!

```html
<head>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css">
</head>
```

The code above shows how we can create this `<link >` to an external style sheet, stored online. Which then applies those style changes our our HTML page.