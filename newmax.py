a=input().split(" ")
b=input().split(" ")
a=[int(c) for c in a]
b=[int(c) for c in b]
c1=0
for c in range(len(b)):
  if b[c]>a[1]:
    c1=c1+1
if c1==0 and a[1] not in b:
  c1=c1+1
if c1>a[2]:
  print("NO")
else:
  print("YES")