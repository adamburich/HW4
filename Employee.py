class Employee:
    def __init__(self, eid, hourly=0):
        self.__eid = eid
        self.__hours = 0
        self.__hourly = hourly
        self.__total = 0

    def __str__(self):
        out1 = "Employee ID: " + str(self.__eid)
        out2 = "Hours: " + str(self.__hours)
        out3 = "Total: " + str(self.__total)
        return out1 + '\n' + out2 + '\n' + out3

    def setHourly(self, hourly):
        self.__hourly = hourly
        self.__total = self.__hours*self.__hourly

    def setHours(self, h):
        self.__hours = h
        self.__total = h * self.__hourly

    def getTotal(self):
        return self.__total

    def getHourly(self):
        return self.__hourly

    def getHours(self):
        return self.__hours

    def getID(self):
        return self.__eid

    



