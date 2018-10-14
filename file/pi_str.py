file_name = "pi_million_digits.txt"
with open(file_name) as file_object:
    lines = file_object.readlines()

pi_str = ""
for line in lines:
    pi_str += line.strip()

birthday = input("Enter your birthday,in the form mmddyy:")
if birthday in pi_str:
    print("Your birthday appears in the first million digits of pil.")

else:
    print("Your birthday does notappears in the first million digits of pil.")
