# ===============================================
# Aufgabe: Hello World, Linear Search, Insertion Sort
# ===============================================

# 1️⃣ Hello World
print("Hello World")

# 2️⃣ Gegebene Liste
my_list = [7, 3, 10, 0, 5, 2, 8, 1, 4, 6, 9, 3, 15]

# 3️⃣ Linear Search Funktion
def linear_search(lst, target):
    """
    Sucht target in lst. Gibt Index zurück oder -1, wenn nicht gefunden.
    """
    for index, value in enumerate(lst):
        if value == target:
            return index
    return -1

# Test der Linear Search
number_to_find = 5
index_found = linear_search(my_list, number_to_find)
print(f"Linear Search: Zahl {number_to_find} gefunden an Index {index_found}")

# Test, was passiert wenn 14 gesucht wird
number_to_find = 14
index_found = linear_search(my_list, number_to_find)
if index_found == -1:
    print(f"Linear Search: Zahl {number_to_find} nicht in der Liste gefunden.")

# 4️⃣ Insertion Sort Funktion
def insertion_sort(lst):
    """
    Sortiert die Liste lst in-place mit Insertion Sort.
    """
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        # Verschiebe alle Elemente, die größer als key sind, nach rechts
        while j >= 0 and lst[j] > key:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key

# Test Insertion Sort
print(f"Ursprüngliche Liste: {my_list}")
insertion_sort(my_list)
print(f"Sortierte Liste: {my_list}")