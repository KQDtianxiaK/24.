import os
import random
import itertools
print('24点游戏解法程序')
a = eval(input('请输入第一位数字:'))
b = eval(input('请输入第二位数字:'))
c = eval(input('请输入第三位数字:'))
d = eval(input('请输入第四位数字:'))
list_four = []
def append(x):
    list_four.append(x)
append(a)
append(b)
append(c)
append(d)
result_list = []     #储存四个数全排列的列表
for i in set(itertools.permutations(list_four,len(list_four))):   # set() 用于去除重复的排列，itertools.permutations()用于生成全排列的各个组合
    result_list.append(list(i))
operator = ['+','-','*','//']
random.shuffle(operator)
result_list1 = []  #存储四个运算符的列表
for j in set(itertools.product(operator,repeat=  4)):
        templist = list(j)
        templist.pop()    #在实际运算过程中，4个数只需要3个运算符，删掉最后一个运算符，保留3个运算符
        if templist not in result_list1:
            result_list1.append(templist)
#存放各个符合条件的表达式
expression = []
expression_list = []
def calculate(x,y,m):
    global count
    count = 0     # 计数器
    for i in x:
        for j in y:
            expression1 = str(i[0]) + j[0] + str(i[1]) + j[1] + str(i[2]) + j[2] + str(i[3])    #将各个数都转化为str类型
           #捕获异常，此处可能出现的是除数为0的异常
            try:
                result = eval(expression1)
            except:
                result = 0
            if result == 24:
                m.append(expression1 + '=' + str(result))
                count += 1
            else:
                expression2 = '(' + str(i[0]) + j[0] + str(i[1]) + ')' + j[1] + str(i[2]) + j[2] + str(i[3])
                try:
                    result = eval(expression2)
                except:
                    result = 0
                if result == 24:
                    m.append(expression2 + '=' + str(result))
                    count += 1
                else:
                    expression3 = str(i[0]) + j[0] + '(' + str(i[1]) + j[1] + str(i[2]) + ')' + j[2] + str(i[3])
                    try:
                        result = eval(expression3)
                    except:
                        result = 0
                    if result == 24:
                        m.append(expression3 + '=' + str(result))
                        count += 1
                    else:
                        expression4 = str(i[0]) + j[0] + str(i[1]) + j[1] + '(' + str(i[2]) + j[2] + str(i[3]) + ')'
                        try:
                            result = eval(expression4)
                        except:
                            result = 0
                        if result == 24:
                            m.append(expression4 + '=' + str(result))
                            count += 1           #计算结果为24则计数+1
    return m
    return count
calculate(x=[list_four],y=result_list1,m=expression)
calculate(x=result_list,y=result_list1,m=expression_list)
print("解法如下：")
for each1 in expression:
    print(each1)                #列出此列数字所有解法
print('此列数字此顺序有{}种解法'.format(len(expression)))
for each2 in expression_list:
    print(each2)                #列出数字全排列后所有解法
print('此列数字一共有{}种解法'.format(count))
os.system('pause')
