n = int(input())
for i in range(n):
    nn = int(input())
    d = {}
    for j in range(nn):
        x, y = input().split(" ")
        if y in d:
            d[y] = d.get(y) + 1;
        else:
            d[y] = 1;
    #print(d)
    tot = 1
    for e in d:
        tot *= d[e] + 1
    print(tot - 1)