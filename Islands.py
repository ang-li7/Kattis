def findIslands(p, q, a):
    count = 0
    for i in range(0, p):
        for j in range(0, q):
            if a[i][j] == '1':
                count = count+1
                floodfill(a, i, j)
    return count
def floodfill(a, x, y):
    if a[x][y] == '1':
        a[x][y] = '3'
        print(a)
        if x > 0:
            floodfill(a, int(x - 1), y)
        if x < len(a[y]) - 1:
            floodfill(a, int(x + 1), y)
        if y > 0:
            floodfill(a, x, y - 1)
        if y < len(a) - 1:
            floodfill(a, x, y + 1)
        if x > 0 and y > 0:
            floodfill(a, x-1, y-1)
        if x > 0 and y < len(a) - 1:
            floodfill(a, x-1, y + 1)
        if x < len(a[y]) - 1 and y > 0:
            floodfill(a, x+1, y - 1)
        if x < len(a[y]) - 1 and y < len(a) - 1:
            floodfill(a, x+1, y + 1)


def makeIslands(p, q, x):
    a = []
    count = 0
    for i in range(0, p):
        aa = []
        for j in range(0, q):
            aa.append(x[count])
            count = count+1
        a.append(aa)
    return a

f = int(input())
for i in range(0, f):
    p, pp, q = input()
    #print(p)
    #print(pp)
    #print(q)
    x = input().split(" ")
    #print(x)
    a = makeIslands(int(p), int(q), x)
    print(a)
    t = findIslands(int(p), int(q), a)
    print(t)