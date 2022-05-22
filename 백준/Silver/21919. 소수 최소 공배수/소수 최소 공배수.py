sosu = 1
input()
ary = set(map(int, input().split()))
def sosuni(num):
    for i in range(2, int(k**0.5)+1):
        if num % i == 0:return False
    return True
for k in ary:
    if sosuni(k) == True:sosu *= k
print(sosu if sosu != 1 else -1)