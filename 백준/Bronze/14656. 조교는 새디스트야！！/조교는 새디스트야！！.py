num=int(input())
ary=list(map(int,input().split()))
ans=0
for i in range(num):
    if ary[i] !=i+1:
        ans+=1
print(ans)