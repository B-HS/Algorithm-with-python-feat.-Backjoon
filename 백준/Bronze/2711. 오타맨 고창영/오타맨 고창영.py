for i in range(int(input())):
    where, word = input().split()
    word = list(word)
    word[int(where)-1] = ""
    print("".join(word))
