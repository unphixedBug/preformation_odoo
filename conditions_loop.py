'''

# largest of three numbers

number1 = int(input("Enter number 1: "))
number2 = int(input("Enter number 2: "))
number3 = int(input("Enter number 3: "))

numbers = [number1, number2, number3]
numbers.sort()

print(f"Largest number is {numbers[-1]}")

---

# grade eval

userScore = int(input("What's your score ? "))

if userScore < 0 or userScore > 100:
    print("Invalid")
elif userScore < 60:
    print("Grade: F")
elif userScore < 69:
    print("Grade: D")
elif userScore < 79:
    print("Grade: C")
elif userScore < 89:
    print("Grade: B")
else:
    print("Grade: A")

---

# countdown

userInt = int(input("Gimme a positif num plz: "))

for i in range(userInt):
    print(f"{userInt - i}")

print("Liftoff!")

---

# multiplication table

userInt = int(input("Gemme an int plz: "))

for i in range(10):
    print(userInt * (i + 1))

---

# !! leap year !!

year = int(input("What year ? "))
is_a_leap_year = False

isDivBy4 = year % 4 == 0
isDivBy100 = year % 100 == 0
isDivBy400 = year % 400 == 0

if isDivBy4:
    if isDivBy400:
        is_a_leap_year = True

---

# fizzbuzz

upperLimit = int(input("Upper limit: ")) + 1

for i in range(1, upperLimit):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# fizzbuzz oneline

for i in range(1, int(input("Upper limit: ")) + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

---

# password check

password = "python123"
userAttempt = ""
attempts = 0
granted = False

while password != userAttempt and attempts < 3:
    userAttempt = input("Password: ")
    if userAttempt == password:
        granted = True
    attempts += 1

print(f"Access granted after {attempts} apptempt(s)." if granted else "Access denied and stop asking.")

---

# sum and average

nums = []

while True:
    user_num = int(input("Enter a number (0 to stop): "))
    nums.append(user_num)

    if user_num == 0:
        break

sum = sum(nums)
average = sum / (len(nums) - 1)

if nums[0] == 0:
    print("No numbers entered.")
else:
    print(f"Sum: {sum}")
    print(f"Average: {average}")

---

# factorial

user_num = int(input("Enter an positive integer: "))
result = 1

for i in range(user_num):
    result *= (i + 1)

print(result)

---

# !! triangle of stars

user_num = int(input("How many rows ? "))

for row in range(user_num):
    print("*" * (row + 1))

---

# !! prime num check

user_num = int(input("Enter an integer: "))
is_prime = True

for i in range(2, user_num):
    if user_num % i == 0:
        is_prime = False

print(f"{user_num} {"is a prime number" if is_prime else "isn't a prime number"}")

---

# !! fibonacci sequence

user_choice = int(input("How many terms ?"))
sequence = []

while len(sequence) < user_choice:
    if len(sequence) == 0:
        sequence.append(0)
    elif len(sequence) == 1:
        sequence.append(1)
    else:
        sequence.append(sequence[-2] + sequence[-1])

print(sequence)
'''

'''
Exercise 13: Fibonacci Sequence
Ask the user for a number of terms n, then display the first n terms of the Fibonacci sequence. Each term is the sum of the two previous ones, and the sequence starts with 0 and 1.

How many terms? 10
0 1 1 2 3 5 8 13 21 34
Bonus: Display only the Fibonacci numbers that are even.
'''



# !! leap year !!

year = int(input("What year ? "))
is_a_leap_year = False

isDivBy4 = year % 4 == 0
isDivBy100 = year % 100 == 0
isDivBy400 = year % 400 == 0

if isDivBy4:
    if not isDivBy100:


print(is_a_leap_year)