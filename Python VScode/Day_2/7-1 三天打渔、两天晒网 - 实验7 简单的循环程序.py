wang=int(100)
guo=int(100)
N=int(input())
for i in range(N):
    guo=guo*1.001
num=N%5
step=N//5
i=int(1)
while step>0:
    wang=wang*1.002*1.002*1.002*0.999*0.999
    step-=1
if num==0:
    wang=wang
elif num==1:
    wang=wang*1.002
elif num==2:
    wang=wang*1.002*1.002
elif num==3:
    wang=wang*1.002*1.002*1.002
elif num==4:
    wang=wang*1.002*1.002*1.002*0.999
print("%.5f"",""%.5f" % (guo, wang))
