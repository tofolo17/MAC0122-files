from classes.array2d import Array2D

a = Array2D((2, 3), 0)
b = a.reshape((3, 2))  # b é vista de a

a[0, 0] = 1
print(a.data, b.data)

nd = [1] * 6
a.carregue(nd)

print(a.data)
print(b.data)

print(b.data is nd, b.data == nd)

# nd = 2
# print(a.data)

nd[0] = 2
print(a.data)

# d
