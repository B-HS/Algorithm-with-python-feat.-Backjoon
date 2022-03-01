string = input()
word = string.upper()
count = 0
list = []
ans = [0 for _ in range(1000)]
for i in word:
    ans[ord(i)] += 1

for i in range(1000):
    if max(ans) == ans[i]:
        list.append(i)
if len(list) >1:
    print("?")
elif len(list) == 1:
    print(chr(list[0]))




