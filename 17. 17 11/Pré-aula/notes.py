from extra import *


def main():
    v = [99, 58, 17, -1, 7, 11, 56, 5, 7, 59, -1, 22]
    m = separe(v, 0, 12)
    # print(v, m)

    v = [99, 58, 17, -1, 7, 11, 56, 5, 7, 59, -1, 22]
    m = partition(v, 0, 11)
    # print(v, m)

    # ----------------

    v = [7, 11, 56, 5, 7, 99, 10]
    m = separe(v, 0, 7)
    # print(m)

    v = [7, 11, 56, 5, 7, 99, 10]
    m = partition(v, 0, 6)
    # print(m)

    # ----------------

    v = [99, 58, 17, -1, 7, 11, 56, 5, 7, 59, -1, 22]
    quicksort(v)
    # print(v)


def separe_lst(v):
    n = len(v)
    x = v[-1]
    i = -1
    for j in range(n):
        if v[j] <= x:
            i += 1
            v[i], v[j] = v[j], v[i]
    return i


def separe(v, e, d):
    sl = v[e:d]

    n = len(sl)
    x = sl[-1]
    i = -1
    for j in range(n):
        if sl[j] <= x:
            i += 1
            sl[i], sl[j] = sl[j], sl[i]

    v[e:d] = sl
    return i


def quicksort(v):
    """(list) -> None
    RECEBE uma lista v.
    REARRANJA os elementos de v para que fiquem em ordem crescente.
    """
    v_t = v[:]

    n = len(v)
    quick_sort(v, 0, n - 1)
    print(v, '\n')

    quicksortR(v_t, 0, n)
    print(v)


def quicksortR(v, e, d):
    """(list, int, int) -> None
    RECEBE uma lista v e índice "e" e "d".
    REARRANJA os elementos de v[e:d] para que fiquem em ordem crescente.
    """
    if e < d - 1:
        m = separe(v, e, d)
        # print(m, v[e:d], e, d)
        quicksortR(v, e, m - 1)
        quicksortR(v, m + 1, d - 1)


main()
