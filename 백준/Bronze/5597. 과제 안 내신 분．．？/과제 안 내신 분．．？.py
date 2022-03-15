ary={i for i in range(1, 31)}
ans=[]
for i in range(28):
    tmp = int(input())
    if tmp in ary:
        ary.remove(tmp)
print(sorted(list(ary))[0])
print(sorted(list(ary))[1])