ary = list(map(int, input().split()))

print(1 if ary[0]-ary[2] >= 2 and ary[1]-ary[3] >= 2 else 0)