favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }
for name,language in favorite_languages.items():
    print(name.title()+"'s favorate language is "+language.title())
for key in favorite_languages.keys():
    print(key)
for value in favorite_languages.values():
    print(value)
print("\n")
friends = ['phil','sarah']
for name in favorite_languages.keys():
    print(name)

    if name in friends:
        print(" Hi "+ name.title() +
              ",I see your favorite languages is "+
              favorite_languages[name].title() + "!"+"\n"
              )
    else:
        print("\n")
if 'eric' not in favorite_languages.keys():
    print("Eric,please take our poll !")


print(sorted(favorite_languages.keys()))
