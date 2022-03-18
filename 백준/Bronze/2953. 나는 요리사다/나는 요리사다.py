ary = []
for i in range(5):
    ary.append(sum(map(int,input().split())))
print(ary.index(max(ary))+1, max(ary))