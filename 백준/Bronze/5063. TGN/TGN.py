for i in range(int(input())):
    a,b,c = map(int,input().split())
    if b-c == a:
        print("does not matter")
    elif b-c <a: 
        print("do not advertise")
    elif b-c >a:
        print("advertise")