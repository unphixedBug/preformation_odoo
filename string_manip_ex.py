'''
# reverse a string

user_str = input("Enter a word")
str_len = len(user_str)
result = ""

for i in range(str_len - 1, -1, -1):
    result += user_str[i]

print(result)

---

# vowels count

user_str = input("Enter a text: ").lower()
vowels = "aeiouy"
total = 0

for char in user_str:
    if char in vowels:
        total += 1

print(f"Number of vowels: {total}")

---

# capitalize each word

user_str = input("Enter a sentence: ").lower()
words = user_str.split()
capitalized_words = []

for word in words:
    capitalized_words.append(word.capitalize())

print(" ".join(capitalized_words))

---

# palindrome checker

user_str = input("Enter a text: ")
str_len = len(user_str)
reverse_str = ""

for i in range(str_len - 1, -1, -1):
    reverse_str += user_str[i]

print("It is a palindrome!" if reverse_str == user_str else "It is not a palindrome")

# remove duplicate char

user_str = input("Enter a text: ")
result = ""

for char in user_str:
    if char not in result:
        result += char

print(result)

---

# most frequent char

user_str = input("Enter a text: ").lower().replace(" ", "")
user_str_set = set(user_str)

most_used_char = user_str[0]
number_of_uses = 1

for set_char in user_str_set:
    actual_count = 0

    for user_char in user_str:
        if set_char == user_char:
            actual_count += 1
    
    if actual_count > number_of_uses:
        number_of_uses = actual_count
        most_used_char = set_char

print(most_used_char, number_of_uses)

---

# anagram checker

user_str_1 = list(input("First text: ").lower().replace(" ", ""))
user_str_2 = list(input("Second text: ").lower().replace(" ", ""))
is_anagram = False

print(user_str_1, user_str_2)

for char in user_str_1:
    if char in user_str_2:
        user_str_2.remove(char)
    else:
        break

if len(user_str_2) == 0:
    is_anagram = True

print(f"Anagrams: {is_anagram}")

---

# !! ceaser cipher


# !! string compar

user_str = input("Enter a text: ").lower()
result = ""

actual_count = 1

for i in range(len(user_str)):
    if i > len(user_str):
        result += user_str[i] + str(actual_count)
        continue
    else:
        if user_str[i + 1] == user_str[i]:
            actual_count += 1
        else:
            result += user_str[i] + str(actual_count)
            actual_count = 1

print(result)

# longest substr without repeating char

user_str = input("Enter a text: ")

longest_substr = ""
longest_substr_size = 0

actual_substr = ""
actual_score = 0

for i in range(len(user_str)):
    if user_str[i] not in actual_substr:
        actual_substr += user_str[i]
        actual_score += 1
    else:
        if actual_score > longest_substr_size:
            longest_substr_size = actual_score
            longest_substr = actual_substr
        actual_score = 0
        actual_substr = ""
        i -= 1

print(f"Length: {longest_substr_size}")
print(f"Substring: {longest_substr}")
'''

'''
'''