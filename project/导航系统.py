'''
    导航系统：
        1.字典数据。
        2.方法的使用。

        1.退出：输入q或者Q
任务1：
    将旅游导航系统结合商城系统，集成开发！
    需求：
        当最终到达景点后，询问是否去买纪念品？
            xxxxXXXXxxxxxxxxxxx
'''

citys = {
    "北京": {
        "昌平": {
            "十三陵": ["十三陵水库"],
            "八达岭": ["八达岭长城", "野生动物园"],
            "回龙观": ["五道口切糕", "甑糕", "呷哺呷哺", "海底捞"]
        },
        "海淀": {
            "高校": ["清华", "北大"],
            "景点": ["香山", "植物园"]
        },
        "朝阳": {
            "公园": ["玉渊潭公园", "朝阳南北塔"]
        },
        "延庆": {
            "景点": ["龙庆峡"]
        }
    },
    "上海": {
        "浦东新区": {
            "叶榭市": ["外滩公园", "外滩"]
        }
    }
}


def showCity(citys):
    print("---------欢迎来到Jason旅游导航系统！-------------")
    for i in citys:
        print(i)
    print("---------------------------------------")


#
while True:
    showCity(citys)
    chose = input("请输入您想去的一级城市：")
    if chose == 'q' or chose == 'Q':
        print("--------------欢迎下次光临,拜拜嘞你嘞！-------------------")
        break  # 跳出循环
    if chose not in citys:
        print("温馨提示：当前城市没有项目！别瞎弄！")
    else:
        showCity(citys[chose])
        chose2 = input("请输入您想去的二级城市：")
        if chose2 == 'q' or chose2 == 'Q':
            print("--------------欢迎下次光临,拜拜嘞你嘞！-------------------")
            break  # 跳出循环
        if chose2 not in citys[chose]:
            print("都跟你讲了没有这个城市项目，别瞎弄！")
        else:
            showCity(citys[chose][chose2])
            chose3 = input("请输入您想去的三级城市：")
            if chose3 == 'q' or chose3 == 'Q':
                print("--------------欢迎下次光临,拜拜嘞你嘞！-------------------")
                break  # 跳出循环
            if chose3 not in citys[chose][chose2]:
                print("你故意找茬是不是？别瞎弄！")
            else:
                showCity(citys[chose][chose2][chose3])
                print("车已经达到！祝你玩的愉快！")
                print("目的地已到达是否购买纪念品？输入0进行参与，输入1不参与")
                shuru = int(input())
                import random

                if shuru == 0:
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
                    num1 = random.randint(1, 10)
                    print("恭喜获取%d张优惠卷" % num1)
                    num2 = random.randint(1, 10)
                    print("每张优惠卷为%d折" % num2)
                    num3 = random.randint(1, 8)
                    num4 = shop[num3][1]
                    print("获取的优惠券为%s卷" % num4)

                    mycart = []  # 空的购物车

                    # 初始化余额
                    salary = input("请输入您的钱包余额：")  # "356"  -->  356
                    sal = salary = int(salary)  # "356" --> 356

                    while True:
                        # 展示商品架
                        for key, value in enumerate(shop):
                            print(key, value)

                        chose = input("请输入您要买的商品编号：")  # "9aa" --> 9
                        if chose.isdigit():
                            chose = int(chose)
                            if chose >= len(shop):
                                print("温馨提示：这个商品不存在！别瞎弄！")
                            else:
                                if num1 > 0 and chose == num3:
                                    shops[num3][1] = num2 * shop[num3][1] * 0.1
                                    num1 = num1 - 1
                                    print("剩余优惠券%x张" % num1)  # 剩余优惠券
                                    if salary < shops[chose][1]:
                                        print("温馨提示：穷鬼，没钱，别瞎买！")
                                    else:
                                        salary = salary - shops[chose][1]
                                        mycart.append(shops[chose])
                                        print(shops[chose][0], "添加购物车成功！余额还剩:￥", salary)
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

                    print("----------------欢迎下次光临小商店-------------------")
                    print("以下是您的购物小条，请拿好：")
                    print("--------------------------------------------------")
                    m = []
                    for i in mycart:
                        if i not in m:
                            m.append(i)
                            print(" %s x %s " % (i, mycart.count(i)))

                    print("--------------------------------------------------")
                    print("您本次消费为：%d ，剩余余额：%d" % (sal - salary, salary))
                elif shuru == 1:
                    print("祝您旅途愉快")
