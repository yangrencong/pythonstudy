import json

numbers =[0,2,3,4,5,6,13 ]

file_name = "number.json"
with open(file_name ,"w") as file_object:
    json.dump( numbers, file_object)
