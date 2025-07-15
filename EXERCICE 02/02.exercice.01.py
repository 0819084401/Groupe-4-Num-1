# Saisie des deux nombres
a = float(input("Entrez le premier nombre : "))
b = float(input("Entrez le deuxième nombre : "))

# Calculs avec gestion de la division par zéro
operations = {
    "Somme": a + b,
    "Différence": a - b,
    "Produit": a * b,
    "Quotient": a / b if b != 0 else "Indéfini (division par zéro)",
    "Division entière": a // b if b != 0 else "Indéfini (division par zéro)",
    "Reste": a % b if b != 0 else "Indéfini (division par zéro)"
}

# Affichage des résultats
for operation, resultat in operations.items():
    print(f"{operation} : {resultat}")