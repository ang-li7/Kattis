class TreeNode(object):
    def __init__(self, value, left, right):
        self._value = value
        self._left = left
        self._right = right

    def getLeftChild(self):
        return self._left

    def getRightChild(self):
        return self._right

    def getValue(self):
        return self._value

    def setLeftChild(self, left):
        self._left = left

    def setRightChild(self, right):
        self._right = right

    def __str__(self):
        return str(self._left + " " + self._value + " " + self._right)