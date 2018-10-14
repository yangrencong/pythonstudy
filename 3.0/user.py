current_users = ["zhao","qian","lei","sun","li"]

new_users   =   ["Wu","Zhou","zhao","Lei","ding"]

new_users_lower=[]
for new_user in new_users:
    new_users_lower.append(new_user.lower())
print(new_users_lower)
for new_user_lower in new_users_lower:
    if new_user_lower in current_users:
        print(new_user_lower+" 此名称已被使用，请更换")
    else:
        print(new_user_lower+"此用户名可正常使用")
