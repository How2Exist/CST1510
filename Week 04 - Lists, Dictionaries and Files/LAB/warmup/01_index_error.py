# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

labels = ["R-001", "R-002", "R-003"]

# Error is that list index is out of range when list is index (0, 1, 2) and trying to call index 3
# Fix: Change index call from 3 -> 2
print(labels[2])
