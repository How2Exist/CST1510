# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

limit = 20
value = input("Value: ")

if value > limit:
    print("OVER")
else:
    print("OK")

# Error: TypeError: '>' not supported between 
# string and integer. Fixed code:

limit = 20
value = int(input("Value: "))

if value > limit:
    print("OVER")
else:
    print("OK")
    
# or

limit = 20
value = input("Value: ")

if int(value) > limit:
    print("OVER")
else:
    print("OK")