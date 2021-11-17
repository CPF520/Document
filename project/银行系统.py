import random

# 银行的数据库
bank = {}
# 银行名称
bank_name = "中国工商银行昌平支行"


def welcome():
    print("---------------------------------------")
    print("-     中国工商银行账户管理系统V1.0      -")
    print("---------------------------------------")
    print("-  1.开户                             -")
    print("-  2.存钱                             -")
    print("-  3.取钱                             -")
    print("-  4.转账                             -")
    print("-  5.查询                             -")
    print("-  6.Bye!                             -")
    print("--------------------------------------")


# 银行的开户逻辑
def bank_addUser(account, username, password, country, province, street, door, money):
    if len(bank) > 100:
        return 3

    if username in bank:
        return 2

    # 正常开户
    bank[username] = {
        "account": account,
        "password": password,
        "country": country,
        "province": province,
        "street": street,
        "door": door,
        "money": money,
        "bank_name": bank_name
    }
    return 1


# 开户的输入数据
def addUser():
    username = input("请输入姓名：")

    password = input("请输入密码：")

    country = input("请输入国籍：")

    province = input("请输入省份：")

    street = input("请输入街道：")
    door = input("请输入您家门牌号：")

    money = int(input("请输入初始化您的银行卡余额："))

    account = random.randint(10000000, 99999999)

    status = bank_addUser(account, username, password, country, province, street, door, money)

    if status == 3:
        print("对不起，该银行用户已满，请携带证件到其他银行办理！")
    elif status == 2:
        print("您之前已经开过户！禁止重复开户！")
    elif status == 1:
        print("嘻嘻，开户成功！以下卡户的个人信息：")
        info = '''
            ------------个人信息查询结果-------------
            用户名：%s
            账号：%s
            密码：%s
            地址：
                国籍：%s
                省份：%s
                街道：%s
                门牌号：%s
            余额：%s
            开户行名称：%s
            ---------------------------------------
        '''

        print(info % (username, account, password, country, province, street, door, money, bank_name))
        print(bank)


# 银行存钱逻辑：
def bank_saveMone(ID, sum):
    for c in bank.keys():
        if ID != bank[c]["account"]:
            return False
        else:
            bank[c]["money"] = bank[c]["money"] + sum
            print("存钱成功！")


# 存钱输入数据：
def saveMoney():
    ID = int(input('请输入账号'))
    sum = int(input('请输入存钱的金额'))
    find = bank_saveMone(ID, sum)

    if find == False:
        print("该用户不存在！")


# 取钱逻辑
def bank_draw(number, coded, amt):
    for p in bank.keys():
        if number != bank[p]["account"]:
            return 1
        if coded != bank[p]["password"]:
            return 2
        if amt > bank[p]["money"]:
            return 3
        else:
            bank[p]["money"] = bank[p]["money"] - amt
            print("取钱成功")


# 取钱输入数据
def draw():
    number = int(input('请输入账号'))
    coded = input("请输入密码")
    amt = int(input("请输入取钱的金额"))
    find = bank_draw(number, coded, amt)

    if find == 1:
        print("账号不存在")
    if find == 2:
        print("密码不对")
    if find == 3:
        print("钱不够")


# 转账逻辑：
def bank_eft(rollout, lnto, rollpass, rollsum):
    for key, value in bank.items():
        if rollout != value['account'] and lnto != value['account']:
            return 1
        # else:
        #     print("该用户存在")
        if rollout == bank[key]['account']:
            if rollpass != bank[key]["password"]:
                 return 2
        # else:
        #     print("密码正确")
        if rollsum > bank[key]["money"]:
            print(bank[key]["money"])
            return 3
        # else:
        #    print("金额足够!")
        else:
            bank[key]["money"] = bank[key]["money"] - rollsum

        if lnto == bank[key]["account"]:
            bank[key]["money"] = bank[key]["money"] + rollsum
            return 4

# 转账输入的数据：
def eft():
    rollout = int(input('请输入转出账号'))
    lnto = int(input('请输入转入账号'))
    rollpass = input('请输入转出账号的密码')
    rollsum = int(input('请输入转出的金额'))
    find = bank_eft(rollout, lnto, rollpass, rollsum)

    if find == 1:
        print("不存在转出和转入的账号")
    elif find == 2:
        print("转出账号的密码不正确")
    elif find == 3:
        print("转账金额不足")
    elif find == 4:
         print("转账成功！")
    # print(bank)

while True:
    welcome()
    chose = input("请输入业务编号：")
    if chose == "1":
        addUser()
    elif chose == "2":
        saveMoney()
    elif chose == "3":
        draw()
    elif chose == "4":
        eft()
    elif chose == "5":
        print(bank)
    elif chose == "6":
        pass
