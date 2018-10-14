favorite_number={}
favorite_number['li'] = 6
favorite_number['sun']= 8
favorite_number['zhang']= 10
favorite_number['lei'] = 100
favorite_number['ding'] = 20
print(favorite_number)

for key,value in favorite_number.items():
    print("\n "+key.title()+" favorite number is "+str(value))
