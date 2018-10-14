def make_pizza(size , *toppings):
    """打印客户点的所有配料"""
    print("\nMake a " + str(size) +
          "-inch pizza with the following topping: ")
    print(toppings)
    for topping in toppings:
        print("- "+ topping)

