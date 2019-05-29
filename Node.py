from Employee import Employee
class Node():
    def __init__(self, data:Employee, nextNode):
        self.__data = data
        self.__nextNode = nextNode
    
    def getData(self):
        return self.__data

    def getNext(self):
        return self.__nextNode

    def setData(self, d):
        self.__data = d

    def setNext(self, n):
        self.__nextNode = n

    def __str__(self):
        return str(self.__data)



