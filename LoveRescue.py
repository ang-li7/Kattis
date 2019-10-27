def change(a, b):
    for i in range(len(a)-1, -1, -1):
       # print(a[i] + " " + b[i])
       # print(i)
        if a[i] == a[0]:
            a[i] = b[0]
            continue
        if b[i] == a[0]:
            b[i] = b[0]
            continue
n = int(input().strip("\n"))
a = list(input().strip("\n"))
b = list(input().strip("\n"))
output = []
#print(a)
#print(b)
#change(a, b)
#print(a)
#print(b)
count = 0
while len(a) > 0 and len(b)>0 and len(a)==len(b):
    #print(len(a))
    #print(len(b))
    while len(a)>0 and a[0] == b[0]:
        #print("bob")
        del a[0]
        del b[0]
    else:
        if len(a) == 0:
            break
        output.append(str(a[0] + " " + b[0]))
        count = count+1
        change(a, b)
        print(a)
        print(b)
        #print(a[0] + " " + b[0])
print(count)
for x in output:
    print(x)