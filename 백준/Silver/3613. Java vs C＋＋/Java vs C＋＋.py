def its_j(st):
    ans = st[0]
    if ans.isupper():
        return 'Error!'
    for i in range(1, len(st)):
        if st[i].isupper():
            ans += "_"
            ans += st[i].lower()
        else:
            ans += st[i]
    return ans


def its_c():
    for i in range(1, len(list(ary))):
        if ary[i-1] == ary[i] == '_':
            return 'Error!'
    if ary[0] == '_' or ary[-1] == '_':
        return 'Error!'
    sndcheck = ary.split('_')

    for i in sndcheck:
        if not i.isalnum():
            return 'Error!'
        if i.lower() != i:
            return "Error!"
    for i in range(len(sndcheck)):
        if sndcheck[i][0].lower() != sndcheck[i][0]:
            return 'Error!'
    for i in range(1, len(sndcheck)):
        sndcheck[i] = sndcheck[i].capitalize()
    return ''.join(sndcheck)


ary = input()
ans = []
b = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

if "_" in ary:
    if len(ans) == 0:
        ans.append(its_c())
else:
    if ary.lower() == ary:
        print(ary)
    else:
        for i in b:
            if i in ary:
                if len(ans) == 0:
                    ans.append(its_j(ary))

if len(ans) > 0:
    print(''.join(ans))
