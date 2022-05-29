t, tt, ttt = map(int, input().split(" : "))
s, ss, sss = map(int, input().split(" : "))

a1 = t*3600 + tt*60 + ttt
a2 = s*3600 + ss*60 + sss


print(a2-a1+3600*24 if a1 > a2 else a2-a1)