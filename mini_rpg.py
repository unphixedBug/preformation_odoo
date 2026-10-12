import random

'''
Simulate 1000 games and display the average level reached.
'''

name = input("What's your name again? ")
level = 1
hp = int(input("How strong are you? In a numerical way (for intern facility...) "))
print("Here we go !")

while hp > 0:
    enemy_possibilities = [level - 1, level, level + 1]
    enemy_level = random.choice(enemy_possibilities)
    print("=================")
    print(f"An level {enemy_level} enemy !")
    print(f"Level {level} {name}: {hp}HP")

    if level >= enemy_level:
        print("Enemy defeated !")
        level += 1
        chance_of_healing = random.randint(1, 100)
        if chance_of_healing < 20:
          hp += 1
          print("You were healed by le Saint-Esprit !")
    else:
        print("Oh no...")
        hp -= 1

    print("Want to go deeper in this forest? ")
    forward = input("Yes - No ").lower()

    if forward == "yes" or forward == "y":
      continue
    elif forward == "no" or forward == "n":
      print("Oh... :(")
      hp = 0

print(f"High grass are too dangerous for you... You reached level {level}")