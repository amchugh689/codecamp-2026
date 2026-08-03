# Lesson 4 – Extension Activities

## Overview

Your game already works: a paddle, a bouncing ball, and a score. This lesson is a set of independent extensions you can pick from to make it your own. This page introduces the idea behind each one; the matching task page has the implementation steps.

Do them in any order, combine as many as you like, or skip straight to the competition if you're happy with what you've got.

## Idea: An AI Opponent

Right now the right wall just bounces the ball back; there's no real opponent. A simple way to fake an opponent is to give the "wall" its own paddle and move it a fixed amount toward the ball's current position every frame. It won't play perfectly (a fast-moving ball can still get past it), which is what makes it feel like an opponent rather than an unbeatable wall.

## Idea: Two-Player Mode

Instead of AI control, a second paddle can be controlled by a second set of keys (commonly `W`/`S` for one player, arrow keys for the other) using the same held-key pattern from Lesson 2.

## Idea: Angled Bounces

Real Pong doesn't bounce the ball back at a fixed angle: where the ball hits the paddle changes the angle it leaves at. Hitting near the paddle's centre gives a mostly-straight bounce; hitting near an edge gives a steeper one. This comes from comparing the ball's position to the paddle's centre at the moment they collide.

## Idea: Escalating Difficulty

A rally that never speeds up can feel flat. Increasing the ball's velocity slightly every time it bounces off a paddle (while keeping its direction) makes each rally get harder the longer it survives, and resetting the speed on a miss keeps every new rally fair.

## Idea: A Win Condition

So far, the game runs forever. Adding a target score and a way to stop and display an end screen once someone reaches it turns an endless rally into an actual match with a result.

## Idea: Sound Effects

A short sound on a paddle hit or a scored point adds feedback beyond what you can see. Browser-based sandboxes don't always support audio reliably, so sound code is usually written to fail silently rather than crash the game if it doesn't work.

---

Ready to try one? Head to [Lesson 4 Task – Extension Activities](../Tutorial/Lesson-04-Extension-Activities-Task.md).
