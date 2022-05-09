L = [23, 45, 32, 25, 46, 33, 71, 90]
a = 0
i = 1
b = len(L)
print(b)
for i in L:
    if L.index(i)%2 != 0:
        print(i, "is odd number")
    else:
        pass
