# Taux de conversion (pourrait être dans un fichier config)
TAUX = {
    'EUR': 0.93,
    'CFA': 610,
    'GBP': 0.79
}

# Saisie du montant
usd = float(input("Montant en USD à convertir : "))

# Conversion et affichage
print("\nRésultats de conversion :")
for devise, taux in TAUX.items():
    montant_converti = usd * taux
    print(f"{usd:.2f} USD = {montant_converti:.2f} {devise}")