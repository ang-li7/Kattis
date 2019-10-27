def lol(n):
    return n*n-n+41

def isPrime(n):
    for i in range(2, n):
        if n%i == 0:
            return False
    return True

for i in range(0, 500):
    x = lol(i)
    if(isPrime(x) == False):
        print(str(i)+ ": " + str(x) + " " + str(isPrime(x)))
