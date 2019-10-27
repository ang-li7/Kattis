def nathan(a):
    for i in a:
        for j in a:
            if i == j:
                continue
            else:
                if abs(i-j)%m != 0:
                    return True
    return False

n, m = [int(x) for x in input().split(" ")]
a = [int(x) for x in input().split(" ")]
aa = []
for i in a:
    aa.append(i)
#print(aa)
b = [int(x) for x in input().split(" ")]
count = 0
index = 0
while len(aa) > 1 and nathan(aa):
    temp = a[b[index]-1]
    aa.remove(temp)
    count = count+1
    index = index + 1
print(count)



