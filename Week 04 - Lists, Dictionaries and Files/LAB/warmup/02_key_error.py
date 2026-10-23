# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

record = {"label": "R-001", "value": 87.0, "limit": 100.0}

# No such key as status.
# Fix: Most likely wants to get value, so replace "status" with "value"
print(record["value"])
