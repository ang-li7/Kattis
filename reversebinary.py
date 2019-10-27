x = int(input())
xx = (bin(x))[2:]
xx = xx[::-1]
b = int(xx, 2)
print(b)
