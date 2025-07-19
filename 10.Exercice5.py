entree = input("Entrez des nombres séparés par des espaces : ")
liste_nombres = [int(x) for x in entree.split()]

# Extraire les éléments aux indices pairs (0, 2, 4, ...)
elements_pairs = liste_nombres[::2]

print(f"Éléments aux indices pairs : {elements_pairs}")