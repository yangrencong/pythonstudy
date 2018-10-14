price_prompt = "请输入你的年龄"
price_prompt += "(输入0退出): "

age_message = ""

while True:
    age_message = int(input(price_prompt))
    if age_message == 0:
        break
    elif age_message<3:
        print("free\n")
    elif age_message<12:
        print("$10\n")
    else:
        print("$15\n")
