print("hey, guy!")
user_input = input("3")
print("Vous avez saisi le nombre ", user_input)
user_number = int(user_input)
for i in range(1, 10):
    print(f"{user_number} x {i} = {user_number * i}")
while True:
    user_input = input("Veuillez entrer un nombre : ")
    print("Vous avez entré le nombre :", user-input)
    user_number = int(user_input)
    for i in range(1, 10):
        print(f"{user_number} x {i} = {user_number * i}")
    response = input("Fin de l'affichage. Appuyez sur R pour recommencer, ou sur une autre touche pour finir le programme: ")
    if response.lower() == "r":
        break