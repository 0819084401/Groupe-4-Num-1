import random

nombre_secret = random.randint(1, 100)
devine = 0

print("J'ai choisi un nombre entre 1 et 100. À vous de deviner !")

while devine != nombre_secret:
    try:
        devine = int(input("Votre proposition : "))
        if devine < nombre_secret:
            print("Trop petit !")
        elif devine > nombre_secret:
            print("Trop grand !")
        else:
            print(f"Bravo ! Vous avez trouvé le nombre {nombre_secret} !")
    except ValueError:
        print("Veuillez entrer un nombre valide.")