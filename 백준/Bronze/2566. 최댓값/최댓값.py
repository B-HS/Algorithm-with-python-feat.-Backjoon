ary = []
for i in range(9):
    tmp = list(map(int, input().split()))
    ary.append(tmp)

mx = 0
where = 0

for i in range(9):
    if mx < max(ary[i]):
        mx = max(ary[i])
        where = i+1, ary[i].index(max(ary[i]))+1

print(mx)
for i in where:
    print(i, end=" ")
