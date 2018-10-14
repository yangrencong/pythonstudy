#存储所点pizza内容信息
pizza = {
    'crust':'thick',
    'toppings':['mushrooms','extra cheese'],
    }

#概述所点pizza
print("You order a "+ pizza['crust'] + "-crust pizza"+
      "with the following topping:")
for topping in pizza['toppings']:
    print("\t"+ topping)
    
