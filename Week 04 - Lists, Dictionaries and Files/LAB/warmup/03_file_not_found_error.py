# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

# records.txt file does not exist.
# Fix: Multiple ways to fix like creating the file beforehand or adding error handling. Will add error handling.
try:
    with open("records.txt") as f:
        print(f.read())
except FileNotFoundError:
    print("File does not exist.")
