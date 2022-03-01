input = int(input())
ans = 0
tpool = []
num1 = 0
num2 = 0
num3 = 0
if 1000>input>99:
    ans = 99
    for i in range(100,input+1):
        for p in str(i):
            tpool.append(p)
        if len(tpool) >2:
            num1 = int(tpool[0])
            num2 = int(tpool[1])
            num3 = int(tpool[2])
            if int(num1-num2) == int(num2-num3):
                ans += 1
                tpool = []
            else:
                tpool = []    
elif input<100:
    ans = input
elif input == 1000:
    ans = 144
print (ans)