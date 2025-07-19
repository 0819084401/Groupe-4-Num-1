entree = input("Entrez des nombres séparés par des espaces : ")
liste_nombres = [float(x) for x in entree.split()]

if liste_nombres:
    maximum = max(liste_nombres)
    minimum = min(liste_nombres)
    moyenne = sum(liste_nombres) / len(liste_nombres)

    print(f"Maximum : {maximum}")
    print(f"Minimum : {minimum}")
    print(f"Moyenne : {moyenne:.2f}")
else:
    print("La liste est vide.")