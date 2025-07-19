mot = input("Entrez un mot d'au moins 5 lettres : ")

if len(mot) >= 5:
    # On enlève les 2 premières et 2 dernières lettres
    milieu = mot[2:-2]
    print(f"Partie centrale : {milieu}")
else:
    print("Le mot doit avoir au moins 5 lettres.")