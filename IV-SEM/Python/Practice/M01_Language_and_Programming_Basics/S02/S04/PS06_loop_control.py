p1 = "abc123"

for i in range(3):
    p2 = input("Enter password: ")
    if p1 == p2:
        print("login successful")
        break
else:
        print("Account Locked")