## Why Bother With Images?

Every game so far in this prep material draws players, enemies, and obstacles as plain rectangles or circles. That's on purpose: shapes keep the focus on logic instead of artwork. But for your own project, swapping a rectangle for a picture, a **sprite**, is one of the easiest ways to make a game look like a real game instead of a prototype.

A sprite is just an image PyGame draws onto the screen at a given position, the same way you've already been drawing shapes.

## Loading an Image

Add the image file to your project first by clicking the `New +` button in the sidebar. Once it's there, load it with:

```python
player_image = pygame.image.load("player.png")
```

Change `"player.png"` to match whatever your image is called. 

This reads the file once and stores it as a **Surface**, the same kind of object your game window is. Do this once, outside the game loop, since re-loading the file every frame would slow the game down for no benefit.

**Quick check**: why load the image before the game loop starts, rather than inside it?

## Transparency With convert_alpha()

Most sprite images have transparent backgrounds so they don't show up as a solid box. Tell PyGame to handle that properly, and draw faster, by calling `convert_alpha()` right after loading:

```python
player_image = pygame.image.load("player.png").convert_alpha()
```

Without it, transparent areas can appear as solid black or white, and every image draws slower.

## Sizing an Image With Rects

A `pygame.Rect` describes a box: an `(x, y)` position plus a width and height. If your game already uses rects for shapes, positioning and collision work the same way for images, `get_rect()` builds one from the image's actual size:

```python
player_rect = player_image.get_rect()
player_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
```

Move the sprite by changing `player_rect.x` and `player_rect.y` each frame, and check whether it overlaps another rect with `player_rect.colliderect(other_rect)`. The image just gives you something nicer to draw at that rect's position, the position and collision logic don't change.

**Quick check**: if two sprites' images don't overlap but their rects are set slightly larger than the artwork, what might that do to collisions?

## Resizing an Image

Image files come in whatever size they were drawn at, which rarely matches what your game needs. Resize one with `pygame.transform.scale()`, giving it the image and a `(width, height)`:

```python
player_image = pygame.transform.scale(player_image, (40, 40))
```

Do this once, right after loading, not every frame, for the same reason as loading itself.

## Drawing an Image

Swap `pygame.draw.rect()` or `pygame.draw.circle()` for `blit()`, the same call used to draw text onto the screen. It takes the thing to draw and where to draw it:

```python
window.blit(player_image, player_rect)
```

That's the whole change. Update `player_rect`'s position each frame the same way you'd update a shape's position, the drawing line is the only thing that's different.

**Quick check**: what two things does `blit()` need to draw an image?

## Where to Get Images

You'll need actual image files to try this. PNG files with transparent backgrounds work best.

## Glossary

- **Sprite**: an image drawn onto the screen at a position, standing in for a shape
- **Surface**: what an image becomes once loaded, the same kind of object as your game window
- **Blit**: draw a Surface (an image, or rendered text) onto another Surface at a given position
