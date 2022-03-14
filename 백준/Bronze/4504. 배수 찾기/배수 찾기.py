num = int(input())
while(1):
    tmp = int(input())
    if tmp == 0:
        break

    if tmp % num == 0:
        print(tmp, "is a multiple of", str(num)+".")
    else:
        print(tmp, "is NOT a multiple of", str(num)+".")
