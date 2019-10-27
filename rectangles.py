a, b, c, d, h = [int(x) for x in input().split(" ")]
aa = [a, b, c, d]
aa.sort()
#print(aa)
if aa[1] == a and aa[2] == b:
    print(str(h*(b-a)))
elif aa[1] == c and aa[2] == d:
    print(str(h*(d-c)))
elif aa[1] == c and aa[2] == b:
    print(str(h*(b-c)))
elif aa[1] == a and aa[2] == d:
    print(str(h*(d-a)))
else:
    print(0)
