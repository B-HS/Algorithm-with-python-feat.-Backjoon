deck= ["D", "C", "B","A","E"]
for i in range(3):
    ary= list(map(int,input().split()))
    print(deck[sum(ary)])