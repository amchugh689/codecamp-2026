## The `<Head>` Element
___
As mentioned previously, the `<head>` element can be populated with some useful tags to provide some context and information about our webpage.

### Title Tags
The `<title>` tag can be used within the head element of your site to change the title of the browser tab the webpage is open in.

```html
<!DOCTYPE html>
<html>
    <head>
        <title> My Page Title </title>
    </head>
</html>
```

### Favicons
Favicons are small images displayed to the left of the page title in the browser tab. 
Such as the coloured G icon on this google tab:
![img.png](favicons.png)

Adding a favicon to your webpage follows a similar process to adding any images/links to our page, however, instead of using the `<a>`, or `<img>` tags, we will use a new tag, `<link>`.

`<link>` tags define the relationship between the current document and any external resources you have linked. 

They are most commonly used for linking:
- Stylesheets
- Favicons

Link tags require some additional attributes in order to work:
- **rel:** This is a required attribute and defines the relationship between the current, and linked document
- **type:** This specifies the media type of the linked document
- **href:** This is used to specify the location of the linked document.

Now we have covered link tags, we can add a favicon to our webpage like this:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>My Page Title</title>
        <link rel="icon" type="image/x-icon" href="/images/favicon.ico">
    </head>
</html>
```