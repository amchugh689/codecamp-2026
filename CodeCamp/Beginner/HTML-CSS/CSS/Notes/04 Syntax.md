## General CSS Syntax
___
The syntax (structure) of CSS follows a simple structure consisting of a **selector** and a **declaration block**. For example:

- The **selector** points to the HTML element you want to style.
- The **declaration block** contains one or more **declarations**, separated by a semicolon (`;`).
- Each **declaration** must include a **property** and **value** pair, separated by a colon (`:`).

## So what does this look like in practice?

```css
p {
    color: blue;
    font-size: 18px;
}

title {
    color: red;
    font-size: 25px;
}
```
Let's break this down this code example together:

- **Selector:** `p`  (Targets all `<p>` (paragraph) elements.)

- **Declarations:** `{ color: blue; font-size: 18px; }`  
    - `color: blue;`
        - **Property:** `color`
        - **Value:** `blue`
    - `font-size: 18px;`
        - **Property:** `font-size`
        - **Value:** 18px