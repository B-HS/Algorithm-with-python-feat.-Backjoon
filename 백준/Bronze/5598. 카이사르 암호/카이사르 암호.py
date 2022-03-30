for i in input():
    print(chr(ord(i)+23) if ord(i)-3 < ord("A") else chr(ord(i)-3), end="")
