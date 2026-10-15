"""
RECORD CHECK  -  my version
===========================

Name  : Stefan Valev
Lane  :  IT
Date  : 09/10/2026

Run it:   python record_check.py


"""
# Hello! After making that quirky little loading thing with the dots for LAB D2
# I decided that I'd like to have a little fun with the mini project.
# I hope I haven't


"""Record Check program - compares rows loaded against rows expected and 
prints a report. Also does a bunch of claculations."""

# Five Hundred Improts
import os
import random
import shlex
import sys
import time
import termios
import tty

# Five thousand variables
CHILD_FLAG = "RECORD_CHECK_CHILD" # set when running inside the new Terminal window
# I don't know how else to run a seperate terminal on MacOS.
MIN_WIDTH = 34 # Min border size
LABEL_WIDTH = 11 # Label Column (left)
MIN_FIELD = 12 # Width of the right column
MARGIN = 5 # Extra space for the right side of the comlumn to make it look nice.
PERCENT_SUFFIX = " %" # Done like this so the digits are aligned.
BAR_CELLS = 30 # Loading bar squares!
FLASH_SECONDS = 2 # How long the prompt text flashes for.
SPIN_FRAMES = "|/-\\|/-\\|" # Spin!


def status_of(percent):
    """Return the status for a percentage: OVER LIMIT (100+), WARNING (90+) or OK."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"
 
 
def check(value, limit):
    """Return the difference and the 
    percentage."""
    difference = limit - value
    percent = value / limit * 100
    return difference, percent


def pause():
    """Wait a random 0.2-1 second. Doing this for *aesthetics*."""
    time.sleep(random.uniform(0.2, 1.0))


def spin():
    """Show a spinning loading symbol, then erase it."""
    for frame in SPIN_FRAMES:
        sys.stdout.write("[" + frame + "]")
        sys.stdout.flush()
        time.sleep(0.12)
        sys.stdout.write("\b\b\b")
    sys.stdout.write("   \b\b\b")
    sys.stdout.flush()


def draw_bar(filled):
    """Redraw the loading bar with the given number of squares filled."""
    bar = "[]" * filled + "  " * (BAR_CELLS - filled)
    sys.stdout.write("\rProcessing |" + bar + "|")
    sys.stdout.flush()


def loading_bar():
    """Fill the loading bar at a random pace (slow stretches or quick bursts), 
    then clear it."""
    filled = 0
    burst_left = 0
    while filled < BAR_CELLS:
        draw_bar(filled)
        if burst_left > 0:
            burst_left -= 1
            time.sleep(random.uniform(0.01, 0.05))
        else:
            if random.random() < 0.3:
                burst_left = random.randint(3, 7)
            time.sleep(random.uniform(0.15, 0.45))
        filled += 1
    draw_bar(filled)
    time.sleep(0.5)
    sys.stdout.write("\r" + " " * (len("Processing |") + 2 * BAR_CELLS + 1) + "\r")
    sys.stdout.flush()


def draw_prompt(prompt, visible, typed):
    """Redraw the input line, showing or hiding the prompt text but always 
    showing what was typed."""
    shown = prompt if visible else " " * len(prompt)
    sys.stdout.write("\r" + shown + typed + "\033[K")
    sys.stdout.flush()


def flash_input(prompt):
    """Read one line of input while the prompt text flashes on and off 
    every 2 seconds."""
    fd = sys.stdin.fileno()
    if not os.isatty(fd):
        return input(prompt)
    saved = termios.tcgetattr(fd)
    typed = ""
    visible = True
    try:
        tty.setcbreak(fd)
        termios.tcflush(fd, termios.TCIFLUSH)
        os.set_blocking(fd, False)
        last_toggle = time.monotonic()
        draw_prompt(prompt, visible, typed)
        finished = False
        while not finished:
            try:
                chunk = os.read(fd, 32)
            except BlockingIOError:
                if time.monotonic() - last_toggle >= FLASH_SECONDS:
                    visible = not visible
                    last_toggle = time.monotonic()
                    draw_prompt(prompt, visible, typed)
                time.sleep(0.02)
                continue
            if chunk == b"":
                raise EOFError
            for byte in chunk:
                if byte == 27:
                    break
                if byte == 10 or byte == 13:
                    finished = True
                    break
                if byte == 127 or byte == 8:
                    typed = typed[:-1]
                elif 32 <= byte <= 126:
                    typed += chr(byte)
            if not finished:
                draw_prompt(prompt, visible, typed)
        sys.stdout.write("\r" + prompt + typed + "\033[K\n")
        sys.stdout.flush()
        return typed
    finally:
        os.set_blocking(fd, True)
        termios.tcsetattr(fd, termios.TCSADRAIN, saved)


def read_whole_number(prompt, error_text, allow_zero):
    """Keep asking until the user enters a valid whole number, and return it."""
    while True:
        text = flash_input(prompt).strip().replace(",", "")
        if text.isascii() and text.isdigit() and len(text) <= 15:
            number = int(text)
            if number > 0 or allow_zero:
                return number
        print("  " + error_text)


def row_prefix(name):
    """Return the left part of a row: indent, padded label and colon."""
    return "  " + name.ljust(LABEL_WIDTH) + ": "


def print_report(label, value, limit, difference, percent, status):
    """Print the whole bordered report, one line at a time, 
    spinning before calculated numbers."""
    used_text = f"{value:.2f}"
    total_text = f"{limit:.2f}"
    free_text = f"{difference:.2f}"
    percent_text = f"{percent:.2f}"
    title = "  RECORD CHECK  -  " + label
    field = max(MIN_FIELD, len(used_text), len(total_text), len(free_text),
                len(percent_text), len(status))
    row_width = len(row_prefix("")) + field + len(PERCENT_SUFFIX) + MARGIN
    border = "=" * max(MIN_WIDTH, len(title) + 2, row_width)

    pause()
    print(border, flush=True)
    pause()
    print(title, flush=True)
    pause()
    print(border, flush=True)
    pause()
    print(row_prefix("Used") + used_text.rjust(field), flush=True)
    pause()
    print(row_prefix("Total") + total_text.rjust(field), flush=True)
    pause()
    print(row_prefix("Free"), end="", flush=True)
    spin()
    print(free_text.rjust(field), flush=True)
    pause()
    print(row_prefix("Percent"), end="", flush=True)
    spin()
    print(percent_text.rjust(field) + PERCENT_SUFFIX, flush=True)
    pause()
    print(row_prefix("Status") + status.rjust(field), flush=True)
    pause()
    print(border, flush=True)
    print(flush=True)


def print_summary(checked, over_limit):
    """Print the closing box with how many records were checked and how many 
    were OVER LIMIT."""
    border = "=" * MIN_WIDTH
    pause()
    print(border, flush=True)
    pause()
    print(row_prefix("Checked") + str(checked).rjust(MIN_FIELD), flush=True)
    pause()
    print(row_prefix("Over limit") + str(over_limit).rjust(MIN_FIELD), flush=True)
    pause()
    print(border, flush=True)


def launch_in_new_terminal():
    """Reopen this script in a new Terminal.app window. Return True if that window 
    was opened."""
    if os.environ.get(CHILD_FLAG) == "1" or sys.platform != "darwin":
        return False
    command = (f"{CHILD_FLAG}=1 {shlex.quote(sys.executable)} "
               f"{shlex.quote(os.path.abspath(__file__))}; exit")
    escaped = command.replace("\\", "\\\\").replace('"', '\\"')
    apple = f'tell application "Terminal"\nactivate\ndo script "{escaped}"\nend tell'
    exit_code = os.system(f"osascript -e {shlex.quote(apple)} >/dev/null 2>&1")
    return exit_code == 0


def wait_to_close():
    """Hold the new window open until Enter is pressed, so the results stay readable."""
    if os.environ.get(CHILD_FLAG) == "1":
        print("  Press Enter to close this window...", flush=True)
        try:
            input()
        except (KeyboardInterrupt, EOFError):
            pass


def main():
    """Run the check loop until 'quit', then print the OVER LIMIT count once."""
    if launch_in_new_terminal():
        return
    checked = 0
    over_limit = 0
    try:
        while True:
            label = flash_input("Dataset name (type 'quit' to stop): ").strip()
            if label.lower() == "quit":
                break
            if label == "":
                print("  Please enter a dataset name.")
                continue
            value = read_whole_number(
                "Rows loaded: ", "Rows loaded must be a whole number, 0 or more.", True)
            limit = read_whole_number(
                "Rows expected: ", "Rows expected must be a whole number, above 0.", False)
            difference, percent = check(value, limit)
            status = status_of(percent)
            loading_bar()
            print_report(label, value, limit, difference, percent, status)
            checked += 1
            if status == "OVER LIMIT":
                over_limit += 1
    except (KeyboardInterrupt, EOFError):
        sys.stdout.write("\n")
    print_summary(checked, over_limit)
    wait_to_close()


if __name__ == "__main__":
    main()
    

