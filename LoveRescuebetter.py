alphabet = "abcdefghijklmnopqrstuvwxyz"
x = []
for i in range(0, 26):
    aa = {i}
    x.append(aa)
n = int(input().strip("\n"))
a = list(input().strip("\n"))
b = list(input().strip("\n"))
#print(x)
#print(n)
#print(a)
#print(b)
count = 0
output = []
for i in range(0, n):
    indexa = alphabet.index(a[i])
    indexb = alphabet.index(b[i])
    #print(x)
    #print(indexa)
    #print(indexb)
    if indexb not in x[indexa]:
        output.append(a[i] + " " + b[i])
        count = count+1
        x[indexa] = x[indexa].union(x[indexb])
        x[indexb] = x[indexa].union(x[indexb])
        for j in x[indexa]:
            x[j] = x[indexa].union(x[indexb])
        for j in x[indexb]:
            x[j] = x[indexa].union(x[indexb])
    #print(x)
print(count)
for xx in output:
    print(xx)