def mini(p, visited):
    index = 0
    lowestprice = 1000000000
    for i in range(len(price)):
        #print(i)
        if p[i] < lowestprice and visited[i] == False:
            lowestprice = p[i]
            index = i
    return index

def allvisited(visited):
    mybool = True
    for i in visited:
        if i == False:
            mybool = False
    return mybool

def dfs(c, aj, visited, p, total):
    visited[c] = True
    #print(total)
    if allvisited(visited) == True:
        #print("all visited")
        print(total)
        return str(total) + " "
    mybool = True
    for i in aj[c]:
        if visited[i] == False:
            mybool = False
            dfs(i, aj, visited, p, total)
    if mybool:
        return dfs(mini(p, visited), aj, visited, p, total+p[mini(p, visited)])

mn = input().split(" ")
m = int(mn[0])
n = int(mn[1])
visited = []
price = input().split(" ")
p = []
aj = []
for i in range (m):
    aj.append([])
    p.append(int(price[i]))
    visited.append(False)

##print(visited)
##print(price)
##print(p)
##print(aj)
for i in range(n):
    xy = input().split(" ")
    x = int(xy[0])
    y = int(xy[1])
    aj[x-1].append(y-1)
    aj[y-1].append(x-1)
#print(aj)
#print(mini(p, visited))
index = mini(p, visited)
#print(index)
#print(p[index])
#print(allvisited(visited))
#dfs(index, aj, visited, p, p[index])
dfs(index, aj, visited, p, p[index])