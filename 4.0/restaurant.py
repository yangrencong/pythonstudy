class Restaurant():
    """创建一个汽车的类"""
    def __init__(self ,res_name,cui_type):
        """初始化属性"""
        self.res_name = res_name
        self.cui_type = cui_type
        self.number_served = 0

    def describle_restaurant(self): #不要丢失self
        print("The restaurant's name is "+self.res_name.title() + ".")

    def open_restaurant(self):
        print("The restaurant's type is "+self.cui_type.title() +".")

    def restaurant_number(self):
        print("Number served: "+str(self.number_served) +" ")

    def set_number_served(self ,set_number):
        self.number_served = set_number
        print("Number served: "+str(self.number_served) +" ")

    def increment_number_served(self ,increment_number):
        self.number_served += increment_number
        print("Number served: "+str(self.number_served) +" ")
        

my_restaurant = Restaurant("hah","chinese food")

my_restaurant.open_restaurant()
my_restaurant.describle_restaurant()
my_restaurant.restaurant_number()
my_restaurant.set_number_served(30)
my_restaurant.increment_number_served(20)
