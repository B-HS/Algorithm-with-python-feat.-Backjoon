for i in range(int(input())):
    tmp=int(input())
    zero=[1,0,1]
    one=[0,1,1]
    if tmp >= 3:
        for i in range(3, tmp+1):
            zero.append(zero[i-1]+zero[i-2])
            one.append(one[i-1]+one[i-2])
    print(zero[tmp], one[tmp])