people_0 = {
    'name':'yang',
    'city':'beijing',
    'age':18,
    }
people_1 = {
    'name':'lei',
    'city':'xian',
    'age':23,
    }
people=[people_0,people_1]
for people_infor in people:
    print("\tName: "+ people_infor['name'])
    print("\tCity: "+ people_infor['city'])
    print("\tAge "  + str(people_infor['age'])+"\n")
