import random  #调用随机函数
#创建一个储存外星人的空列表
aliens = []

#创建30个绿色外新人
for alien_number in range(30):
    new_alien = {'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)
    
#显示前五个机器人
for alien in aliens[:5]:
    print(alien)
print('...')

#显示创建了多少个机器人
print("Total number of aliens:" + str(len(aliens)))

#修改前3个机器人
for alien in aliens[0:5]:
    if alien['color'] == 'green':
        alien['color']  = 'yellow'
        alien['speed']  =  'medium'
        alien['points'] = 10
#显示前五个机器人
for alien in aliens[:5]:
    print(alien)
print('...')



#随机修改3个机器人为红色在30个中
for alien in random.sample(aliens,3):
    if alien['speed'] == 'slow':
        alien['color']  = 'red'
        alien['speed']  =  'fast'
        alien['points'] = 30
#显示前五个机器人
for alien in aliens[:29]:
    print(alien)
print('...')



























    
