## Why Mouse Input?

Every game in this prep material is controlled entirely from the keyboard. That's fine for a lot of genres, but plenty of game ideas, menus, and buttons need the mouse instead. Reading mouse input works a lot like reading the keyboard: through events, in the same loop where you already check for `pygame.QUIT`.

Mouse events go through that same `pygame.event.get()` loop your keyboard input already uses, so there's nothing extra to set up on CodeHS. If clicks feel laggy or a right-click doesn't behave the way you expect, test that early rather than assuming your code is wrong. Try running the game locally (see `Running PyGame Locally`) to check whether it's a browser-streaming issue or something in your code.

## Detecting a Click

A click shows up as a `pygame.MOUSEBUTTONDOWN` event in your event loop, alongside the `pygame.QUIT` check you already have:

```python
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
    if event.type == pygame.MOUSEBUTTONDOWN:
        print("Clicked at", event.pos)
```

`event.pos` is an `(x, y)` tuple (a list of multiple items stored as one variable) giving the position of the click. It uses the same coordinate system you already use for drawing: `(0, 0)` at the top-left, `x` increasing to the right, `y` increasing downward.

**Quick check**: why check for the click inside the `for event in pygame.event.get()` loop, rather than outside it?

## Was a Button Clicked?

A click on its own is just a position. To know whether it landed on something, like a button or a sprite, use the same `rect` you already use for these, since its `collidepoint()` method checks whether a position falls inside the rect:

```python
if event.type == pygame.MOUSEBUTTONDOWN:
    if button_rect.collidepoint(event.pos):
        print("Button clicked!")
```

It's the same idea as `colliderect()`, which checks whether two rects overlap, just applied to a single point (where your mouse clicked) against one rect instead.

**Quick check**: if `button_rect` and `button_image` exist, how would you check whether the player clicked that button?

## Which Button Was Pressed?

`event.button` tells you which mouse button triggered the event: `1` for left, `2` for middle, `3` for right. Most games only care about the left button:

```python
if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
    ...
```

## Tracking the Mouse Every Frame

Clicks are events: they fire once, the instant the button goes down. Sometimes you want the mouse's position on every frame instead, for example to highlight a button the player is hovering over before they click it. `pygame.mouse.get_pos()` gives you that directly, with no event needed:

```python
mouse_pos = pygame.mouse.get_pos()
hovering = button_rect.collidepoint(mouse_pos)
```

Call it once per frame, outside the event loop, since it always returns the mouse's current position rather than something that happened.

**Quick check**: would you use `MOUSEBUTTONDOWN` or `get_pos()` to make a button glow while the mouse sits over it, without clicking?

## Putting It Together

Here's a button that changes color on hover and prints a message on click, combining everything above. It assumes your game loop already has `running = True` set before it starts, the same way every game in this prep material does:

```python
button_rect = pygame.Rect(300, 250, 200, 60)

# inside the game loop:
mouse_pos = pygame.mouse.get_pos()
hovering = button_rect.collidepoint(mouse_pos)

for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        if button_rect.collidepoint(event.pos):
            print("Button clicked!")

button_color = (200, 200, 0) if hovering else (150, 150, 150)
pygame.draw.rect(window, button_color, button_rect)
```


# Further Information

If you want to learn more about PyGame, check out the documentation here:
https://www.pygame.org/docs/

## Glossary

- **MOUSEBUTTONDOWN**: the event fired the instant a mouse button is pressed
- **event.pos**: the `(x, y)` position of a mouse event
- **collidepoint()**: checks whether a position falls inside a rect
- **get_pos()**: the mouse's current position, read directly rather than from an event
