while(1):
    a, b, c  = map(int,input().split())
    if a==0 and b == 0 and c ==0:
        break

    if b-a == c-b:
        print("AP", c+(b-a))
    elif b//a == c//b:
        print("GP", c*(b//a))