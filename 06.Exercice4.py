mdp_correct = "Python2025"
mdp_saisi = ""

while mdp_saisi != mdp_correct:
    mdp_saisi = input("Entrez le mot de passe : ")
    if mdp_saisi != mdp_correct:
        print("Mot de passe incorrect. Veuillez réessayer.")
print("Mot de passe correct ! Accès autorisé.")