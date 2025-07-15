# Saisie du nombre
nombre = int(input("Entrez un nombre entier : "))

# Vérification de la divisibilité
divisible_par_3 = nombre % 3 == 0
divisible_par_5 = nombre % 5 == 0

if divisible_par_3 and divisible_par_5:
    print(f"{nombre} est divisible par 3 et 5 simultanément.")
elif divisible_par_3:
    print(f"{nombre} est divisible par 3 seulement.")
elif divisible_par_5:
    print(f"{nombre} est divisible par 5 seulement.")
else:
    print(f"{nombre} n'est divisible ni par 3 ni par 5.")