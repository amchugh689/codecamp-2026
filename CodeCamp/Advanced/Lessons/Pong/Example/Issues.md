
Codehs - see [snake](obsidian://open?vault=codecamp-2026&file=Advanced%2FWIP%2FSnake%2FExample%2FIssues) - same `SDL_AUDIODRIVER` fix applied here.

local:
- see general issues
- This game doesn't have a game over, it just keeps going but resets score every death. Could it implement lives?
  - **Decision: leave as-is.** The base game resetting on a miss is intentional; Lesson 4 already has a different extension idea ("A Win Condition" - stop at a target score), and a lives system would compete with that rather than complement it.