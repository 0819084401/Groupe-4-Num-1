# Saisie des notes avec validation
notes = []
for i in range(3):
    while True:
        note = float(input(f"Note {i+1}/3 (sur 20) : "))
        if 0 <= note <= 20:
            notes.append(note)
            break
        print("Erreur : la note doit être entre 0 et 20")

# Calcul de la moyenne
moyenne = sum(notes) / len(notes)

# Détermination du résultat
print(f"\nMoyenne : {moyenne:.2f}/20")
if moyenne >= 10:
    print("Résultat : Admis")
else:
    print("Résultat : Non admis")