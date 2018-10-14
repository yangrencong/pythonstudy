research_info = {}

research_active = True

while research_active:
    research_name = input("\nWhat your name ? ")
    research_response = input("\nWhere would you go")
    
    research_info[research_name] = research_response
    
    repeat = input("Would you like to let another people repond ?(yes or no)")
    if repeat == "no":
        research_active = False

print("----- Research Results-----")
for name,response in research_info.items():
    print(name.title() + " would like to go " +response.title() + ".")
        
