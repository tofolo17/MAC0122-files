def main():
    v = [7, 11, 56, 5, 7, 99, 104]
    mergesort(v)
    print(v)


def merge(v, e, m, d):
    v1 = v[e:m]
    v2 = v[m:d]
    v_aux = []
    m, n = len(v1), len(v2)
    i = j = 0
    while i < m and j < n:
        if v1[i] < v2[j]:
            v_aux.append(v1[i])
            i += 1
        else:
            v_aux.append(v2[j])
            j += 1
    v_aux += v1[i:m]
    v_aux += v2[j:n]

    v[e:d] = v_aux


def mergesort(v):
    n = len(v)
    mergesortR(v, 0, n)


def mergesortR(v, e, d):
    if d == e or e == d - 1:
        return None
    m = (e + d) // 2
    mergesortR(v, e, m)
    mergesortR(v, m, d)
    merge(v, e, m, d)


# TODO: analisar esta função.
def mergesortI(v):
    n = len(v)
    b = 1
    while b < n:
        e = 0
        while e + b < n:
            d = e + 2 * b
            if d > n:
                d = n
            merge(v, e, e + b, d)
            e = d
        b = 2 * b


main()
