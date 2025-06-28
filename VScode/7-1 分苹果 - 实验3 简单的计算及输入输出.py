apple1=int(input())
left=apple1%5
apple2=int((apple1-left)/5)
print(f"每人分得{apple2}个苹果.")
print(f"一共分出去{apple1-left}个苹果.")
print(f"交还老师{left}个苹果.")
