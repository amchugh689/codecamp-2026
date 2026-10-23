On codehs:
- See [Snake](obsidian://open?vault=codecamp-2026&file=Advanced%2FWIP%2FSnake%2FExample%2FIssues) - same `SDL_AUDIODRIVER` fix applied here.


Locally:
- ~~When enemies reach edge of screen, they move with intense speed towards bottom, instead of going down one step~~
	- **Fixed**: the edge check now only triggers for the wall the enemies are currently moving towards (`enemy_dx > 0` vs the right wall, `enemy_dx < 0` vs the left wall). Previously, an enemy sitting at x=0 after a drop kept re-triggering `hit_edge` every frame because its x position hadn't changed yet, even though `enemy_dx` had already reversed - dropping it every frame instead of once.
