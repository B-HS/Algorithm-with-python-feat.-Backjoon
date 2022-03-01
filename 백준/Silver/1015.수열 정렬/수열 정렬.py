num = int(input())
ary = list(map(int,input().split()))
temp = []
temp = ary
ary = sorted(ary)
for i in range(num):
    print(ary.index(temp[i]))
    ary[ary.index(temp[i])] = 0

