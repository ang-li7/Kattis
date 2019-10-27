import statistics

x=input().split(",")
lgn=int(x[0])
x=x[1:]
x=[int(i) for i in x]
y=x
sum=0
while(y!=[]):
  x=y
  cc=len(x)
  while(x==y and cc>0):
    cc=cc-1
    if(x[cc]==0):
      y=y[cc+1:]
      sum=sum+1
  if(y!=[]):
    med=int(statistics.median(y))
    lgn=len(y)
    cc=lgn
    boo=True
    while(cc>0 and boo):
      cc=cc-1
      if(med==y[cc]):
        boo=False
      if(cc==0 and boo):
        med=med-1
        cc=lgn
    if(y[cc]%2==1):
      y[cc]=med-1
    else:
      y[cc]=med-2
    sum=sum+1
print(sum)
