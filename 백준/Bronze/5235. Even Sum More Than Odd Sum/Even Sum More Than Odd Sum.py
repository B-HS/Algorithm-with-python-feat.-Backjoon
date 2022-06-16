for _ in range(int(input())):
    odd, even = 0, 0
    for k in list(map(int, input().split()))[1:]:
        if k % 2 == 0:
            even += k
        else:
            odd += k
    if even > odd:
        print("EVEN")
    elif even < odd:
        print("ODD")
    else:
        print("TIE")