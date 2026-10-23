### Div Tags
___
`<div>`, or division, tags are used to divide your webpage up into sections. This is especially useful when attempting to group content together so it can be styles easily using class or id attributes (More on styling later !!)

The `<div>` tag has no effect on the content, or the layout of the content, until CSS has been applied to it.

```html
<!DOCTYPE HTML>
<html>
    <head>
        <style>
            .myDiv{
                /* Style your Div here! */
            }            
        </style>
    </head>
    <body>
        <div class="myDiv">
          <h2>This is a heading in a div element</h2>
          <p>This is some text in a div element.</p>
        </div>
    </body>
</html>
```