import time
import os
import random
import sys

try
    import pygame
except Exception:
    pygame = None

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

COLORS = ["\033[31m", "\033[32m", "\033[33m", "\033[34m", "\033[35m", "\033[36m"]
HIGHLIGHT = "\033[1;92m"
RESET = "\033[0m"

LYRICS = [
    (0, "--- ❄️ Instrumental Intro ❄️ ---"),
    (15, "Last Christmas, I gave you my heart"),
    (19, "But the very next day, you gave it away"),
    (24, "This year, to save me from tears"),
    (28, "I'll give it to someone special"),
    (33, "Last Christmas, I gave you my heart"),
    (37, "But the very next day, you gave it away"),
    (42, "This year, to save me from tears"),
    (46, "I'll give it to someone special"),
    (52, "Once bitten and twice shy"),
    (56, "I keep my distance, but you still catch my eye"),
    (61, "Tell me, baby, do you recognize me?"),
    (65, "Well, it's been a year, it doesn't surprise me"),
    (70, "Happy Christmas, I wrapped it up and sent it"),
    (74, "With a note saying 'I love you', I meant it"),
    (79, "Now I know what a fool I've been"),
    (83, "But if you kissed me now, I know you'd fool me again"),
    (88, "Last Christmas, I gave you my heart"),
    (92, "But the very next day, you gave it away"),
    (97, "This year, to save me from tears"),
    (101, "I'll give it to someone special"),
    (110, "A crowded room, friends with tired eyes"),
    (115, "I'm hiding from you and your soul of ice"),
    (119, "My God, I thought you were someone to rely on"),
    (123, "Me? I guess I was a shoulder to cry on"),
    (128, "A face on a lover with a fire in his heart"),
    (132, "A man under cover but you tore me apart"),
    (137, "Now I've found a real love, you'll never fool me again"),
    (142, "Last Christmas, I gave you my heart"),
    (146, "But the very next day, you gave it away"),
    (151, "This year, to save me from tears"),
    (155, "I'll give it to someone special")
]

tree_structure = [
    "       * ", "      *** ", "     ***** ", "    ******* ", "   ********* ",
    "  *********** ", " ************* ", "***************", "      |||      ", "      |||      "
]

def _enable_windows_ansi():
    if os.name != "nt":
        return True
    try:
        import ctypes
        kernel32 = ctypes.windll.kernel32
        handle = kernel32.GetStdHandle(-11)  # STD_OUTPUT_HANDLE
        mode = ctypes.c_uint32()
        if kernel32.GetConsoleMode(handle, ctypes.byref(mode)) == 0:
            return False
        ENABLE_VIRTUAL_TERMINAL_PROCESSING = 0x0004
        new_mode = mode.value | ENABLE_VIRTUAL_TERMINAL_PROCESSING
        return kernel32.SetConsoleMode(handle, new_mode) != 0
    except Exception:
        return False

ANSI_ENABLED = _enable_windows_ansi()

def clear_console():
    cmd = 'cls' if os.name == 'nt' else 'clear'
    if os.system(cmd) != 0:
        print("\n" * 50)

def get_colored_tree():
    colored_tree = []
    for line in tree_structure:
        if ANSI_ENABLED:
            new_line = "".join([f"{random.choice(COLORS)}{c}{RESET}" if c == "*" else c for c in line])
        else:
            new_line = "".join([c for c in line])
        colored_tree.append(new_line)
    return colored_tree

def run_performance():
    if pygame is None:
        print("Error: pygame is not installed. Install with: pip install pygame")
        return
    try:
        import pygame.mixer as pg_mixer
    except Exception:
        pg_mixer = None

    if pg_mixer is None:
        print("Warning: pygame.mixer is not available. Running without audio.")
    try:
        if pg_mixer is not None:
            pg_mixer.init()
    except Exception as e:
        print(f"Error: could not initialize audio device ({e}).")
        return

    audio_path = resource_path("Last Christmas.mp3")

    try:
        if pg_mixer is not None:
            pg_mixer.music.load(audio_path)
            pg_mixer.music.play()
    except Exception:
        print(f"Error: could not load song. Looking for: {audio_path}")
        print("Make sure 'Last Christmas.mp3' is in the same folder as main.py.")
        return

    start_time = time.time()
    try:
        end_at = (LYRICS[-1][0] + 8) if LYRICS else 30
        def is_running(elapsed):
            if pg_mixer is None:
                return elapsed <= end_at
            return pg_mixer.music.get_busy()

        while True:
            elapsed = time.time() - start_time
            if not is_running(elapsed):
                break
            clear_console()
            tree = get_colored_tree()
            current_lyric = ""
            for ts, text in LYRICS:
                if elapsed >= ts:
                    current_lyric = text

            print("\n    🎄 MERRY CHRISTMAS 🎄\n")
            for i, line in enumerate(tree):
                if i == 4:
                    print(f"{line}   {HIGHLIGHT}{current_lyric}{RESET}")
                else:
                    print(line)
            time.sleep(0.2)
    except KeyboardInterrupt:
        if pg_mixer is not None:
            pg_mixer.music.stop()

if __name__ == "__main__":
    run_performance()
