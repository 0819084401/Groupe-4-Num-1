notes = []
note = 0

print("Entrez les notes une par une. Entrez -1 pour terminer.")

while note != -1:
    try:
        note = float(input("Note : "))
        if note != -1:
            notes.append(note)
    except ValueError:
        print("Veuillez entrer un nombre valide.")

if notes:
    moyenne = sum(notes) / len(notes)
    print(f"La moyenne est : {moyenne:.2f}")
else:
    print("Aucune note n'a été saisie.")