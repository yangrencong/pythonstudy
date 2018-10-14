file_name = "pi_digits.txt"

with open(file_name) as file_object:
    lines = file_object.readlines()

pi_str = ""
for line in lines:
    pi_str += line.strip()

print(pi_str)
print(len(pi_str))
