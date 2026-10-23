# Lesson 4 – Extension Activities

## Overview

Your game already works: a flapping bird, scrolling pipes, collisions, and a score. This lesson is a set of independent extensions you can pick from to make it your own. This page introduces the idea behind each one; the matching task page has the implementation steps.

Do them in any order, combine as many as you like, or skip straight to the competition if you're happy with what you've got.

## Idea: Restart Without Re-running

Right now, once the game ends, the only way to play again is to run the program again from scratch. Letting the player press a key to reset every piece of state (the bird's position and velocity, the pipe list, the score, and the `game_over` flag) back to how it started, without leaving the program, makes it feel like a real game rather than a one-shot demo.

## Idea: A High Score

A single run's score disappears the moment you restart. Keeping track of the best score seen so far, in a variable that only ever gets reset when the whole program restarts (not when the game restarts), gives the player something to beat.

## Idea: Difficulty Ramp

A constant pipe speed and gap size never gets any harder. Increasing `PIPE_SPEED` slightly, or shrinking `GAP_HEIGHT` slightly, as the score goes up ties difficulty directly to how well the player is doing, rather than to a fixed timer.

## Idea: A Second Way to Fly

Some versions of this style of game let you hold a key to rise steadily instead of tapping to flap. This means checking held keys (not just single presses) and setting velocity toward a target rather than instantly overriding it, a different feel from the tap-to-flap control in Lesson 2.

## Idea: Sound Effects

A short sound for flapping and a different one for a collision. Browser-based environments don't always support audio reliably, so sound code is usually written to fail silently rather than crash the game if it doesn't work.
