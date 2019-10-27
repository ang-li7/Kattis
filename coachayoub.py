n, a, b, s = [int(x) for x in input().split(" ")]
if n > 1 and (s-b)/(n-1) >= a and n*a<=s and n*b>=s:
    print("YES")
elif n ==1 and a == b and s == b:
    print("YES")
else:
    print("NO")