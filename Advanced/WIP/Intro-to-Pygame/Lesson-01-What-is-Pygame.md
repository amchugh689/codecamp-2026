## What Is PyGame?

Python doesn't know how to open a window, draw a shape, or read a key press on its own. PyGame is a library that adds those abilities: windows, drawing, keyboard/mouse input, sound, so you can focus on your game instead of building that machinery yourself.

## Why Games Don't Just Run Once

Most scripts run top to bottom, then stop. A game can't: it needs to keep its window open, keep checking for input, and keep redrawing the screen so anything that moves appears to move. It only stops when the player quits. PyGame games do this with a **game loop**.

## The Game Loop

A game loop repeats continuously, many times per second. Each pass, the game:

1. **Checks for input** - a key press, a click, or the window closing
2. **Updates the game state** - works out what's changed
3. **Draws everything** - shows the result on screen

Then repeats. Every game you build this week starts with one of these loops, because without it there's just a window that draws once and freezes.

**Quick check**: what three things does a game loop do on every pass?

## Frame Rate

Left to run flat out, the loop would go faster on a fast computer than a slow one. PyGame uses a clock to cap how many times it runs per second: the **frame rate**, or FPS. You'll see this set to a fixed number, commonly 60, in every game you build.

**Quick check**: why cap the frame rate instead of letting the loop run as fast as possible?

## Words You'll Keep Seeing

- **Window**: the box PyGame draws your game into
- **Event**: something the game might care about, most often a key press or the window closing
- **Clock**: controls frame rate
- **Surface**: the area PyGame draws onto (usually your window)
