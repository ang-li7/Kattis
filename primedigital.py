x = int(input())
ew=[0,1,4,6,8,9]
for i in range(0,x):
  cc=0
  a=input().split(" ")
  for j in range(int(a[0]),int(a[1])+1):
    j=str(j)
    boo=True
    for k in j:
      if(int(k) in ew):
        boo=False
    if(boo):cc=cc+1
  print("Range #"+str(i+1)+": "+str(cc))