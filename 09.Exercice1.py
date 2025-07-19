texte = input("Entrez un texte : ")

# Retirer les espaces en trop (avant et après)
texte_nettoye = texte.strip()
# Convertir en minuscules
texte_minuscules = texte_nettoye.lower()
# Remplacer tous les points par des points d’exclamation
texte_final = texte_minuscules.replace('.', '!')

print(f"Texte nettoyé : {texte_final}")