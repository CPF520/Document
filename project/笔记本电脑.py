'''
有笔记本电脑（屏幕大小，价格，cpu型号，内存大小，待机时长），行为（打字，打游戏，看视频）
'''


class Form:
    __screen = 0
    __price = 0
    __cpu = ""
    __memory = 0
    __standby = 0

    def setScreen(self, screen):
        if screen > 30 or screen < 12:
            print("你这电脑咋玩呢")
        else:
            self.__screen = screen

    def getScreen(self):
        return self.__screen

    def setprice(self, price):
        if price < 100 or price > 100000:
            print("厉害了大哥")
        else:
            self.__price = price

    def getprice(self):
        return self.__price

    def setcpu(self, cpu):
        if cpu == "":
            print("型号不正确")
        else:
            self.__cpu = cpu

    def setmemory(self, memory):
        if memory > 20000 or memory < 100:
            print("你电脑真厉害")
        else:
            self.__memory = memory

    def getmemory(self):
        return self.__memory

    def setstandby(self, standby):
        if standby > 24 or standby < 1:
            print("电脑电力过低或过高")
        else:
            self.__standby = standby

    # 行为
    def type(self, minute):
        print(self.__cpu, "打字速度", minute)

    def playGame(self, gameName, ):
        print(self.__cpu, "可以玩【", gameName, "】")

    def watchVideo(self, hour):
        print(self.__cpu,"正在播放电视，已经播放了", hour, "小时")

    def showMe(self):
        print("此电脑屏幕大小为", self.__screen, "寸,价格", self.__price, "元,中央处理器是", self.__cpu, "内存大小", self.__memory, "可待机",
              self.__standby, "小时")


d = Form()
# 屏幕大小
d.setScreen(15)
# 价格
d.setprice(5500)
# 型号
d.setcpu("英特尔PXA系列处理器")
# 内存大小
d.setmemory(10000)
# 待机时长
d.setstandby(3)

d.type("200/min")
d.playGame("各种游戏", )
d.watchVideo(10)
d.showMe()
