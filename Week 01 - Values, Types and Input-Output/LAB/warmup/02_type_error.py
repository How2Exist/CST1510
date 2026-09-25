# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

value = input("Value: ")

print(value + 1)

# Error: TypeError: can only concatenate 
# str (not "int") to str
# Cause: input() returns a string, 
# so value is a string. 

#Fixed code:

value = int(input("Value: "))
print(value + 1)
