import random
import time

## 创建卡池
card_tuple = ('武则天','嬴政','诸葛亮','宫本武藏','李白')
## 定义卡的权重
weight_list = (5, 10, 50, 50, 100)
## 定义用于比较的权重列表
weight_compare = (5, 15, 65, 115, 215)
## 创建背包
package_dic = {}

## 主程序
while 1:
    ## 接收用户的选择指令
    choose = int(input('''
    充值能让你变得更强！
    请选择指令：
    1. 抽卡
    2. 查看背包
    3. 离开
    '''))

    ## 当用户输入 1 时，先询问抽卡次数
    if choose == 1:
        num = int(input('输入抽卡次数：'))
        for i in range(0,num):
            int_Randcard = random.randint(1,weight_compare[-1])
            i = 0
            while int_Randcard > weight_compare[i]:
                i += 1
            print('你抽到的卡是:{}'.format(card_tuple[i]))
            
            if package_dic.__contains__(card_tuple[i]):
                package_dic[card_tuple[i]] += 1
            else:
                package_dic[card_tuple[i]] = 1

            time.sleep(0.3)

        # TODO

        ## 完成抽完后，提示卡已存入背包    
        print('卡已存入背包')
        print('________________')

    ## 当用户输入 2，打印背包内容
    if choose == 2:
        ## 分背包有卡片和背包没卡片两种情况
        if len(package_dic) == 0:
            print('背包暂无英雄，快去抽卡吧')
            print('________________')
        else:
            for key,value in package_dic.items():
                print('{} - 数量：{}'.format(key,value))
            print('________________')
            # TODO

    ## 当用户输入 3，退出程序
    if choose == 3:
        break

