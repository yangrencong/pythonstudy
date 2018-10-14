import json
import types
def get_number():
    """如果用户存储了喜欢的数字，就获取他"""
    file_name = "favorate_number.json"
    try:
        with open(file_name) as file_object:
            f_number = json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return f_number

def get_new_number():
    """提示用户输入喜欢的数字"""
    while True:
        f_number = input("What,s your favorate number?")
        if f_number.isdigit():
            file_name = "favorate_number.json"
            with open(file_name,"w") as file_object:
                json.dump(f_number ,file_object)
            break
        else:
            print("Input error,Please enter the number")
    return f_number

def reply_user():
    """告诉用户最喜欢的数字"""
    f_number = get_number()
    if f_number:
        print("I konw your favorate number! It's "+ str(f_number) +" .")
    else:
        f_number = get_new_number()
        message="I will remember your favorate number is "+str(f_number)
        message += " when you come back!"
        print(message)

reply_user()
