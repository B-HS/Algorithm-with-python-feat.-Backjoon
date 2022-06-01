ary = list(map(int, open(0)))
k = [8, 9]
if ary[0] in k and ary[-1] in k and ary[1] == ary[2]:
    print("ignore")
else:
    print("answer")