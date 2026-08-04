## External Style Sheets
___
The recommended way of applying CSS to multiple elements and files is to use a separate CSS file which contains all the styling rules you wish to apply.

For example, this would change all `<p>` tags to have a font size of 30 pixels if set in the external file.

This example shows you how the `<link>` element works. This tag defines a link between a document and an external resource, and it used to link external style sheets such as CSS.

```html
<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="example.css"/>
    </head>
    <body>
    </body>
</html>
```


The three attributes above are the most common ones which define the <link> tag.
- **rel:** specifies the relationship between the current document and the linked document
- **type:** specifies the media type of the linked document
- **href:** specifies the location of the linked document

## How do we set up our own external style-sheet?
 To set up an external style-sheet for your page, 
 - create a new file such as `example.css` and write your CSS within that file,
 - then use a link in your HTML head to link it to your page, as shown:
 
example.css:
 ```css
 p {
	font-size: 30px;
}
```

HTML: 
```html
<head>
    <link rel="stylesheet" type="text/css" href="example.css"/>
</head>
```
**Remember to update the "href" value to point to the correct stylesheet file!
