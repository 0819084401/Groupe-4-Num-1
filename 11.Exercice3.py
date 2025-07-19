def est_palindrome(mot):
    # Nettoyer le mot (minuscules, sans espaces)
    mot_nettoye = ''.join(filter(str.isalnum, mot)).lower()
    return mot_nettoye == mot_nettoye[::-1]

# Exemples d'utilisation
print(f"'radar' est un palindrome : {est_palindrome('radar')}")
print(f"'Python' est un palindrome : {est_palindrome('Python')}")
print(f"'Engage le jeu que je le gagne' est un palindrome : {est_palindrome('Engage le jeu que je le gagne')}")