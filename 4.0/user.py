class User():
    """创建一个user类"""
    def __init__(self ,f_name ,l_name):
        self.f_name = f_name
        self.l_name = l_name
        self.login_attempts = 0

    def describle_user(self):
        name = self.f_name.title() +" "+self.l_name
        print("This user's name is "+ name + ".")

    def greet_user(self):
        name = self.f_name.title() +" "+self.l_name
        print("Hello "+name)

    def increment_login_attempts(self):
        self.login_attempts += 1

    def rest_login_attempts(self):
        self.login_attempts = 0

user1 = User("li","yangzi")
user1.describle_user()
user1.greet_user()
print("Login attempts: " +str(user1.login_attempts)+".")
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print("Login attempts: " +str(user1.login_attempts)+".")
user1.rest_login_attempts()
print("Login attempts: " +str(user1.login_attempts)+".")
