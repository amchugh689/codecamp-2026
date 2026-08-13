On CodeHS (happens for all games):
```
pygame 2.5.2 (SDL 2.28.2, Python 3.11.14)
Hello from the pygame community. https://www.pygame.org/contribute.html
ALSA lib confmisc.c:855:(parse_card) cannot find card '0'
ALSA lib conf.c:5178:(_snd_config_evaluate) function snd_func_card_inum returned error: No such file or directory
ALSA lib confmisc.c:422:(snd_func_concat) error evaluating strings
ALSA lib conf.c:5178:(_snd_config_evaluate) function snd_func_concat returned error: No such file or directory
ALSA lib confmisc.c:1334:(snd_func_refer) error evaluating name
ALSA lib conf.c:5178:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5701:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2664:(snd_pcm_open_noupdate) Unknown PCM default
```
- **Fixed**: added `import os` + `os.environ["SDL_AUDIODRIVER"] = "dsp"` before `pygame.init()` in every example file (matches CodeHS's own reference examples), so the sandbox doesn't try to talk to a real ALSA sound card.


Locally:
- ~~Builds & runs fine, however pressing two directional keys in quick succession causes a game over~~
  - **Fixed**: direction changes now go into a `next_dx, next_dy` pair on keydown, and are only copied into the direction actually used for movement (`dx, dy`) once per move tick. Previously, two keypresses in the same tick could set a direction that was the reverse of the snake's actual heading, driving it straight into its own body.
