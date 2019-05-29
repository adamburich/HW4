from LinkedList import *
from Employee import *
from Node import *

def main():
    emptyList = LinkedList()
    emptyList.addEmployee()
    emptyList.addEmployee()
    emptyList.addEmployee()
    emptyList.delete(1001)
    emptyList.output()
main()