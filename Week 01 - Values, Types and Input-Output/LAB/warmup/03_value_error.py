# BROKEN ON PURPOSE.
# Run it, type 23.7 when asked, read the last line, then fix it.

value = int(input("Value: "))

print(value)

# Error: ValueError: invalid literal for 
# int() with base 10: '23.7'
# Cause: int(input()) expects an integer, 
# but 23.7 is a float.

#Fixed code:

value = float(input("Value: "))

print(value)
