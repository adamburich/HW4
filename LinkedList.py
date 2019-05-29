from Node import *
from Employee import *

class LinkedList():
    def __init__(self, head=None):
        self.__head = self.__tail = head

    def isEmpty(self):
        return self.__head == None

    def addEmployee(self):
        eid = input("Enter employee id: \n")
        hourly = input('Enter hourly rate: \n')
        new = Node(Employee(eid, hourly), None)
        if self.isEmpty():
            self.__head = new
        else:
            current = self.__head
            while current.getNext() != None:
                current = current.getNext()
            current.setNext(new)
            
    def search(self, eid):
        current = self.__head
        found = False
        while current != None and not found:
            if current.getData().getID() == eid:
                found = True
            else:
                current = current.getNext()

    def getWeeklyTotal(self):
        current = self.__head
        while current:
            eid = current.getID()
            current.setHours(input('Enter hours worked for employee %s: ' % eid))
            current = current.getNext()

    def output(self):
        current = self.__head
        while current:
            print(current.getData())
            current = current.getNext()

    def newHourly(self):
        eid = input('Enter ID: \n')
        employee = self.search(eid)
        if employee is not None:
            hourly = input('Enter hourly wage: \n')
            employee.setHourly(hourly)
            
    def remove(self, eid):
        if self.__head == None:
            print("This isn't working!")
        current = self.__head
        previous = None
        found = False
        
        # first find item in the list
        while not found:
            if self.__head.getData().getID() == eid:
                found = True
            else:
                previous = self.__head
                self.__head = self.__head.getNext()

        if previous == None:  # item was in the fist node
            self.__head = current.getNext()
        else:  # item was somewhere after the first node
            previous.setNext(current.getNext())

