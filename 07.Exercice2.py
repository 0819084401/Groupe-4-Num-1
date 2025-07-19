entree = input("Entrez des éléments séparés par des espaces : ")
liste_elements = entree.split()

liste_unique = []
for element in liste_elements:
    if element not in liste_unique:
        liste_unique.append(element)

print(f"Liste avec valeurs uniques : {liste_unique}")