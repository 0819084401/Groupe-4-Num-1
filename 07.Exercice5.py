entree = input("Entrez des éléments séparés par des espaces : ")
liste_originale = entree.split()

liste_inversee = []
for i in range(len(liste_originale) - 1, -1, -1):
    liste_inversee.append(liste_originale[i])

print(f"Liste originale : {liste_originale}")
print(f"Liste inversée : {liste_inversee}")