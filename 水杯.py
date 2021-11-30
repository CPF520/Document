'''
分析一个水杯的属性和功能，使用类描述并创建对象
高度，容积，颜色，材质
能存放液体
'''

class Form:
    #定义添加属性
    __high = 0.0
    __cubage = 0
    __color = ""
    __texture = ""

    def sethigh(self, high):
        if high > 50 or high < 2:
            print("你好厉害哦，这都能喝")
        else:
            self.__high = high

    def setcubage(self, cubage):
        if cubage > 1000 and cubage <50:
            print("你真棒哇")
        else:
            self.__cubage = cubage
    def setcolor(self,color):
        if color == "":
            print("不是这个颜色")
        else:
            self.__color = color
    def settexture(self,texture):
        if texture =="":
            print("??")
        else:
            self.__texture = texture

    def heat(self):
        print(self.__color,self.__texture,"泡茶")


b = Form()

b.sethigh(25)

b.setcubage(500)

b.setcolor("黑色")

b.settexture("玻璃水杯")

b.heat()
