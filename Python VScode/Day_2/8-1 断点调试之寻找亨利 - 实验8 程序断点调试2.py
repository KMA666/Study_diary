names = ['Peter Anderson', '20240395', 'Tom Henry', 'Jack Lee']
sName = "NOTFOUND"
for x in names:
    if x.endswith("Henry"):
        sName = x
        break
    print(x, "not ends with 'Henry'.")

print("I found a Henry:", sName)