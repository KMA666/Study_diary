x=int(input())
s=1
d=0
while d < 3:
    s = (s + 1) / ((100 - x) / 100)
    d += 1
print(f"猴子第1天摘得{s}个桃")
    