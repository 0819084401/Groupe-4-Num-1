nombre = int(input("Entrez un nombre entier positif : "))
factorielle = 1
i = 1

if nombre < 0:
    print("La factorielle n'est pas définie pour les nombres négatifs.")
elif nombre == 0:
    print("La factorielle de 0 est 1.")
else:
    while i <= nombre:
        factorielle *= i
        i += 1
    print(f"La factorielle de {nombre} est {factorielle}.")