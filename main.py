theString = "Hello World"
numLs = int(0)

for letter in theString:
    if letter.lower() == "l":
        numLs += 1

print("the number of Ls in the string is {}" .format(numLs))
