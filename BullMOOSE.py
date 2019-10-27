aa = input()
a = aa.split(" ")
x = int(a[0])
y = int(a[1])
if (x==0 and y == 0):
    print("Not a moose")
elif x==y:
    print("Even "+str(2*x))
else:
    if x>y:
        print("Odd "+str(2*x))
    else:
        print("Odd "+str(2*y))