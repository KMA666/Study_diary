X=input()
N=int(input())
num=ord(X)
num1=num-64
word=chr(N+64)
print(f"{X}是字母表中第{num1}个字母.")
print(f"字母表中第{N}个字母是{word}.")