users = {
    'aeinstein':{
        'first':'albert',
        'last' :'einstein',
        'location':'princrton',
        },
    
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris',
        }
    }
for username,user_infor in users.items():
    print("\nUsername:   "+username)
    full_name = user_infor['first'] + user_infor['last']
    location  = user_infor['location']
    print("\tFull name: "+full_name.title())
    print("\tLocation: "+location.title())
