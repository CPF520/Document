'''
1、猜的数字是系统产生，不是自定义
        使用random随机数技术来获取随机数
范围：0~100
    猜10次！
    如果输入大了：温馨提示：大了
    如果输入小了：温馨提示：小了
    正好猜中，恭喜您，猜中，本次猜的数字为XXX
操作完成之后才增加：
    起始：5000金币，每猜错一次，减去500金币，一直扣完为止。10次没猜中，系统锁定。猜中加3000。
'''

import random

C = random.randint(0, 100)
print(C)
gold = 5000
print("您的初始金币为：5000" ,end=",")
print("猜对加3000，猜错减500，您共有10次机会")
i = 1
while i <= 10:
    num = input("请输入你猜的数字")
    num = int(num)
    if num == C:
        gold += 3000
        print("恭喜您猜中，本次的数字为 %d" % C)
        print("ok")
    elif C < num:
        gold += 500
        print("您输入的数字太大了")
    else:
        gold -= 500
        print("您输入的数字太小了")
else:
    print("no")
    i = i + 1
