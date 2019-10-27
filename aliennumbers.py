z = ''
def int2base(xx, base):
    print(xx)
    print(base)
    while xx>0:
        z = str(xx%base) + z
        xx = xx/base
    print(z)

n = int(input())
print(int2base(9, 3))
for i in range(1, n+1):
    a = input().split(" ")
    x = ""
    for n in a[0]:
        x = x+str(a[1].find(n))
    x = int(str(x), len(a[1]))
    #xx = int('9', 2)
    #print(xx)
    print(x)
    print(len(a[2]))
    #yy = int('9', 3)
    int2base(x, len(a[2]))
    print(z)
    print(y)
    ans = 0
    print("Case "+str(i)+": "+str(ans))