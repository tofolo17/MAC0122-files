def main():
    a = [11, 22, 33, 66, 44, 55, 77]
    mergesort(a)

    print(a)


def insertion_sort(array):
    for i in range(1, len(array)):
        key_item = array[i]
        j = i - 1
        while j >= 0:
            print(array[j], key_item)
            if array[j] < key_item:
                break
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key_item

    return array


def merge(v, e, m, d):
    lista = []
    i = e
    j = m
    while i < m and j < d:
        print(v[i], v[j])
        if v[i] < v[j]:
            lista.append(v[i])
            i += 1
        else:
            lista.append(v[j])
            j += 1
    lista += v[i:m]
    lista += v[j:d]
    v[e:d] = lista


def mergesortR(v, e, d):
    if e < d - 1:
        m = (e + d) // 2
        mergesortR(v, e, m)
        mergesortR(v, m, d)
        merge(v, e, m, d)


def mergesort(v):
    n = len(v)
    mergesortR(v, 0, n)


main()
