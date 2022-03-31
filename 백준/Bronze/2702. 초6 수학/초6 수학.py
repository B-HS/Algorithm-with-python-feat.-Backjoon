for i in range(int(input())):
    a, b = map(int,input().split())
    ab=a*b
    mx = 0
    tmp =0
    if a<b:
        tmp= a
        a=b
        b=tmp
    while(1):
        if a%b==0:
            mx = b
            break
        elif a%b!=0:
            tmp = a%b
            a=b
            b=tmp
    print(int(ab/mx), mx)
