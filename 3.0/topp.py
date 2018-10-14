avaliable_toppings = ['mushrooms','olives','green peppers',
                      'pepperoni','pineapple','extra cheese']

request_toppings = ['mushrooms','french fries','extra cheese']

for request_topping in request_toppings:
    if request_topping in avaliable_toppings:
        print("Adding "+request_topping+".")
    else:
        print("sorry,we don't have "+request_topping+".")
print("\nFinish making your pizza")
