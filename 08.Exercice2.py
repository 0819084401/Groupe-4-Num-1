entree = input("Entrez des éléments séparés par des espaces : ")
liste_elements = entree.split()

print("Éléments avec leurs indices :")
for index, element in enumerate(liste_elements):
    print(f"Indice {index} : {element}")