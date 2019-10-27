def indexit(a):
    odds = []
    for i in range(0, len(a)):
        if a[i] % 2 == 1:
            odds.append(i)
    return odds
def yes(a, k, o):
    odds = len(o)
    if odds < k:
        print("NO")
        return False
    if (odds - k)%2 == 1:
        print("NO")
        return False
    else:
        print("YES")
        return True

def doit(a, k, o):
    s = ""
    for i in range(0, k-1):
        s = s + str(o[i]+1) + " "
    s = s + str(len(a))
    print(s)

q = int(input())
for i in range(0, q):
    n, k = [int(x) for x in input().split(" ")]
    a = [int(x) for x in input().split(" ")]
    o = indexit(a)
    if yes(a, k, o):
        doit(a, k, o)