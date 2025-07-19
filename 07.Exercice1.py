# Saisie de la liste de nombres (exemple de conversion de string en list d'int)
entree = input("Entrez des nombres séparés par des espaces : ")
liste_nombres = [int(x) for x in entree.split()]

n = len(liste_nombres)

# Algorithme de tri à bulles
for i in range(n):
    for j in range(0, n - i - 1):
        if liste_nombres[j] > liste_nombres[j+1]:
            liste_nombres[j], liste_nombres[j+1] = liste_nombres[j+1], liste_nombres[j]

print(f"Liste triée : {liste_nombres}")