tmp = int(input())
while(1):
    if tmp % 4 == 0 and tmp != 0:
        tmp -= 4
        print("long", end=" ")
    else:
        print("int")
        break