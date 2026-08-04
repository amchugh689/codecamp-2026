## What exactly is HTML?
___

HTML stands for HyperText Markup Language, and it's what we use to build the structure of a web page.

Contrary to what many may think, HTML is not a programming language.
HTML is a markup language that defines the structure of your content (whats on the page, and how it is organised).

HTML is made up of individual elements, that are combined to form an entire HTML page.
Each element uses tags,

- Elements are defined by their tags (Start and End tags).
- Tags are named with keywords which tell the webpage what to insert.

```html
<tag>
Everything within the tag is content!
</tag>
```

The start tag is written inside < > and is followed by the end tag which is written inside </>
___

### Page Structure
Every HTML page will follow the same structure and contain the following 3 elements:

```html
<!DOCTYPE HTML>
<html>
	<head>
            <!-- Info about the page -->
	</head>
	<body>
            <!-- What people see on the page -->
	</body>
</html>
```

`<!DOCTYPE HTML>`
This is, in fact, a declaration, and not a tag. It is used to let the browser know this is a HTML document.

`<html>`
This element wraps around all the content of the page and contains the head and body elements.

`<head>`
This element acts as a container for anything you wish to include on the html page that is not content. Some examples of what may be included inside the head tag are:
- page title
- a description of the page
- links to external scripts/files
- other metadata (author, charset etc...)

`<body>`
This element contains all the content you wish to display on your webpage, to the end users. For example:
- Text
- Images
- Videos