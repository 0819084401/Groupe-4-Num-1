# Saisie des données
montant_ht = float(input("Montant HT (€) : "))
taux_tva = float(input("Taux de TVA (%) : "))

# Calculs
taux_coef = taux_tva / 100  # Conversion % → décimal
montant_tva = montant_ht * taux_coef
montant_ttc = montant_ht + montant_tva

# Affichage détaillé
print("\nDétail du calcul :")
print(f"Montant HT : {montant_ht:.2f} €")
print(f"TVA ({taux_tva}%) : {montant_tva:.2f} €")
print(f"Montant TTC : {montant_ttc:.2f} €")