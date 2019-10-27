n = input()
zl = len(n)
x = 0
y = 0;
for i in range(zl-1, -1, -1):
    q = n[zl-i-1]
    if q == '1' or q == '3':
        x = x + 2**i
    if q == '2' or q =='3':
        y = y + 2**i
print(zl, x, y)


