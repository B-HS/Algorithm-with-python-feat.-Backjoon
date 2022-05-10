ary = list(map(int,open(0)))
if ary[0] == ary[1] and  ary[1] ==ary[2] and ary[2] == ary[3]:
    print("Fish At Constant Depth")
elif ary[0]<ary[1] and ary[1]<ary[2] and ary[2]<ary[3]:
    print("Fish Rising")
elif ary[0]>ary[1] and ary[1]>ary[2] and ary[2]>ary[3] :
    print("Fish Diving")
else:
    print("No Fish")