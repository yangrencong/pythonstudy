def greet_users(names):
    """向每个列表中的每个用户都发出简单的问候"""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ["hannaha" ,"try" ,"margot"]
greet_users(usernames)
