import math
def distance(a, b):
    if(a>b):
        return min(28-(a-b), a-b)
    else:
        return min(28-(b-a), b-a)
dict={}
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ '"
#print(len(alphabet))
count = 0
for a in alphabet:
    dict[a] = count
    count = count+1
tc = int(input())
for i in range(0, tc):
    s = input()
    tot = 0
    for j in range(0, len(s)-1):
        tot = tot+(math.pi*60*distance(dict[s[j]], dict[s[j+1]]))/(28*15)
        tot = tot+1
        #print(tot)
    print(tot+1)