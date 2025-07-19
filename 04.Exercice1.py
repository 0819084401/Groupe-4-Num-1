age = int(input("Age : "))
statut = input("Statut (etudiant/salarie/retraite) : ").lower()

if age < 18:
    tarif = 5
else:
    if age <= 25:
        if statut == "etudiant":
            tarif = 6
        elif statut == "salarie":
            tarif = 8
        else:
            tarif = 10 # Pas d'info spécifique pour 18-25 non étudiant/salarié
    else:
        if statut == "retraite":
            tarif = 7
        else:
            tarif = 10

print(f"Tarif : {tarif} €")