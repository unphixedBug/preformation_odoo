'''

sorted() prend un itérable et retourne une nouvelle liste triée. L'original n'est pas modifié (contrairement à list.sort() qui trie sur place).
 
sorted(iterable, key=None, reverse=False)

key : une fonction qui calcule la valeur utilisée pour comparer chaque élément.
reverse=True : tri décroissant.

numbers = [5, 2, 9, 1]
 
sorted(numbers)                 # [1, 2, 5, 9]
sorted(numbers, reverse=True)   # [9, 5, 2, 1]
print(numbers)                  # [5, 2, 9, 1]  -> inchangé
 
sorted("python")                # ['h', 'n', 'o', 'p', 't', 'y']
sorted(("b", "c", "a"))         # ['a', 'b', 'c']

 
Le paramètre key
words = ["banana", "fig", "apple"]
sorted(words, key=len)          # ['fig', 'apple', 'banana']

sorted() est stable : deux éléments égaux selon key gardent leur ordre d'origine.
 
---
 
Use case
Trier une liste de produits du moins cher au plus cher :
 
products = [
    {"name": "bread", "price": 1.29},
    {"name": "milk", "price": 0.95},
    {"name": "cheese", "price": 3.49},
]
 
by_price = sorted(products, key=lambda p: p["price"])
 
for p in by_price:
    print(p["name"], p["price"])
# milk 0.95
# bread 1.29
# cheese 3.49

 
---
Exercice : classement des magasins
Énoncé
 
Écris une fonction rank_stores(prices) qui reçoit un dictionnaire magasin -> prix et retourne la liste des magasins triés du moins cher au plus cher, sous forme de tuples (magasin, prix).
 
lidl milk 1L costs 0,99 €
aldi milk 1L costs 1,09 €
colruyt milk 1L costs 0,95 €
delhaize milk 1L costs 1,35 €

 
Résultat attendu
 
[("colruyt", 0.95), ("lidl", 0.99), ("aldi", 1.09), ("delhaize", 1.35)]

 
Contraintes
 
Utilise sorted() avec le paramètre key.
Si le dictionnaire est vide, retourne une liste vide.
Bonus
 
Retourne le classement du plus cher au moins cher.
Retourne uniquement les noms des 2 magasins les moins chers.
'''

stores_arg = [
    {"store": "lidl", "price": 0.99},
    {"store": "aldi", "price": 1.09},
    {"store": "colruyt", "price": 0.95},
    {"store": "delhaize", "price": 1.35},
]

def rank_stores(stores):
    if not stores:
        return []

    sorted_stores = sorted(stores.item(), key=lambda p: p["price"])

    for p in sorted_stores:
        print(p["name"])

print(rank_stores(stores_arg))