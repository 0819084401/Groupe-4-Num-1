texte = input("Entrez un texte : ").lower()
mot_cherche = input("Entrez le mot à chercher : ").lower()

# Utiliser count() pour compter les occurrences non superposées
count = texte.count(mot_cherche)

print(f"Le mot '{mot_cherche}' apparaît {count} fois dans le texte.")