choix = -1

while choix != 0:
    print("\n--- MENU ---")
    print("1. Dire bonjour")
    print("2. Additionner deux nombres")
    print("0. Quitter")
    choix = int(input("Votre choix : "))

    if choix == 1:
        print("Bonjour !")
    elif choix == 2:
        a = float(input("Entrez le premier nombre : "))
        b = float(input("Entrez le deuxième nombre : "))
        print(f"La somme est : {a + b}")
    elif choix == 0:
        print("Au revoir !")
    else:
        print("Choix invalide. Veuillez réessayer.")