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

num1=random.randint(0,10)
print("恭喜你幸运的获得了%d张优惠券"%num1)
num2=random.randint(0,8)
print('每张优惠券折扣为%d折'%num2)
num3= random.randint(0, 8)  # 随机获取vshop中的一种商品为折扣商品
num4= shop[num3][0]
print("获取的优惠券为%s卷" % num4)

# 空的购物车
mycart = []
# 初始化自己的余额
salary = input("请输入您的余额")
sal = salary = int(salary)

# 展示超市商品：角标+数据

# 买东西
while True:
    for index, value in enumerate(shop):
        print(index, value)
    chose = input("请输入您的商品编号：")
    if chose.isdigit():  #看chose能否被看成数字
        chose = int(chose)
    # 判断商品是否存在
        if chose < len(shop):

            # 判断余额是否足够
            if salary >= shop[chose][1]:
                # 正常买东西
                mycart.append(shop[chose])
                # 减去金额
                salary = salary - shop[chose][1]
                print("恭喜，添加成功！您的余额还剩：￥", salary)
            else:
                print("穷鬼，钱不够，请选择其他商品")

    elif chose == "Q" or chose == "q":
        print("欢迎下次光临，再见")
        break
    else:
        print("对不起，您的输入有误，请重新输入")

# 打印购物小条
for index, value in mycart:
    print(index, value)


# 打印购物小条
print("----------------欢迎下次光临Jason小商店--------------")
print("以下是您的购物小条，请拿好：")
print("--------------------------------------------------")
# for key,value in enumerate(mycart):
#     print(key,value)
myct = []

for i in mycart:
    if i not in myct:
        myct.append(1)
        print(" %s x %s " % (i, mycart.count(i)))
print("-------------------------------------------------")
print("您本次还剩余额为：￥", salary, "，本次消费：￥", (sal - salary))
