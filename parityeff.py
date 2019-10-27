from collections import OrderedDict
import math

for i in range(0, 10):
    a = input()
    aa = a.split(", ")
    hexnum = aa[0]
    eo = aa[-1]
    hexdec = OrderedDict()
    hexdec["A"] = "1010"
    hexdec["B"] = "1011"
    hexdec["C"] = "1100"
    hexdec["D"] = "1101"
    hexdec["E"] = "1110"
    hexdec["F"] = "1111"
    hexdec['1'] = "0001"
    hexdec['2'] = "0010"
    hexdec['3'] = "0011"
    hexdec['4'] = "0100"
    hexdec['5'] = "0101"
    hexdec['6'] = "0110"
    hexdec['7'] = "0111"
    hexdec['8'] = "1000"
    hexdec['9'] = "1001"
    hexdec['0'] = "0000"
    j = ""
    for c in hexnum:
        num = hexdec[c]
        j = j + num
    print(str(j))
    #print(len(j))
   # print(str(math.log(int(j, 2), 2.0)-1))
    length = len(j)+math.ceil(math.log(len(j), 2.0))+1
    print(length)

    a = ["A"]*int(length)
    count = 0
    for k in range(0, length):
        if(math.pow(2, k)<length):
            a[int(math.pow(2, k))-1] = "P"
        if a[k] is "A"and count<len(j):
            a[k] = j[count]
            count = count+1
            #print(count)
    print(str(a))
    while a[-1] is 'A':
        a = a[:-1]
        print(str(a))
        length = length -1
    for k in range(0, math.ceil(math.log(length, 2))):
        kk = int(math.pow(2, k))
        total = 0
        for v in range(kk-1, length, 2*kk):
            seg = a[v:v+kk]
            if len(seg)>0:
                #print(seg)
                #print(len(seg))
                for h in seg:
                    #print(h)
                    if h == "1":
                        total = total+1
        if(total%2 == 1 and eo == "ODD"):
            print(0, end = "")
        elif(total%2 == 0 and eo == "EVEN"):
            print(0, end = "")
        else:
            print(1,end = "")

        #print(total)
