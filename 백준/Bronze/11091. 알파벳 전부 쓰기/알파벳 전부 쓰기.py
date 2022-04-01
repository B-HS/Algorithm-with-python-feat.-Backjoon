for i in range(int(input())):
    ary = list("abcdefghijklmnopqrstuvwxyz")
    for p in input():
        if p.lower() in ary:
            ary.pop(ary.index(p.lower()))
    if len(ary)==0:
        print("pangram")
    else:
        print("missing","".join(ary))

