import math
d1=float(input())
d2=float(input())
r1=d1/2
r2=d2/2
V1=4/3*math.pi*r1*r1*r1
V2=4/3*math.pi*r2*r2*r2
V3=V1+V2
d3=V3**(1/3)
print(f"正方体边长为:{d3:.2f}.")