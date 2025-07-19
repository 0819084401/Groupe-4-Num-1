# Créer une liste vide pour stocker les carrés
liste_carres = []

# Générer les carrés des nombres de 1 à 20
for i in range(1, 21):
    liste_carres.append(i * i)

# Filtrer et afficher les carrés supérieurs à 100
print("Carrés supérieurs à 100 :")
for carre in liste_carres:
    if carre > 100:
        print(carre)