p, q = map(int, input().split())
ary = []
for i in range(1, p+1):
    if p % i == 0:
        ary.append(i)


if len(ary) >= q:
    print(ary[q-1])
else:
    print(0)
