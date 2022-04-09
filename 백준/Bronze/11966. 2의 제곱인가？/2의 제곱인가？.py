num = int(input())
tmp = 1
for _ in range(32):
    if tmp == num:
        print(1)
        exit(0)
    else:
        tmp *= 2
print(0)
