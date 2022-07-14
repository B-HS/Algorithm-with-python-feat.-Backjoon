ans = 0
person = int(input())
ary = sorted([int(input()) for _ in range(person)])[::-1]
for i in range(person):
    tmp = ary[i]-i
    if tmp>-1:
        ans+=tmp
print(ans)