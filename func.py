'''
num1 = int(input("num 1: "))
num2 = int(input("num 2: "))

def apply_discount(price, discount):
    return (price / 100) * discount

print(apply_discount(num1, num2))

help(print)

# Write a function format_price(amount, currency="EUR", decimals=2) that returns a string such as "19.99 EUR". Add a docstring to document your function.
# Call it in 3 different ways: with only amount, with all positional arguments, and with keyword arguments in a different order. 
# Use the 'help' function to see your documentation.

def format_price(amount, currency = "EUR", decimals = 2):
    return f"{amount:.{decimals}f} {currency}"

print(format_price(19.5555))
print(format_price(19, "DLR"))
print(format_price(19.5454, decimals = 1, currency = "DLR"))
help(format_price)

def stats(numbers):
    sum = 0

    for num in numbers:
        sum += num

    return sum, sum / len(numbers), len(numbers)

sum, average, count = stats([2,4,6,8])

print(sum, average, count)

def build_profile(first_name, last_name, **details):
    result = details
    result["first_name"] = first_name
    result["last_name"] = last_name
    return result


print(build_profile("Phil", "Del", age=27, country="belgium"))
'''

