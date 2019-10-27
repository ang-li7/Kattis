x=int(input())
for i in range(0,x):
  cc=0
  input()
  a=input().split(" ")
  b=input().split(" ")
  for g in a:
    if(g in b):
      cc=cc+1
  print("Birthday #"+str(i+1)+": "+str(cc))
