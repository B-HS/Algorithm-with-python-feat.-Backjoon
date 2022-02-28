ary = []
for _ in range(7):
    tmp = int(input())
    if tmp % 2 != 0:
        ary.append(tmp)
if len(ary) == 0:
    print(-1)
else:
    print(sum(ary))
    print(min(ary))
