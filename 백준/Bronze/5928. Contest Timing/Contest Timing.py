a,b,c=map(int,input().split())
t = a*24*60 + b*60 + c
p = 11*24*60 + 11*60 + 11
ans = t-p
if ans < 0:
    print(-1)
else:
    print(ans)
