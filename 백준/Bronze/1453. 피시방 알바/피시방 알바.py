ary = [0]*101
ans = 0
input()

for i in map(int,input().split()):
    if ary[i] ==0:
        ary[i]+=1
    else:
        ans+=1
print(ans)