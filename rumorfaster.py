def dfs(curr):
  s = []
  s.append(curr)
  mini = bribes[curr]
  while len(s)>0:
    n = s.pop()
    if visited[n]:
      continue
    visited[n] = True
    mini = min(mini, bribes[n])
    for ne in aj[n]:
      s.append(ne)
  return mini
mn = [int(s) for s in input().split(" ")]
n = mn[0]
m = mn[1]
bribes = [int(x) for x in input().split(" ")]
aj = [[] for i in range(n)]
for i in range(m):
    xy = input().split(" ")
    x = int(xy[0])
    y = int(xy[1])
    aj[x-1].append(y-1)
    aj[y-1].append(x-1)
total = 0
visited = [False]*n
for i in range(n):
  if not visited[i]:
    total += dfs(i)
print(total)