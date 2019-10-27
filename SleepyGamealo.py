n, m = [int(x) for x in input().strip("\n").split(" ")]
ed = []
dr = []
for i in range(n):
    bob = [int(x) for x in input().strip("\n").split(" ")]
    if bob[0] == 0:
        dr.append(i+1)
    ed.append(set(bob[1:]))
start = int(input().strip("\n"))-1
print(ed)
print(dr)
stack = {start}
visied = {}
while len(stack)>0:
    curr = stack.pop()
