print("**************************")
'''
商品表
'''
print("************************")
print("*   momo的商城   *")
print("服装名称	价格/件	库存数量 销售量/每日")
print("\
羽绒服	253.6	500	10\n\
牛仔裤	86.3	600	60\n\
风衣	    96.8	335	43\n\
皮草	   135.9	855	63\n\
T血	    65.8	632	63\n\
衬衫	    49.3	562	120\n\
牛仔裤	86.3	600	72\n\
羽绒服	253.6	500	69\n\
牛仔裤	86.3	600	35\n\
羽绒服	253.6	500	140\n\
牛仔裤	86.3	600	90\n\
皮草	    135.9	855	24\n\
T血	    65.8	632	45\n\
风衣  	96.8	335	25\n\
牛仔裤	86.3	600	60\n\
T血	    65.8	632	129\n\
羽绒服	253.6	500	10\n\
风衣	    96.8	335	43\n\
T血	    65.8	632	63\n\
牛仔裤	86.3	600	60\n\
皮草	   135.9	855	63\n\
风衣	    96.8	335	60\n\
T血	    65.8	632	58\n\
牛仔裤	86.3	600	140\n\
T血	    65.8	632	48\n\
风衣	    96.8	335	43\n\
皮草	   135.9	855	57\n\
羽绒服	253.6	500	10\n\
T血	    65.8	632	63\n\
风衣	    96.8	335	78")

sum=(253.6*10+
86.3*60+
96.8*43+
135.9*63+
65.8*63+
49.3*120+
86.3*72+
253.6*69+
86.3*35+
253.6*140+
86.3*90+
135.9*24+
65.8*45+
96.8*25+
86.3*60+
65.8*129+
253.6*10+
96.8*43+
65.8*63+
86.3*60+
135.9*63+
96.8*60+
65.8*58+
86.3*140+
65.8*48+
96.8*43+
135.9*57+
253.6*10+
65.8*63+
96.8*78
      )

print("\n")
print("商品总额：",sum)


a=(10+
60+
43+
63+
63+
120+
72+
69+
35+
140+
90+
24+
45+
25+
60+
129+
10+
43+
63+
60+
63+
60+
58+
140+
48+
43+
57+
10+
63+
78)

print("\n")
print("平均每日数量",a/30)

Txue=(63+45+129+63+58+48+63)/1844
chenshan=(120)/1844
fengyi=(43+25+43+60+43+78)/1844
niuzaiku=(60+72+35+90+60+60+140)/1844
picao=(63+24+63+57)/1844
yurongfu=(10+69+140+10+10)/1844

print("每种种类占比：")
print("T恤",Txue*100,"%")
print("衬衫",chenshan*100,"%")
print("风衣",fengyi*100,"%")
print("皮草",picao*100,"%")
print("羽绒服",yurongfu*100,"%")