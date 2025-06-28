a=input("请输入圆的半径：")
zhouchang=2*3.14*float(a)
mianji=3.14*float(a)**2
print("周长:{}, 面积:{}".format(zhouchang, mianji))

# 计算圆的周长和面积
# 输入圆的半径，计算周长和面积
# 输出结果
import math
r=eval(input("请输入圆的半径："))
fArea=math.pi*r**2
fPerimeter=2*math.pi*r
print("圆的面积为：{:.2f}".format(fArea))
print("圆的周长为：{:.2f}".format(fPerimeter))