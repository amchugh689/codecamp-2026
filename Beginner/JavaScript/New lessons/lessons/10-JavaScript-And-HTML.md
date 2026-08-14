## JavaScript and HTML

Now we'll combine everything. JavaScript can work with HTML and CSS to do powerful things — change text, update styles, and make elements interactive.

---

### Adding JavaScript to HTML

There are two ways:

**Inline:** write JavaScript directly in the HTML using `<script>` tags:

```html
<script>
  console.log("Hello!");
</script>
```

This is fine for small projects but gets messy in larger ones.

**External:** write JavaScript in a separate `.js` file and link it:

```html
<script src="script.js"></script>
```

Add this inside the `<head>` or just before the closing `</body>` tag. This keeps your code organised - we'll use this approach.

