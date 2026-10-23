## More `<Body>` Elements
___
### Paragraph Tags
The next tag we will focus on is the, `<p>` tag.
This tag is used to define a, 'paragraph', and works similarly to the `<h>` tag to display content to our webpage.

```html
<p> I am a paragraph </p>
```
___

### Link Tags
The `<a>` tag defines a hyperlink, which is used to link from one web page to another.

This tag also contains additional attributes, most importantly, the **href attribute** which indicates the link’s destination.
Once the link has been provided, any text placed between the `<a>` tags will be the text displayed to the user as a clickable link.
It will display similarly to how it does when we use the `<p>` tags.

`<a>`  tags can be used to :
Link to external sites, provided via a URL.
```html
<a href="https://www.kainos.com/"> Link text to display </a>
```

Or it can be used to link your html pages. To do this specify the name of your page rather than a URL. This will search the local directory for your page so make sure that your page is in the same directory.
```html
<a href="example.html"> Link text to display </a>
```

___
### Image Tags
The `<img>` tags can be used to add images to your webpage.
Similarly to the link tags, image tags also require additional attributes:
- **src:** This attribute specifies the source/location of the image
- **alt:** This attribute specifies any alternative text to display in place of the image, should the browser have issues loading the image.

Note: the source of the images can be either an external site, or from within your project folder. The `src` attribute works similarly to the `href` attribute we learnt about above!
```html
 <img src="KainosLogo.jpg" alt="Logo for Kainos Software">
```
