# Lesson 4 – Extension Activities

## Overview

Your game already works: a player ship, marching enemies, bullets, scoring, and a win/lose message. This lesson is a set of independent extensions you can pick from to make it your own. This page introduces the idea behind each one; the matching task page has the implementation steps.

Do them in any order, combine as many as you like, or skip straight to the competition if you're happy with what you've got.

## Idea: Enemy Return Fire

Right now only the player can shoot. Giving enemies their own bullets, fired downward at random moments, turns a one-sided shooting gallery into something with actual risk. The core idea is a second list of bullets, moving the opposite direction, with a small random chance each frame that an enemy fires one.

## Idea: Lives Instead of One Hit

At the moment, one enemy bullet reaching the player would end the game outright (once you've built return fire). Giving the player a small number of lives, and only ending the game once they run out, makes losing feel less abrupt.

## Idea: Difficulty Ramp

As enemies are destroyed, there are fewer of them left, which in the original Space Invaders means the remaining ones speed up. This comes from tying `enemy_dx`'s size (not just its direction) to how many enemies remain in the list.

## Idea: A Bonus UFO

A rare, fast-moving enemy that crosses the top of the screen occasionally, worth more points than a regular enemy if hit. This is a second, independent object with its own timer for when it appears, separate from the main enemy grid.

## Idea: Barriers

Small blocks of cover between the player and the enemies that can be shot away bit by bit, by either side, giving the player somewhere to hide. This reuses the same rectangle-collision idea from Lesson 3, just with a small grid of destructible blocks instead of one player rectangle.

## Idea: Sound Effects

A short sound for firing and a different one for an enemy being destroyed. Browser-based sandboxes don't always support audio reliably, so sound code is usually written to fail silently rather than crash the game if it doesn't work.

---

Ready to try one? Head to [Lesson 4 Task – Extension Activities](../Tutorial/Lesson-04-Extension-Activities-Task.md).
