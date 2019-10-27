for c in range(1, 11):
    for p in range(1, 34):
        s = (100 - (c*10) - (p*3))*2
        if c + p + s == 100:
            print(str(c) + " " + str(p) + " " + str(s))