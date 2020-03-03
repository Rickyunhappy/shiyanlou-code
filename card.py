card_turple = ('武则天','嬴政','诸葛亮','宫本武藏','李白') #卡池
package = [] #背包
import random #导入随机数

#主界面
while 1:
    choose = int(input('''
    充值能让你变得更强！
    请选择指令：
    1.抽卡
    2.查看背包
    3.整理背包
    4.离开
    '''))
    if choose == 1: #抽卡
        num = int(input('输入抽卡次数：'))
        #抽卡程序
        for i in range(0,num):
            n = random.randint(0,4)
            print('你抽到了:{}'.format(card_turple[n]))
        #放入背包
            package.append(card_turple[n])
        #提示抽卡完毕
        print('卡已存入背包')
        print('______________________')
           
    
    

    if choose == 2: #查看背包(分为有卡和无卡两种情况)
        if len(package) == 0:
            print('背包暂无英雄，快去抽卡吧')
            print('______________________')
        else:
            for i in package:
                print(i)
            print('______________________')


    if choose == 3: #整理背包(分为有卡和无卡两种情况)
        if len(package) == 0:
            print('背包暂无英雄，快去抽卡吧')
            print('______________________')
        else:
            package.sort()
            for i in package:
                print(i)
            print('______________________')

    if choose == 4:
        break







