- short definition
- 2 exemples
- one situation when very useful

- create an exercise
- has to create a function using the builtin
- at least an exemple of input and output

# max()

## definition

when used on an iterable of numbers, returns the highest value
when used on an iterable of strings, returns the last string based on alphabetic order

## exemples

max(["Kayak", "Yakak"]) returns "Yakak"
max([1, 3, 67, 4, 34]) returns 67

it can be useful when you want to know who made the best score

---

# reversed()

## definition

returns an iterable starting from the end

## exemples

reversed([1, 2, 3]) returns [3, 2, 1]
reversed(["acheter du pain", "passer le balais", "regarder un film"]) returns ["regarder un film", "passer le balais", "acheter du pain"]

useful example: tasks are often added step by step (the one finished lately are in the end of a list) but we often want to display in an anti chronological order

---

# callable()

## definition

to know if an element is callable (an element is callable when we can have a value with () after it)

## exemples

def is_it():
    return "oui"

callable(is_it) returns True

example = 4

callable(example) returns False


---

# exercise

using the reversed built-in, create a function that displays the three last tasks you made

input: ["passer le balais", "faire la vaisselle", "avancer sur le projet web", "faire les courses"]
output: ["faire les courses", "avancer sur le projet web", "faire la vaisselle"]

def three_latest_done(tasks_done):
    backward_tasks = list(reversed(tasks_done))
    three_latest = []

    for i in range(3):
        three_latest.append(backward_tasks[i])

    return three_latest

print(three_latest_done(["passer le balais", "faire la vaisselle", "avancer sur le projet web", "faire les courses"]))



# exo rida

'''
Écris une fonction cheapest_store(prices) qui retourne le magasin où le même article (lait 1L) est le moins cher, ainsi que son prix.

lidl milk 1L costs 0,99 €
aldi milk 1L costs 1,09 €
colruyt milk 1L costs 0,95 €
delhaize milk 1L costs 1,35 €


Résultat attendu

cheapest_store(prices)   # ("colruyt", 0.95)


Contraintes

Utilise min() avec le paramètre key.
Si la liste est vide, retourne None (sans planter).

Bonus

Affiche le résultat formaté : Cheapest: colruyt at 0,95 €
Retourne aussi l'économie par rapport au magasin le plus cher.
'''

products = {
    "lidl": 0.99,
    "aldi": 1.09,
    "colruyt": 0.95,
    "delhaize": 1.35,
}

def cheapest_store(products):
    if not products:
        return

    cheapest = min(products, key=products.get)

    return f"Cheapest: {cheapest.capitalize()} at {products[cheapest]}€"

def most_expansive_store(products):
    if not products:
        return

    most_expansive = max(products, key=products.get)

    return f"Most expansive: {most_expansive.capitalize()} at {products[most_expansive]}€"

def savings_amount(products):
    if not products:
        return
    
    max_amount = 

print(cheapest_store(products))
print(most_expansive_store(products))