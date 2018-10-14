file_name = "user_message.txt"

polling_active = True

while polling_active:
    user_name = input("Please enter your name(enter q to quit):  ")
    if user_name != "q":
        print("Hello "+ user_name + " ")
        with open(file_name , "a") as file_object:
            file_object.write(user_name + "\n")
    else:
        polling_active = False
