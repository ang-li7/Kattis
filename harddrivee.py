
n, c, b = [int(x) for x in input().split(" ")]
bb = [int(x)-1 for x in input().split(" ")]
a = []
for i in range(n):
    a.append('0')
start = 1
if c % 2 == 1:
    c -= 1
    a[0] = '1'
    start = 2

p = 0

while c > 0 and start < n:
    while p < b and bb[p] < start:
        p += 1
    if p < b and bb[p] == start:
        p += 1
        start += 1
        continue
    c -= 2
    a[start] = '1'
    start += 2

#print(a)
s = ""
for i in a:
    s = s + i
print(s)