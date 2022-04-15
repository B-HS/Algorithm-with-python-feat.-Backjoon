ary = list(map(int,input().split()))
ary.append((ary[1]*ary[1])+(ary[2]*ary[2]))

for i in range(ary[0]):
    tmp = int(int(input()))
    if  tmp*tmp <= ary[1] or tmp*tmp <= ary[2] or tmp*tmp <= ary[3]:
        print("DA")
    else:
        print("NE")