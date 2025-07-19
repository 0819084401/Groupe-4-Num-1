texte = input("Entrez un texte : ")
consonnes = ""
voyelles = "aeiouAEIOU"

for char in texte:
    if char.isalpha() and char not in voyelles:
        consonnes += char

print(f"Consonnes dans le texte : {consonnes}")