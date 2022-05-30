ary = [input() for _ in range(6)]
i = ary.count('W')
if i >= 5:
    print(1)
elif i >= 3:
    print(2)
elif i >= 1:
    print(3)
else:
    print(-1)