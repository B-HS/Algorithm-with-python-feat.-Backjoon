ary = {}
for i in "abcdefghijklmnopqrstuvwxyz":
    ary[i] = 0

for i in input():
    ary[i] += 1

for i in "abcdefghijklmnopqrstuvwxyz":
    print(ary[i], end=" ")
