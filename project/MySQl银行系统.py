import random
from DBUtils import update
from DBUtils import select

# 银行的数据库
bank = {}
# 银行名称
bank_name = "中国工商银行昌平支行"


def welcome():
    print("---------------------------------------")
    print("-      中国工商银行账户管理系统V1.0       -")
    print("--------------------------------------")
    print("-  1.开户                             -")
    print("-  2.存钱                             -")
    print("-  3.取钱                             -")
    print("-  4.转账                             -")
    print("-  5.查询                             -")
    print("-  6.Bye!                            -")
    print("--------------------------------------")


# 银行的开户逻辑
def bank_addUser(account, username, password, country, province, street, door, money):
    # 判断是否已满
    sql = "select count(*) from system"
    param = []
    data = select(sql, param, mode="one")  # (4,)
    if data[0][0] > 100:
        return 3
    # 查询是否存在
    sql1 = "select * from system where username  = %s"
    param1 = [username]
    data1 = select(sql1, param1, mode="all")  # ()

    # 判断是否开过户
    if len(data1) > 0:
        return 2

    # 插入数据
    sql2 = "insert into system values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    param2 = [account, username, password, country, province, street, door, money, "2021-11-22", bank_name]
    update(sql2, param2)
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
    sql = "select * from system where account=%s"
    param = [ID]
    data = select(sql, param, mode="all")
    # 判断 data是不是一个空元组（）   是空元组返回False  不是执行update_addmoney函数进行存钱操作
    if not data:
        print("该账号不存在！")
        return False
    else:
        sql1 = "update system set money = money+%s where account =%s"
        param1 = [sum,ID]
        update(sql1, param1)
        print("存钱成功！")


# 存钱输入数据：
def saveMoney():
    ID = int(input('请输入账号'))
    sum = int(input('请输入存钱的金额'))
    find = bank_saveMone(ID, sum)

    find == False


# 取钱逻辑
def bank_draw(number, coded, amt):
    sql = "select * from system where account=%s"
    param = [number]
    data = select(sql, param, mode="all")
    # 判断 data是不是一个空元组（）   是空元组返回1
    if not data:
        return 1
    if coded != data[0][2]:
        return 2
    if amt > data[0][7]:
        return 3
    else:
        sql1 = "update system set money=money-%s where account=%s and password=%s"
        param1 = [amt,number, coded]
        update(sql1, param1)
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


# 查询逻辑
def bank_query(af, bf):
    sql = "select * from system where account  = %s"
    param = [af]
    data = select(sql, param, mode="all")
    if not data:
        print("该用户不存在")
        return 1
    if bf != data[0][2]:
        return 2
    else:
            print("-------------查询的账号信息------------")
            print("用户名：", data[0][1])
            print("账号：", data[0][0])
            print("密码：", data[0][2])
            print("国籍：", data[0][3])
            print("省份：", data[0][4])
            print("街道：", data[0][5])
            print("门牌号：", data[0][6])
            print("余额：", data[0][7])
            print("开户日期：", data[0][8])
            print("开户银行：", data[0][9])


# 查询输入数据
def query():
    af = int(input("请输入用户账号"))
    bf = input("请输入密码")
    find = bank_query(af, bf)
    if find == 1:
        print("账号不存在")
    if find == 2:
        print("密码不对")



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
        pass
    elif chose == "5":
        query()
    elif chose == "6":
        pass
