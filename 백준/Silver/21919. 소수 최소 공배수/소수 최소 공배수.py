a=1
input()
b=set(map(int, input().split()))
def c(d):
    for i in range(2,int(k**0.5)+1):
        if d%i==0:return False
    return True
for k in b:
    if c(k)==True:a*=k
print(a if a!=1 else -1)