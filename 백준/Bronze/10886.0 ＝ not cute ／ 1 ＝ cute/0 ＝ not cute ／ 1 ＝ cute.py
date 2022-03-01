zero,one=0,0
for i in range(int(input())):
    tmp = int(input())
    if tmp ==0:
        zero +=1
    else:
        one+=1

print("Junhee is cute!" if zero<one else "Junhee is not cute!")