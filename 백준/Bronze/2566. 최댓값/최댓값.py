ary = []
mx = 0

for i in range(9):
    ary.append(list(map(int,input().split())))
    
    if mx <= max(ary[i]):
        mx = max(ary[i])
        a = i + 1
        b = ary[i].index(mx) + 1

if mx !=0:
    print(mx)
    print(a, b)
else:
    print(0)
    print(1, 1)