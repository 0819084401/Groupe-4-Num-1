entree = input("Entrez des éléments séparés par des espaces : ")
liste_originale = entree.split()

liste_inversee = liste_originale[::-1]

print(f"Liste originale : {liste_originale}")
print(f"Liste inversée (slicing) : {liste_inversee}")