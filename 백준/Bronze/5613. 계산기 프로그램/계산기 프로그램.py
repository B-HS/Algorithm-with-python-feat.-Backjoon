init = input()
while 1:
    tmp = input()
    if tmp =="=":
        break
    tmp2 = input()
    if tmp in "+-**=":
        init = str(eval(init+tmp+tmp2))
    elif tmp =='/':
        init = str(eval(init+tmp+tmp+tmp2))
print(init)