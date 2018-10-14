order_prompt = "请输入pizza的配料"
order_prompt += "(输入quit退出) : \t"
order_message = " "
while order_message != "quit":
    order_message=input(order_prompt)
    if order_message != 'quit':
        print("我们将会在菜单中加入 "+order_message+"\n")
    else:
        print("谢谢你的光临")
