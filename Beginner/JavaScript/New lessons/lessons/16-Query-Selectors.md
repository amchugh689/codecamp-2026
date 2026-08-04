## Query Selectors

`querySelector` and `querySelectorAll` let you select HTML elements using **CSS selectors** — the same selectors you use in your stylesheets.

---

### querySelector — Select One Element

Returns the **first** element that matches:

```js
let element = document.querySelector(".example");
element.style.color = "red";
```

This finds the first element with class `example` and makes its text red.

You can use any CSS selector:
- `".className"` — select by class
- `"#idName"` — select by ID
- `"p"` — select by tag
- `"div .child"` — select nested elements

---

### querySelectorAll — Select Multiple Elements

Returns **all** matching elements as a list:

```js
let elements = document.querySelectorAll(".example");

elements.forEach(function(element) {
  element.style.color = "blue";
});
```

This makes every element with class `example` blue.

---

### querySelector vs getElementById

| `getElementById` | `querySelector` |
| --- | --- |
| Only selects by ID | Uses any CSS selector |
| Returns one element | Returns first match |
| Slightly faster | More flexible |

Both work well. Use whichever fits your situation — `querySelector` is more versatile, `getElementById` is simpler for IDs.
