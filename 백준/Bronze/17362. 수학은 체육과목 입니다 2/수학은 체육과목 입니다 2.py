ary = [[1], [2, 0], [3, 7], [4, 6], [5]]
mod = int(input()) % 8
for i in range(5):
    if mod in ary[i]:
        print(i+1)