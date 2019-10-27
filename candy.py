n = int(input())
for i in range(0, n):
    a = [int(x) for x in input().split(" ")]
    sum = 0
    for j in a:
        sum = sum + j
    print(sum//2)