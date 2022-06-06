while 1:
    tmp = input()
    if tmp == "#":
        break
    ans = 0
    for i in tmp:
        if i.lower() in "aeiou":
            ans += 1
    print(ans)
