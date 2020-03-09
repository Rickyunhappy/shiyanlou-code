##定义变量
salary = 0
shouldPay = 0
tax = 0
import sys

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
    ##获取id:income的每个元素
    for item in sys.argv[1:]:
        ##把id:income分割成两个元素
        id, income = item.split(':')
        ##定义可能的报错：无法将薪资转化为整数形式
        try:
            income = int(income)
        ##如果无法转化为整数，打印提示文字
        except ValueError:
            print('请在薪资位置输入数字')
            continue #跳过当前异常值
        print("{}:{}".format(id, calculator(income)))

if __name__ == '__main__':
    main()
