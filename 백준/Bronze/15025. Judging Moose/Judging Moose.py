a = list(map(int, input().split()))

if a[0] == a[1]:
    if a[0] != 0:
        print("Even", a[0]*2)
    else:
        print("Not a moose")
elif a[0] != a[1]:
    print("Odd", max(a)*2)