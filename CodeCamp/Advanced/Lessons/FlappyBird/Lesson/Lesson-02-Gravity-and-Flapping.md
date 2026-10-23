# Lesson 2 – Gravity & Flapping

## Velocity That Changes Itself: Gravity

So far you might think of movement as "add a fixed amount to a position every frame." That works for something moving at a constant speed, but a falling object doesn't move at a constant speed: it starts slow and keeps getting faster the longer it falls. That's what gravity is, in code terms: instead of adding a fixed amount to the bird's position each frame, you add a small, fixed amount to its **velocity** each frame, and then add that (constantly increasing) velocity to its position.

```
velocity = velocity + gravity   # velocity grows every frame
position = position + velocity  # position changes faster and faster
```

Two lines, but the effect is a believable falling motion: slow at first, speeding up the longer nothing interrupts it.

## Flapping: A One-Off Push

A flap doesn't gradually push the bird upward, it instantly sets its velocity to a specific upward value the moment you press a key, overriding whatever the velocity was before (even if it was a large downward number from a long fall). Gravity then immediately starts pulling that velocity back down again, frame by frame, which is what gives a flap its "rise then fall" arc rather than a floaty, permanent upward drift.

Because this should happen exactly once per press rather than continuously, it belongs in the part of the game loop that reports single moments (a key going down), not the part that reports what's currently held.

## Ending the Game at the Edges

If the bird's y-position goes above the top of the window or below the bottom, that's a loss: the bird has flown off the playable area. Checking this is a simple comparison against `0` and the window's height, done every frame right after gravity and the bird's position are updated.

## Check Your Understanding

- Why does a falling object's velocity need to change every frame, rather than staying fixed?
- Why does a flap set velocity directly rather than gradually increasing it?
