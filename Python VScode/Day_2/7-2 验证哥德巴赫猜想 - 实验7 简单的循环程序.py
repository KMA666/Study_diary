#N=int(input())
#for p in range(N):
    #if(p==1):
    #    continue
    #if(p%2==0):
    #    continue
    #if(p%2==1):
   #     q=N-p
     #   if(q%p==0):
           # continue
     #   if(q%2==0):
       #     continue
    #    if(q%2==1):
  #          print(f"{N}={p}+{q}")
      #      break
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

N = int(input())
for p in range(2, N):
    q = N - p
    if is_prime(p) and is_prime(q):
        print(f"{N}={p}+{q}")
        break