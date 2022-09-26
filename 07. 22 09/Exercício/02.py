lstA = [2, 3, 4]
lstB = lstA[:]

lstA[0] = 1
print(lstA, lstB)  # Deixou de ser cópia.

lstB = lstA
lstA[0] = 2
print(lstA, lstB)  # Continua como cópia.

# a, d, g, h, j
