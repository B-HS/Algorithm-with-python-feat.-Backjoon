for i in range(int(input())):
    tmp = list(map(int,bin(int(input()))[2:][::-1].strip()))
    for p in range(len(tmp)):
        if tmp[p] ==1:
            print(p,end=" ")
    print("")
        