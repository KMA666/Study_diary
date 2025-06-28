year=int(input())
if(year%400==0):
    print("闰年")
else:
    if(year%400!=0 and year%100==0):
        print("平年")
    else:
        if(year%100!=0 and year%4==0):
            print("闰年")
        else:
            print("平年")