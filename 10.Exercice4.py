numero = input("Entrez un numéro (ex. 0897654321) : ")

if len(numero) >= 3:
    # Masquer tout sauf les 3 derniers chiffres
    numero_masque = '*' * (len(numero) - 3) + numero[-3:]
    print(f"Numéro masqué : {numero_masque}")
else:
    print("Le numéro doit contenir au moins 3 chiffres.")