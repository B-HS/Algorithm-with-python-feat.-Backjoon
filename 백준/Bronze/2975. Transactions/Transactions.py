result = 0
while(1):
    ary = list(input().split())
    if ary == ["0", "W", "0"]:
        break
    if ary[1] == "W":
        result = int(ary[0])-int(ary[2])
    elif ary[1] == "D":
        result = int(ary[0])+int(ary[2])

    if result < -200 and ary[1] == "W":
        print("Not allowed")
        continue
    else:
        print(result)
