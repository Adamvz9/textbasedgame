print ("Welcome player are you ready?")

Direction = input("Do you want to go down the left path or right path")

if Direction == "Left" or Direction =="left":
    print ("You go towards the village")
elif Direction == "Right" or  Direction =="right":
    print("You go towards the lake")

print ("you encounter the warlock of the east he questions you about the secret password of the town as there has been rumors of spies running around trying to collect intel. ")
print("pick one, apple, sock, stick")

attempts = 3
password = "apple"

while attempts > 0:
    guess = input("please enter your guess")
    if guess == password:
        print("you pass the warlocks test")
        break

    attempts -= 1
else:
    print("no attempts lefts")


