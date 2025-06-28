#import this     #本行的执行结果忽略不填写
#love = this 
#print(love is True)
#print(love is not True or False) 
#print(love==True) 
#print(bool(love)==True)
#print(id(this)==id(love))
#print(id(love)==id(True)) 
peter = ['10000','Peter Lee', 26, 'CEO']
dora = peter 
dora[1] = 'Dora Chen'
print("peter:",peter)
print("dora:",dora)
peter = ('10000','Peter Lee', 26, 'CEO')
dora = peter 
dora = ('10001','Dora Chen', 22, 'Sales')
print("peter:",peter)
print("dora:",dora)