"""
Renvoie le plus petit indice i tel que la somme des éléments à gauche de i égale la somme des éléments à droite de i (l’élément i n’est dans aucune des deux). 
Renvoie -1 s’il n’existe pas. O(n).

[1, 7, 3, 6, 5, 6] → 3 (gauche : 1+7+3 = 11 ; droite : 5+6 = 11)
[1, 2, 3] → -1
[2, 1, -1] → 0 (gauche : 0 ; droite : 1 + (-1) = 0)
[] → -1

Question guide : si tu connais la somme totale et la somme à gauche, comment obtiens-tu la somme à droite sans la recalculer ?
"""
def build_prefix(arr):
    prefix = [arr[0]]

    for i in arr:
        if i > len(arr):
            break

        prefix.append(arr[i] + arr)

    return prefix

def pivot_indices(arr):
    if len(arr) < 2:
        return -1

    index_equality = 0

    prefix_arr = build_prefix(arr)

    for i in range(1, len(prefix_arr)):
        if 

    return index_equality

print(pivot_indices([1, 7, 3, 6, 5, 6]))
print(pivot_indices([1, 2, 3]))
print(pivot_indices([2, 1, -1]))
print(pivot_indices([]))