print("hey, guy!")
user_input = input("3")
print("Vous avez saisi le nombre ", user_input)
user_number = int(user_input)
for i in range(1, 10):
    print(f"{user_number} x {i} = {user_number * i}")
