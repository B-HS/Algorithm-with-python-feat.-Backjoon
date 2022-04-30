for i in range(int(input())):
    ary = sorted(list(map(int,input().split())))
    if (ary[0]**2)+(ary[1]**2) == ary[2]**2:
        print("Scenario #"+str(i+1)+":")
        print("yes")
    else:
        print("Scenario #"+str(i+1)+":")
        print("no") 
    print("")
    ary = ""