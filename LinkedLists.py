__author__ = 'tiffanislutsky'


class MyNode(object):
    def __init__(self, value):
        self._value = value
        self._next = None

    def getValue(self):
        return self._value

    def setValue(self, v):
        self._value = v

    def setNext(self, n):
        self._next = n

    def getNext(self):
        return self._next

    def __str__(self):
        #works
        return str(self.getValue()) + " | " + str(self.getNext())


class MyLinkedList(object):
    def __init__(self, node):
        self._head = node

    def add(self, n):
        node = MyNode(n)
        node.setNext(self._head)
        self._head = node

    def addPos(self,n, p):
        if p is 0:
            self.add(n)
        else:
            node=MyNode(n)
            place = self._head
            for i in range(0,p-1):
                place = place.getNext()
            temp=place.getNext()
            place.setNext(node)
            node.setNext(temp)

    def remove(self, p):
        place = self._head
        if p is (self.size()-1):
            for i in range(0, p-1):
                place = place.getNext()
            place.setNext(None)
            return
        elif p is 0:
            place = place.getNext()
            self._head = place
        else:
            for i in range(0, p-1):
                place = place.getNext()
            b=place.getNext()
            place.setNext(b.getNext())
            return b.getValue()

    def get(self, p):
        #works
        place = self._head
        for i in range(0, p):
            place = place.getNext()
        return place.getValue()

    def set(self, p, val):
        place = self._head
        for i in range(0, p):
            place = place.getNext()
        place=place.setValue(val)

    def __str__(self):
        place = self._head
        if self._head == None:
            return "empty"
        s = str(self._head.getValue())
        while place.getNext() != None:
            place = place.getNext()
            s = s + " " + str(place.getValue())
        return s

    def size(self):
        #works
        i = 1
        place = self._head
        while place.getNext() != None:
            place = place.getNext()
            i=i+1
        return i
n1 = MyNode(1)
nums = MyLinkedList(n1)
print(nums)
for i in range(2, 11):
    nums.add(i)
nums.addPos(2, 3)
print(nums)
print(str(nums.size()))
print(str(nums.get(nums.size()-1)))
nums.set(3, 8)
print(nums)
nums.remove(nums.size()-1)
print(nums)



