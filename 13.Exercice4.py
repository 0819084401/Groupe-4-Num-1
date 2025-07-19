nombre = -1
while True:
    try:
        saisie = input("Entrez un entier positif : ")
        nombre = int(saisie)
        if nombre >= 0:
            print(f"Vous avez saisi : {nombre}")
            break # Sortir de la boucle si la saisie est valide
        else:
            print("Veuillez entrer un nombre positif.")
    except ValueError:
        print("Saisie invalide. Veuillez entrer un entier.")