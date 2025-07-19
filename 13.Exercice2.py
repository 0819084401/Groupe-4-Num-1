texte = input("Entrez un texte à convertir en entier : ")

try:
    entier = int(texte)
    print(f"Le texte '{texte}' a été converti en l'entier : {entier}")
except ValueError:
    print(f"Erreur : Impossible de convertir '{texte}' en entier.")