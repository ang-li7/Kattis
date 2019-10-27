import math
xx = input().split(" ")
rc = int(xx[0])
sc = int(xx[1])
r = []
r.append(int(input()))
maxload = 1
curload = 1
nto = 0
for i in range(1, rc):
    r.append(int(input()))
    curload = curload+1
    while r[i]>=r[nto]+1000:
        nto = nto+1
        curload = curload -1
    maxload = max(maxload, curload)
servers = int(math.ceil(float(maxload)/sc))
print(servers)