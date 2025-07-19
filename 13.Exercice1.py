try:
    num1 = float(input("Entrez le numérateur : "))
    num2 = float(input("Entrez le dénominateur : "))

    resultat = num1 / num2
    print(f"Le résultat de la division est : {resultat}")
except ZeroDivisionError:
    print("Erreur : Division par zéro impossible.")
except ValueError:
    print("Erreur : Veuillez entrer des nombres valides.")