'''
购物商城：
    需求：购物商城
    1.商品
    2.金钱
    3.购物车

    买东西需求：
        看这个商品是不是存在
            若存在，您的余额是否购买这个东西
                将自己的余额减去商品的价格
                将这个商品添加购物车，
            余额不够，提示您的余额，穷鬼！选其他商品！
        若不存在：提示，您要的商品不存在
        是否是Q，q；
            结算，打印购物小条
有十张优惠券，系统初始化就会随机抽取一张优惠券，最后计算的时候进行打折。
'''
# 准备必备商品
import random
shop = [
    ["联想电脑", 6000],
    ["Iphone 16x plus", 15000],
    ["辣条", 3],
    ["手表", 2000],
    ["手机", 3000],
    ["耳机", 10],
    ["MAC PC", 10000]
]
shops = [
    ["联想电脑", 6000],
    ["Iphone 16x plus", 15000],
    ["辣条", 3],
    ["手表", 2000],
    ["手机", 3000],
    ["耳机", 10],
    ["MAC PC", 10000]
]
num1=random.randint(1,10)
print("恭喜获取%d张优惠卷"%num1)
num2=random.randint(1,10)
print("每张优惠卷为%d折"%num2)
num3=random.randint(0,8)
num4=shop[num3][0]
print("获取的优惠券为%s卷"%num4)

mycart = []  # 空的购物车

# 初始化余额
salary = input("请输入您的钱包余额：") # "356"  -->  356
sal = salary = int(salary)   # "356" --> 356


while True:
    # 展示商品架
    for key,value in enumerate(shop):
        print(key,value)

    chose = input("请输入您要买的商品编号：") # "9aa" --> 9
    if chose.isdigit():
        chose = int(chose)
        if chose >= len(shop):
            print("温馨提示：这个商品不存在！别瞎弄！")
        else:
            if num1 > 0 and chose == num3:
                shops[num3][1] = num2 * shop[num3][1] * 0.1
                num1 = num1-1
                print("剩余优惠券%x张"%num1)#剩余优惠券
                if salary < shops[chose][1]:
                    print("温馨提示：穷鬼，没钱，别瞎买！")
                else:
                    salary = salary - shops[chose][1]
                    mycart.append(shops[chose])
                    print(shops[chose][0],"添加购物车成功！余额还剩:￥",salary)
            else:
                if salary < shop[chose][1]:
                    print("温馨提示：穷鬼，没钱，别瞎买！")
                else:
                    salary = salary - shop[chose][1]
                    mycart.append(shop[chose])
                    print(shop[chose][0], "添加购物车成功！余额还剩:￥", salary)
    elif chose == "q" or chose == "Q":
        print("欢迎下次光临！")
        break  # 跳出循环
    else:
        print("兄弟，商品不存在！别瞎弄！")


# 打印购物小条

'''print("----------------欢迎下次光临Jason小商店--------------")
print("以下是您的购物小条，请拿好：")
print("--------------------------------------------------")
for key,value in enumerate(mycart):
    print(key,value)
print("-------------------------------------------------")
print("您本次还剩余额为：￥",salary,"，本次消费：￥",(sal - salary))'''


print("----------------欢迎下次光临小商店-------------------")
print("以下是您的购物小条，请拿好：")
print("--------------------------------------------------")
m = []
for i in mycart:
    if i not in m:
        m.append(i)
        print(" %s x %s " % (i, mycart.count(i)))
print("--------------------------------------------------")
print("您本次消费为：%d ，剩余余额：%d" % (sal-salary , salary))