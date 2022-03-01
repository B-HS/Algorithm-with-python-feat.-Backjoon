num = int(input())
ary = list(map(int,input().split()))
count = 0
ans = 0

if 1 in ary:
    ary.pop(ary.index(1))

for i in ary:
    for z in range(1, i+1):
        if i/z == 1 or i/z == i:
            count +=1
        elif i%z == 0:
            count +=1        
    if count == 2 :
        ans +=1
    count = 0
print (ans)