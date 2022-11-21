m = 0
v = [i for i in range(40)]

for i in range(len(v)):
    print(v[i], end=" ")
    if i % (2 ** m) == 0 and i != 4:
        print(f'\n{i, 2 ** m}')
        m += 1
