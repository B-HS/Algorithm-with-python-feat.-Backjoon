target = int(input())
ans = 0
for i in map(int,input().split()):
    if target == i:
        ans+=1
print(ans)