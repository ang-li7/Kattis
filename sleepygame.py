def go(curr, depth, aj, visited, a):
    print(str(curr) + " " + str(depth))
    visited[curr] = True
    doesnothavenext = True
    for nexty in aj[curr]:
        if visited[nexty] == False:
            doesnothavenext = False
            go(nexty, depth + 1, aj, visited, a)
    if doesnothavenext and depth%2 == 1:
        print(depth)
        a.append(depth)

n, m = [int(x) for x in input().strip("\n").split(" ")]
#print(n)
#print(m)
draw = True
aj = [[] for i in range(n)]
visited = [False]*n
for i in range(1, n+1):
    bob = [int(x) for x in input().strip("\n").split(" ")]
    if bob[0] == 0:
        draw = False
    for j in range (1, bob[0]+1):
        aj[i-1].append(bob[j]-1)
print(aj)
start = int(input().strip("\n"))-1
a = []
#print(start)
if draw:
    print("Draw")
else:
    go(start, 0, aj, visited, a)
    print(a)
    win = False
    for i in a:
        if i%2 == 0:
            print("Lose")
        else:
            print("Win")