input()
ary = map(int,input().split())
num = int(input())
ans = 0
for i in ary:
    if i == num:
        ans+=1
print(ans)