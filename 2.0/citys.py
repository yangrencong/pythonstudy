prompt = "\n Please enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.)\t"
while True:
    city = input(prompt)
    print("\n")
    
    if city == 'quit':
        break
    else:
        print("I'd love to go to "+ city.title() + "!")
