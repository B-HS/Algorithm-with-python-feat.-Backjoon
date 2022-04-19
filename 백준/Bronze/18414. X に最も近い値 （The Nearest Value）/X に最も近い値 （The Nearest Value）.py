min = 1000001
ans = 0
a,b,c=map(int,input().split())
for i in range(b, c+1):
    if min > abs(a-i):
        min = abs(a-i)
        ans = i
print(ans)