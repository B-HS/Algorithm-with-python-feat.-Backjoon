ary = [0, 1, 1]
for i in range(2, int(input())):
    ary.append(ary[i]+ary[i-1])
print(ary[-1])
