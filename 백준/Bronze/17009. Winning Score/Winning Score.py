ary = list(map(int, open(0)))
apples = ary[0]*3+ary[1]*2+ary[2]
bananas = ary[3]*3+ary[4]*2+ary[5]
if apples > bananas:
    print("A")
elif apples < bananas:
    print("B")
else:
    print("T")