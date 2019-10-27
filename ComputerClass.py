class Computer(object):
    def __init__(self, p, r):
        self.__processor = p
        self.__ramsize = r

    def getprocessor(self):
        return self.__processor

    def getramsize(self):
        return self.__ramsize

    def setprocessor(self, p):
        self.__processor = p

    def setramsize(self, r):
        self.__ramsize = r

class MobilePhone(Computer):
    def __init__(self, p, r, c, n):
        super().__init__(p, r)
        self.__camera = c
        self.__mobilenetwork = n

    def getcamera(self):
        return self.__camera

    def getmobilenetwork(self):
        return self.__mobilenetwork

    def setcamera(self, c):
        self.__camera = c

    def setmobilenetwork(self, n):
        self.__mobilenetwork = n

class Laptop(Computer):
    def __init__(self, p, r, t, u):
        super().__init__(p, r)
        self.__touchscreen = t
        self.__usb = u

    def gettouchscreen(self):
        return self.__touchscreen

    def getusb(self):
        return self.__usb

    def settouchscreen(self, t):
        self.__touchscreen = t

    def setusb(self, n):
        if n>=0 and n<=6 and int(n) == n:
            self.__usb = n

myphone = MobilePhone("CIE234X", "2GB", True, "camNetwork")
print(myphone.getcamera())
print(myphone.getmobilenetwork())
print(myphone.getprocessor())
print(myphone.getramsize())
myphone.setcamera(False)
print(myphone.getcamera())
myphone.setmobilenetwork("AT&T")
print(myphone.getmobilenetwork())
