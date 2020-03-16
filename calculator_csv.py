##定义变量
salary = 0
shouldPay = 0
tax = 0
import sys
import csv
import json

def calculator(num):
##减去五险一金
    shouldPay = num *(1-0.165) - 5000
    if shouldPay <= 0:
        tax = 0
    elif 0 < shouldPay <= 3000:
        tax = shouldPay * 0.03
    elif 3000 < shouldPay <= 12000:
        tax = shouldPay * 0.1 - 210 
    elif 12000 < shouldPay <= 25000:
        tax = shouldPay * 0.2 - 1410
    elif 25000 < shouldPay <= 35000:
        tax = shouldPay * 0.25 - 1410
    elif 35000 < shouldPay <= 55000:
        tax = shouldPay * 0.3 - 4410 
    elif 55000 < shouldPay <= 80000:
        tax = shouldPay * 0.35 - 7160 
    else:
        tax = shouldPay * 0.45 -15160 

    salary = num * (1-0.165) - tax
    return '{:.2f}'.format(salary)

##对命令行传入的每一个用户，依次调用计算器
def main():
    ##定义字典
    dic_data = dict()
    ##获取id，income的每个元素
    data_file = sys.argv[1]
    usr_csv = csv.reader(open(data_file))
    data_list = list(usr_csv)
    for item in data_list:
        ##把id,income分割成两个元素
        id, income = item[0],float(item[1])
        ##定义可能的报错：无法将薪资转化为整数形式
        try:
            income = int(income)
        ##如果无法转化为整数，打印提示文字
        except ValueError:
            print('请在薪资位置输入数字')
            continue #跳过当前异常值
        ##将结果存入字典
        dic_data[id] = calculator(income)
        
        print("{}:{}".format(id, calculator(income)))
        ##将字典存入json文件
    with open(sys.argv[2], 'w') as f:
        json.dump(dic_data,f)
                
        
        

if __name__ == '__main__':
    main()
