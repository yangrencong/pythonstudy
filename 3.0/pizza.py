pizzas=['popizza','bbpizza','ccpizaa']
for pizza in pizzas:
    print("I like "+pizza.title())
print('I really love pizza')
print(pizzas)
friend_pizzas=pizzas[:]
print(friend_pizzas)
pizzas.append('caomei')
friend_pizzas.append('xigua')
print("my favorate food is:")
for pizza in pizzas:
    print(pizza)
print("my friend's favorate food is:")
for friend_pizza in friend_pizzas:
    print(friend_pizza)
