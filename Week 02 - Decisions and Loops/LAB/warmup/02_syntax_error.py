# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

attempts = 3
max_attempts = 3

while attempts <= max_attempts
    print("checking...")
    attempts += 1

# Error is that the while loop is missing a colon 
# at the end of the line. Fixed program:

attempts = 3
max_attempts = 3

while attempts <= max_attempts:
    print("checking...")
    attempts += 1