import json

def get_stored_username():
    """如果用户存储了用户，就获取他"""
    file_name = "username.json"
    try:
        with open(file_name) as file_object:
            username = json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    username = input("What's your name？: ")
    file_name = "username.json"
    with open(file_name ,"w") as file_object:
        json.dump(username ,file_object)
    return username

def renovate_username():
    user_name = input("Hello，please enter your new name !")
    file_name = "username.json"
    with open(file_name,"w") as file_object:
        json.dump(user_name,file_object)
    return user_name




def greet_user():
    """问候用户，并指出其姓名"""
    username = get_stored_username()
    
    
    if username:
        user_reply = input("Is your name called "+username +" ?(yes or no)")
        if user_reply == "yes":
            print("Welcome back " +username +" !")
            
        else:
            username =renovate_username()
            print("We'll remember you when you come back "+ username +" !")
    else:
        username = get_new_username()
        print("We'll remember you when you come back "+ username +" !")

greet_user()
