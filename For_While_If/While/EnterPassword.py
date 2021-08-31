guess = input("Enter password: ")
password = 'qwerty'
count = 0
while guess != password:
    count += 1
    print("Incorrect password entered! Try again!")
    guess = input()
print(f"You spent {count} attempts")
