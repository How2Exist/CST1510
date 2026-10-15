# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

def check(value, limit):
    status = "OVER LIMIT" if value > limit else "OK"
    # Add return
    return status

# Add print to output result
print(check(87, 100))

# print(status)
