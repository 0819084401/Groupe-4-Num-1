import math

try:
    nombre = float(input("Entrez un nombre pour calculer sa racine carrée : "))
    if nombre < 0:
        raise ValueError("Impossible de calculer la racine carrée d'un nombre négatif.")

    resultat = math.sqrt(nombre)
    print(f"La racine carrée de {nombre} est : {resultat}")
except ValueError as ve:
    print(f"Erreur de saisie : {ve}")
except Exception as e:
    print(f"Une erreur inattendue s'est produite : {e}")
finally:
    print("Fin de l'opération de calcul de racine carrée.")