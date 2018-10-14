import json


file_name = "number.json"
with open(file_name) as file_object:
    numbers = json.load(file_object)

print(numbers)
