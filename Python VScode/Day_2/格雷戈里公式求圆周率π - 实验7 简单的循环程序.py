fError = 1e-6
iDenominator = 1
bAdd = True
fPi = 0.0
fItem = 1.0 / iDenominator
while fItem>=fError:    
    fPi = (fPi+fItem) if bAdd else (fPi-fItem)#可以使用条件表达式
    iDenominator += 2
    fItem = 1.0/iDenominator
    bAdd = not bAdd
print("pi = %.15f" % (fPi*4.0))