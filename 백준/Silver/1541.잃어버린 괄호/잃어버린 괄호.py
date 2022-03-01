ary = input().split('-')
sum = 0

for i in ary[0].split('+'):
    sum +=int(i)

for i in ary[1:]:
    for ii in i.split('+'):
        sum -=int(ii)
print (sum)