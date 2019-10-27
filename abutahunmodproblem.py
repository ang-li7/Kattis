def isPal(arr,mod):
  a=[]
  for c in range(len(arr)):
    a.append(arr[c]%mod)
  return a==a[::-1]


a=int(input())
b=[int(c) for c in input().split(" ")]
c1=1
for c in range(max(b),2,-1):
  if isPal(b,c):
    c1=c
    break
if b==b[::-1]:
  print("-1")
else:
  print(c1)