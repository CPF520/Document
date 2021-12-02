'''
需求：
1、猜的数字是系统产生的，不是自己定义的
2、键盘输入的   操作完填入：input（“提示”）
3、判断			操作完填入：if判断条件 elif 判断条件。。。。。。Else
4、循环			操作完填入：while 条件循环
任务：如果键盘输入大于随机数弹出友好提示信息“猜大了”，猜小了
起始金额  5000 才对一次给300 猜错扣除100 猜错15次结束

import random
#   随机生成数字  （开始int，结束int）  []
while True:
    Ran = random.randint(1, 20)
    num=input("请输入一个数字")
    num=int(num)
    #  键盘输入  随机数
    if num == Ran:
        print("猜对了")
        break
    else:
        print("猜错了")

i =input("请输入数字")
i=int(i)#等于号后面的是之前的变量，等于号前面的是新变量
if i == 1:
    print("ok")
elif i >4:
    print("ok2")
elif i<2:
    print("ok5")
else:
    print("no")

for
while



i=0
while i<12: # 条件为T F
    i=i+1#
    if i == 3:
        continue
    print(i)#打印i

    while循环  if如果  continue跳出此循环  break跳出整个循环  int取整  print打印  input默认为字符串类型 else否则 True对
    random开始.randint结束 input（“提示”）
'''
import random #导入模块
money=5000
I=15
B=0
print("持有现金:",money)
T = random.randint(1, 20)
while True:#这是一个循环
    print("正确答案:",T)
    E=input("请输入一个1-20的数字")
    E=int(E)
    if T == E:
        print("BING")
        money=money+3000
        print("持有现金:",money)
        T = random.randint(1, 20)
        continue
    else:
        print("Try Again")
        money=money-100
        I=I-1
        print("持有现金:",money)
        print("剩余次数:",I)
        if T > E:
            print("猜小了")
        else:
            print("猜大了")
    if I == B:
        print("GAME OVER")
        break



'''
i=0
while i<12:
    i=i+1
    if i==3:
        continue
    print(i)
'''
