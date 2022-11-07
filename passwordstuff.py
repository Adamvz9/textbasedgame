#password

attempts = 3
password = "apple"

while attempts > 0:
    guess = input("please enter your password")
    if guess == password:
        print("login successful")
        break

    attempts -= 1
else:
    print("no attempts lefts")