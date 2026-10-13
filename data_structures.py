'''
print([n / 2 for n in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])
---
toolbox = ["Screwdriver", "Hammer", "Adjustable Wrentch"]
toolbox.append("Clé à molette")

to_remove = input("Tool to remove: ").lower()
toolbox.remove(to_remove) if to_remove in toolbox else print("Not in toolbox")

print(toolbox)
print(toolbox[2])
---
red = int(input("Red: "))
green = int(input("Green: "))
blue = int(input("Blue: "))

rgb = (red, green, blue)

print(f"Decimal: RGB{rgb}")
print(f"Hexadecimal: #{red:02X}{green:02X}{blue:02X}")
'''

'''
• If the user tries to remove or check an item that doesn't exist, print
a friendly error message instead of crashing.
'''

items = [
    { "name": "Example",
    "bought": False }
]

def doesnt_exist(item):
    print(f"{item} doesn't exist, check your spelling or you can check the list by clicking 3.")

def add_item():
    added_item = input("What item to add? ").lower()
    items.append({"name": added_item.capitalize(), "bought": False})

    menu()

def remove_item():
    removed_item = input("What item to remove? ").lower()
    is_in_the_list = False

    for item in items:
        if item["name"].lower() == removed_item.lower():
            items.remove(item)
            is_in_the_list = True
    
    if not is_in_the_list:
        doesnt_exist(removed_item)

    menu()

def view_list():
    for item in items:
        print(f"{item["name"]}: {"[x]" if item["bought"] else "[ ]"}")

    menu()

def check():
    item_to_check = input("Item to check / uncheck: ")
    is_in_the_list = False

    for item in items:
        if item["name"].lower() == item_to_check.lower():
            item["bought"] = not item["bought"]
            is_in_the_list = True

    if not is_in_the_list:
        doesnt_exist(item_to_check)
    menu()

def clear_list():
    if input("Are you sure? y/n") == "y":
        items.clear() 

    menu()

def quit():
    print("Byebye")

def menu():
    user_choice = int(input("""=== Shopping List Manager ===
    1. Add item
    2. Remove item
    3. View list
    4. Check / Uncheck item
    5. Clear list
    6. Quit
    """))

    match user_choice:
        case 1:
            add_item()
        case 2:
            remove_item()
        case 3:
            view_list()
        case 4:
            check()
        case 5:
            clear_list()
        case 6:
            quit()

menu()