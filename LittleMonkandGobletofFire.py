a = []
def eee(schoolroll):
    school, roll = [int(x) for x in schoolroll.split(" ")]
    #print(school)
    added = False
    for i in a:
        if(i[0] == school):
            i.append(roll)
            added = True
    #print(added)
    if not added:
        aa = [school, roll]
        a.append(aa)
    print(a)
def ddd():
    count = 0
    while len(a[count])<2:
        count = count + 1
    print(str(a[count][0]) +" " + str(a[count].pop(1)))
    print(a)
n = int(input())
for i in range (0, n):
    x = input().split(" ")
    if x[0] == 'E':
        schoolroll = str(int(x[1])) + " " + str(int(x[2]))
        eee(schoolroll)
    else:
        ddd()