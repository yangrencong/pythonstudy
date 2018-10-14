sandwich_orders = ["pastrami_sandwich","tomato_sandwich"    ,"pastrami_sandwich",
                   "potato_sandwich"  ,  "pastrami_sandwich","beef_sandwich",
                   "pastrami_sandwich"
                   ]
sandwich_finished = []
print("The pastrami has run up")
while "pastrami_sandwich" in sandwich_orders:
    sandwich_orders.remove("pastrami_sandwich")

for sandwichs in sandwich_orders:
    print(sandwichs)

while sandwich_orders:
    sandwich_order = sandwich_orders.pop()
    print("\tI made your "+ sandwich_order + ".")
    sandwich_finished.append(sandwich_order)
    
print("The following sandwichs had finished:")
for sandwich in sandwich_finished:
    print("\t"+sandwich)
