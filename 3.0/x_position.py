alien_0 = {'color':'green','x_position':0,'y_position':25,'speed':'fast'}
print(alien_0)
print("Original x_position:" + str(alien_0['x_position']))

#向右移动机器人
#根据机器人当前的速度决定其移动多远

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
elif alien_0['speed'] == 'fast':
    x_increment = 3 #这个机器人速度一定很快

#新的位置等于老位置加上增量
alien_0['x_position'] = alien_0['x_position'] +x_increment
print("New x_position: " + str(alien_0['x_position']))

#删除其中的color
del alien_0['color']
print(alien_0)
