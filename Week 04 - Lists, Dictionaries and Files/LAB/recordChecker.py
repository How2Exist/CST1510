"""
RECORD CHECK  -  my version
===========================

Name  :  Stefan
Lane  :  IT
Date  :  17/10/2026

Run it:   python recordChecker.py
"""

"""Record Check (batch) - checks every record in a data file and prints a CRT-style report for each."""
 
import os
import random
import shlex
import sys
import time
import termios


# PS: Why add so many pointless variables? idk
CHILD_FLAG = "RECORD_CHECK_CHILD"   # set when running inside the new Terminal window
RECORDS_FILE = "records_sample.txt" # input: one label,value,limit per line
RESULTS_FILE = "results.txt"        # output: one label,status per line
MIN_WIDTH = 34                      # narrowest border, matching the design sample
LABEL_WIDTH = 11                    # label column, so the colons line up
MIN_FIELD = 12                      # width of the right-aligned value column
MARGIN = 5                          # spare space to the right of the value column
PERCENT_SUFFIX = " %"               # sits after the right edge so digits stay aligned
BAR_CELLS = 30                      # squares in the loading bar
SPIN_FRAMES = "|/-\\|/-\\|"         # [|] -> [/] -> [-] -> [\] -> [|] -> [/] -> [-] -> [\] -> [|]
 
 
def status_of(percent):
    """Return the status for a percentage: OVER LIMIT (100+), WARNING (90+) or OK."""
    if percent >= 100:
        return "OVER LIMIT"
    if percent >= 90:
        return "WARNING"
    return "OK"
 
 
def check_record(value, limit):
    """Return the difference (limit - value), the percentage (value / limit * 100) and the status."""
    difference = limit - value
    percent = value / limit * 100
    return difference, percent, status_of(percent)
 
 
def parse_count(text):
    """Return text as a whole number, or None if it is not one."""
    text = text.strip()
    if text.isascii() and text.isdigit() and len(text) <= 15:
        return int(text)
    return None
 
 
def load_records(path):
    """Read label,value,limit lines from a file and return them as a list of dicts (no statuses)."""
    records = []
    with open(path, encoding="utf-8", errors="replace") as handle:
        for number, line in enumerate(handle, start=1):
            if line.strip() == "":
                continue
            parts = line.strip().split(",")
            if len(parts) != 3:
                raise ValueError(number)
            label = parts[0].strip()
            value = parse_count(parts[1])
            limit = parse_count(parts[2])
            if label == "" or value is None or limit is None or limit == 0:
                raise ValueError(number)
            records.append({"label": label, "value": value, "limit": limit})
    return records
 
 
def write_result(handle, label, status):
    """Write one label,status line to the open results file."""
    handle.write(label + "," + status + "\n")
 
 
def pause():
    """Wait a random 0.2-1 second, like a slow CRT terminal drawing its next line."""
    time.sleep(random.uniform(0.2, 1.0))
 
 
def spin():
    """Show a spinning indicator, then erase it."""
    for frame in SPIN_FRAMES:
        sys.stdout.write("[" + frame + "]")
        sys.stdout.flush()
        time.sleep(0.12)
        sys.stdout.write("\b\b\b")
    sys.stdout.write("   \b\b\b")
    sys.stdout.flush()
 
 
def draw_bar(filled):
    """Redraw the Processing bar with the given number of squares filled."""
    bar = "[]" * filled + "  " * (BAR_CELLS - filled)
    sys.stdout.write("\rProcessing |" + bar + "|")
    sys.stdout.flush()
 
 
def loading_bar():
    """Fill the Processing bar at a random pace (slow stretches, quick bursts), then clear it."""
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
 
 
def row_prefix(name):
    """Return the left part of a row: indent, padded label and colon."""
    return "  " + name.ljust(LABEL_WIDTH) + ": "
 
 
def print_report(label, value, limit, difference, percent, status):
    """Print the whole bordered report, one line at a time, spinning before calculated numbers."""
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
    """Print the closing box with how many records were checked and how many were OVER LIMIT."""
    border = "=" * MIN_WIDTH
    pause()
    print(border, flush=True)
    pause()
    print(row_prefix("Checked") + str(checked).rjust(MIN_FIELD), flush=True)
    pause()
    print(row_prefix("Over limit") + str(over_limit).rjust(MIN_FIELD), flush=True)
    pause()
    print(border, flush=True)
 
 
def data_path(name):
    """Return the full path of a data file that lives next to this script."""
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), name)
 
 
def process_records(records, results_path):
    """Check and report every record, save each result, and return how many were OVER LIMIT."""
    over_limit = 0
    with open(results_path, "w", encoding="utf-8") as results:
        for record in records:
            difference, percent, status = check_record(record["value"], record["limit"])
            print_report(record["label"], record["value"], record["limit"],
                         difference, percent, status)
            write_result(results, record["label"], status)
            if status == "OVER LIMIT":
                over_limit += 1
    return over_limit
 
 
def launch_in_new_terminal():
    """Reopen this script in a new terminal window and return True if that window was opened."""
    if os.environ.get(CHILD_FLAG) == "1" or sys.platform != "darwin":
        return False
    command = (f"{CHILD_FLAG}=1 {shlex.quote(sys.executable)} "
               f"{shlex.quote(os.path.abspath(__file__))}; exit")
    escaped = command.replace("\\", "\\\\").replace('"', '\\"')
    apple = f'tell application "Terminal"\nactivate\ndo script "{escaped}"\nend tell'
    exit_code = os.system(f"osascript -e {shlex.quote(apple)} >/dev/null 2>&1")
    return exit_code == 0
 
 
def wait_to_close():
    """keep the new window open until Enter is pressed, so the results stay readable."""
    if os.environ.get(CHILD_FLAG) == "1":
        print("  Press Enter to close this window...", flush=True)
        try:
            if os.isatty(sys.stdin.fileno()):
                termios.tcflush(sys.stdin.fileno(), termios.TCIFLUSH)
            input()
        except (KeyboardInterrupt, EOFError):
            pass
 
 
def main():
    """Load the records, report on each one, save the results, and print the OVER LIMIT count once."""
    if launch_in_new_terminal():
        return
    records_path = data_path(RECORDS_FILE)
    results_path = data_path(RESULTS_FILE)
    try:
        records = load_records(records_path)
    except FileNotFoundError:
        print("  Could not find " + RECORDS_FILE + " - starting with no records.")
        records = []
    except ValueError as problem:
        print("  " + RECORDS_FILE + " line " + str(problem) +
              " is not valid (expected label,value,limit) - starting with no records.")
        records = []
    try:
        if len(records) == 0:
            print("  No records to check.")
        else:
            loading_bar()
            over_limit = process_records(records, results_path)
            print_summary(len(records), over_limit)
            print("  Results saved to " + RESULTS_FILE)
    except KeyboardInterrupt:
        sys.stdout.write("\n")
    wait_to_close()
 
 
if __name__ == "__main__":
    main()
 

# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job
