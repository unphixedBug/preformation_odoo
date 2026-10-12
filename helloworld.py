import random

'''
# greeting

print(input("Enter your first name: "))

# display sum 
intVar = 3
floatVar = 2.2
print(intVar + floatVar)

# multiply two num

print(int(input("Enter a number")) * int(input("Enter another number")))

# rectangle area

print(int(input("Length")) * int(input("Height")))

# user age

print(2026 - int(input("where are you born")))

# sentence generator

print(input("whats your name") + " found " + input("item you want (with preposition)") + " " + input("where (with prero)"))

# ID
userLastName = input("Last name: ")
userFirstName = input("First name: ")
userAge = input("Age: ")
userClass = input("Class: ")

print("LAST NAME: " + userLastName)
print("First name: " + userFirstName)
print("Age: " + userAge)
print("Class: " + userClass)

# average

print((int(input("num")) + int(input("num")) + int(input("num"))) / 3)

# !! circle perimeter

# price with tva

print(int(input("price without tva")) * 1.21)

#swap values

a = input("first value")
b = input("second value")

print("after swapping: a = " + b + " and b = " + a)

# fahrenheit to celsius

print(((int(input("fahrenheit temp: ")) - 32) * 5 / 9) + 5)

# !! word mixer

userWord1 = input("word 1 plz: ")
userWord2 = input("word 2 plz: ")
userWord3 = input("word 3 plz: ")
userWordsList = [userWord1, userWord2, userWord3]
shuffledUserWordsList = random.shuffle(userWordsList)

print(userWord1 + userWord1 + userWord2 + userWord2 + userWord3 + userWord3)
print(userWord1[::-1].upper(), userWord2[::-1].upper(), userWord3[::-1].upper())
print(shuffledUserWordsList)

# sum of digits

userNum = input("give me 3 digit positive number")

word = "Programming"
print(word[0])
print(word[-1])
print(word[0:3])
print(word[3:7])
print(word[::-1])

print("-".join("Je suis un fifou".split()))

stringInput = input("enter a string: ")
max_length = int(input("enter the max length: "))

print(stringInput[0: max_length] + "...") if len(stringInput) > max_length else print(stringInput)

userInt = int(input("entier stp: "))
print("0" if userInt == 0 else "even" if userInt % 2 == 0 else "odd")

userNum1 = int(input("first num plz: "))
userNum2 = int(input("second num plz: "))

if userNum1 % 2 == 0:
    if userNum2 % 2 != 0:
        print("Congrats")
else:
    if userNum2 % 2 == 0:
        print("Congrats")

temp = int(input("enter temps plz: "))

if temp < 10:
    print("glagla")
elif temp < 15:
    print("glagla mais un peu moins")
elif temp < 20:
    print("bien bien")
else:
    print("canicular")

for x in range(1, 6):
    print(f"{x} Goodbye")


total = 0

for x in range(1, 11):
    if x % 2 == 0:
        total += x

print(total)


vowels = ["a", "e", "i", "o", "u"]
result = ""

for i in "Coucou vas tu bien":
    if i.isalpha():
        if i in vowels:
            result += i.upper()
        else:
            result += i.lower()
    else:
        result += "_"

print(result)


fruits = ["apple", "banana", "strawberry", "penser à acheter du lay"]

for i, fruit in enumerate(fruits):
    print(f"{i + 1}: {fruits[i]}")

    tries = 10


number = random.randrange(1, 100)

while tries > 0:
    userInput = input("choisis un nombre: ")

    try:
        userInput = int(userInput)
    except ValueError:
        print("donne un entier stp")
        break

    if userInput == number:
        print("gg")
        break
    else:
        tries -= 1
        if userInput > number:
            if tries > 0:
                print("moins")
            else:
                print("perdu")
                break
        else:
            if tries > 0:
                print("plus")
            else:
                print("perdu")
                break

---

while True:
    print(input("gimme a word"))

    res = input("wanne stop ? type stop")

    if res.lower() == "stop":
        break

---

result = ""

for i in "phrase avec 456 mots ou un peu moins peut-être":
    if not i.isalpha():
        continue
    result += i.upper()

print(result)

---

playerOneName = input("Player one name: ")
playerTwoName = input("Player two name: ")

playerOneScore = 0
playerTwoScore = 0
manche = 1

choices = ["rock", "paper", "scissors"]

while playerOneScore < 3 and playerTwoScore < 3:
    print(f"Round: {manche}")
    playerOneChoice = input(f"{playerOneName} choice: ")
    playerTwoChoice = input(f"{playerTwoName} two choice: ")

    if playerOneChoice.lower() in choices and playerTwoChoice.lower() in choices:
        if playerOneChoice == "paper" and  playerTwoChoice == "scissors":
            playerTwoScore += 1
        if playerOneChoice == "paper" and  playerTwoChoice == "rock":
            playerOneScore += 1
        if playerOneChoice == "scissors" and  playerTwoChoice == "paper":
            playerOneScore += 1
        if playerOneChoice == "scissors" and  playerTwoChoice == "rock":
            playerTwoScore += 1
        if playerOneChoice == "rock" and  playerTwoChoice == "paper":
            playerTwoScore += 1
        if playerOneChoice == "rock" and  playerTwoChoice == "scissors":
            playerOneScore += 1

        manche += 1

        print(f"{playerOneName}: {playerOneScore}")
        print(f"{playerTwoName}: {playerTwoScore}")

    else:
        print("Someone wants to cheat")
        continue

if playerOneScore > playerTwoScore:
    print(f"{playerOneName} won")
else:
    print(f"{playerTwoName} won")


tempCels = [15, 35, -2, 0, 15, 20]
tempFar = map(lambda temp: int((temp * 1.8) + 32), tempCels)

print(list(tempFar))


def power(base, exp):
    if exp == 1:
        return base
    return base * power(base, exp - 1)

print(power(3, 3))
'''

