## Why Mouse Input?

Every game in this prep material is controlled entirely from the keyboard. That's fine for a lot of genres, but plenty of game ideas, menus, buttons, click-to-place objects, point-and-shoot, need the mouse instead. Reading it works a lot like reading the keyboard: through events, in the same loop you already check for `pygame.QUIT`.

Mouse events use the same `pygame.event.get()` loop your keyboard input already goes through, so there's nothing extra to set up on CodeHS. If clicks feel laggy or a right-click doesn't behave the way you expect, that's worth testing early, try running the game locally (see Lesson 2) to check whether it's the browser streaming or something in your code.

## Detecting a Click

A click shows up as a `pygame.MOUSEBUTTONDOWN` event in your event loop, alongside the `pygame.QUIT` check you already have:

```python
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
    if event.type == pygame.MOUSEBUTTONDOWN:
        print("Clicked at", event.pos)
```

`event.pos` is an `(x, y)` tuple, the position of the click in the same coordinate system you already use for drawing: `(0, 0)` top-left, `x` right, `y` down.

**Quick check**: why check for the click inside the `for event in pygame.event.get()` loop, rather than outside it?

## Was a Button Clicked?

A click on its own is just a position. To know whether it landed on something, like a button or a sprite, reuse the same `pygame.Rect` you already use for sprites and collisions, `collidepoint()` checks whether a position falls inside a rect:

```python
if event.type == pygame.MOUSEBUTTONDOWN:
    if button_rect.collidepoint(event.pos):
        print("Button clicked!")
```

This is the same idea as `colliderect()` checking whether two rects overlap, just checking a single point against one rect instead.

**Quick check**: if `button_rect` and `button_image` exist, how would you check whether the player clicked that button?

## Which Button Was Pressed?

`event.button` tells you which mouse button triggered the event: `1` for left, `2` for middle, `3` for right. Most games only care about the left button:

```python
if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
    ...
```

## Tracking the Mouse Every Frame

Clicks are events, they fire once, the instant the button goes down. Sometimes you want the mouse's position on every frame instead, for example to highlight a button the player is hovering over before they click it. `pygame.mouse.get_pos()` gives you that directly, no event needed:

```python
mouse_pos = pygame.mouse.get_pos()
hovering = button_rect.collidepoint(mouse_pos)
```

Call it once per frame, outside the event loop, since it always returns the mouse's current position rather than something that happened.

**Quick check**: would you use `MOUSEBUTTONDOWN` or `get_pos()` to make a button glow while the mouse sits over it, without clicking?

## Putting It Together

A button that changes color on hover and prints a message on click, combining everything above. Assumes your game loop already has `running = True` set before it starts, the same way every game in this prep material does:

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

## Words You'll Keep Seeing

- **MOUSEBUTTONDOWN**: the event fired the instant a mouse button is pressed
- **event.pos**: the `(x, y)` position of a mouse event
- **collidepoint()**: checks whether a position falls inside a rect
- **get_pos()**: the mouse's current position, read directly rather than from an event
