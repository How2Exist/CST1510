# C2
password = "python123"
tries = 0
while tries < 3:
    guess = input("Enter the password: ")
    if guess == password:
        print("Access Granted")
        break
    else:
        print("Wrong Password")
        tries += 1
if tries == 3:
    print ("Account Locked")