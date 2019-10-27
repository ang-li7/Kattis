x = input()
comp = x[len(x)-1]
n = int(input())
match = []
first = ""
last = ""

for i in range(n):
    x = input()
    if(x[0] == comp):
        match.append(x)
    first = first + x[0]
    last = last + x[len(x)-1]
print(match)
print(first)
print(last)
if(len(match) == 0)
    print("?")
else:
