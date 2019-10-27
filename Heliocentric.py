z = 1
while(z<11):
    s = input()
    if(s == ''):
        break
    data = s.split(" ")
    e = int(data[0])
    m = int(data[1])
    tot = 0
    while e!=0 or m!=0:
        e = (e+1)%365
        m = (m+1)%687
        tot=tot+1
    print("Case "+str(z)+": "+str(tot))
    z = z+1
