matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Affichage de la matrice :")
for ligne in matrice:
    print(ligne)
print("\nAffichage élément par élément :")
for i, ligne in enumerate(matrice):
    for j, element in enumerate(ligne):
        print(f"Élément[{i}][{j}] : {element}")