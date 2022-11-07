#numbers

numbers = [2, 3, 5, 7, 66, 89, 134]
playerNum = input("tell me a number")

if not playerNum.isdigit():
    print("that is not a number")
    exit()

playerNum = int(playerNum)
outputList = []

for i in numbers:
    if i < playerNum:
        outputList.append(i)

print(outputList)



