ary = list(map(int,input().split()))
if sum(ary) <100:
    if ary.index(min(ary)) ==0:
        print("Soongsil")
        
    elif ary.index(min(ary)) ==1:
        print("Korea")
        
    elif ary.index(min(ary)) ==2:
        print("Hanyang")    
else:
    print("OK")