request_toppings = ['mushrooms','extra cheese']
if 'mushrooms' in request_toppings:
    print("Adding mushrooms.")
elif 'pepperoni' in request_toppings:#elif只会执行其中的一个模块
    print("Adding pepperoni.")       #if。。if可执行多个模块
elif 'extra cheese' in request_toppings:
    print("Adding extra cheese")
print("\nFinished making your pizzas!")
