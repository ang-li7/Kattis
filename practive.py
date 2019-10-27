
a = int(input("Give me an integer"))
b = int(input("Give me another integer"))
for a in range(a,b+1):
    if a % 7 == 0 and a % 3 != 0:
        print(a)

x = int(input("Enter a number to find its factorial. Enter a negtive number to stop the program"))
while(x>=0):
    m=1
    z=1
    for z in range(z, x+1):
        m = m*z
    print("x! is "+str(m))
    x = int(input())


name = input("Enter your name:")
for i in range(0,len(name), 2):
    print(name[i:i+2])
print(name[-1]+name[1:-1]+name[0])


