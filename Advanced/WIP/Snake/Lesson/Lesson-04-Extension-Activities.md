# Lesson 4 – Extension Activities

## Overview

Your game already works: a snake that moves, grows, and ends the game on collision, with a score. This lesson is a set of independent extensions you can pick from to make it your own. This page introduces the idea behind each one; the matching task page has the implementation steps.

Do them in any order, combine as many as you like, or skip straight to the competition if you're happy with what you've got.

## Idea: Restart Without Re-running

Right now, once the game ends, the only way to play again is to run the program again from scratch. Letting the player press a key to reset every piece of state (the snake's body, its direction, the score, and the `game_over` flag) back to how it started, without leaving the program, makes it feel like a real game rather than a one-shot demo.

## Idea: Speed Ramp

A fixed `MOVE_INTERVAL` never gets any harder. Shrinking it slightly as the score goes up makes the snake move faster the longer a run goes on, tying difficulty directly to how well the player is doing.

## Idea: Wrap-Around Edges

Instead of ending the game at a wall, the snake could reappear on the opposite side of the screen, as if the grid wrapped around on itself. This changes what happens at the wall-collision check from "end the game" to "recalculate the position," while leaving self-collision untouched.

## Idea: Obstacles

Fixed blocks placed on the board that end the game if the snake's head touches them, checked the same way self-collision already is: a position, checked against a list.

## Idea: Sound Effects

A short sound for eating food and a different one for a collision. Browser-based environments don't always support audio reliably, so sound code is usually written to fail silently rather than crash the game if it doesn't work.

---

Ready to try one? Head to [Lesson 4 Task – Extension Activities](../Tutorial/Lesson-04-Extension-Activities-Task.md).
