# Merry Christmas (Terminal Performance)

A small terminal performance that animates a colorful ASCII Christmas tree while syncing on-screen lyrics to "Last Christmas". It uses `pygame` for audio playback and ANSI colors for the tree.

## What It Does
- Plays `Last Christmas.mp3` via `pygame.mixer`.
- Animates a blinking, colorized ASCII tree in the terminal.
- Shows lyrics in sync with the song.

## Requirements
- Python 3.8+
- `pygame`

Install dependencies:

```bash
pip install pygame
```

## Run
From this folder:

```bash
python main.py
```

## Notes
- Keep `Last Christmas.mp3` in the same folder as `main.py`.
- On Windows, ANSI color support is enabled automatically if possible. If colors look off, try Windows Terminal.
- If audio fails to initialize, the script will print an error and exit.

## Files
- `main.py` — main program
- `Last Christmas.mp3` — audio track
