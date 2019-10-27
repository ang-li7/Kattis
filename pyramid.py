n = int(input().strip("\n"))
for i in range(1, n+1):
    proper = True
    x = int(input().strip("\n"))
    a = [0, 0, 0]
    for j in range(0, x):
        b = [int(s) for s in input().split(" ")]
        #print(b)
        for k in range(0, 3):
            #print(k)
            #print(str(a[k]) + " " + str(b[k]))
            if a[k] > b[k]:
                #print("bob")
                proper = False
                break
        a = b
    #print("proper" + str(proper))
    if proper:
        print("Pyramid #"+str(i)+": Proper Pyramid")
    else:
        print("Pyramid #"+str(i)+": Improper Pyramid")