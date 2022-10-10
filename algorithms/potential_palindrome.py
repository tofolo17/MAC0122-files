def main():
    s = "vovova"
    r = pp(s)

    print(r)


def pp(s):
    occ = {}
    for char in s:
        if char not in occ:
            occ[char] = 1
        else:
            occ[char] += 1

    odd = 0
    for v in occ.values():
        if v % 2 == 1:
            odd += 1

    return odd <= 1


main()
