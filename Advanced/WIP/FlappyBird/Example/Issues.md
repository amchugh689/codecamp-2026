
On CodeHS:
- Doesn't run - see [Snake](obsidian://open?vault=codecamp-2026&file=Advanced%2FWIP%2FSnake%2FExample%2FIssues) - same `SDL_AUDIODRIVER` fix applied here.


Locally:
- After building & opening, game instantly ends. User has no opportunity to press play etc.
	- Gravity too strong? Not enough time to input? Should all games have a title screen that allows the user to press any key to start to prevent this?
	- **Decision: leave as-is for now.** Start screens (and restart-without-exiting, raised in general issues) are being left out of the base 3-lesson game and Complete-Game.py by design - restart is already an optional Lesson 4 extension idea for Snake/FlappyBird. A start screen isn't currently one of the Lesson 4 extension ideas for any game; worth considering adding it as a new extension idea in a future pass rather than folding it into the base tutorial.