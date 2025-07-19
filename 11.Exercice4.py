def convertir_devise(montant_usd):
    eur = montant_usd * 0.93
    cfa = montant_usd * 610
    gbp = montant_usd * 0.79
    return eur, cfa, gbp

# Exemple d'utilisation
usd = float(input("Montant en USD à convertir : "))
euros, francs_cfa, livres_sterling = convertir_devise(usd)

print(f"{usd} USD = {euros:.2f} EUR")
print(f"{usd} USD = {francs_cfa:.2f} CFA")
print(f"{usd} USD = {livres_sterling:.2f} GBP")