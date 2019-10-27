tot = 0
cost = float(input())
num = int(input())
for i in range(0, num):
    d = input().split(" ")
    tot = tot + float(d[0]) * float(d[1])*cost
print("%f"%tot)
