import random #importing module
import time
def getRandomDate(startDate,endDate): #defining function
    print("Printing random date between",startDate,"and",endDate)
    randomGenerator=random.random()
    dateFormat='%m/%d/%y'
    startTime=time.mktime(time.strptime(endDate,dateFormat))
    randomTime=startTime+randomGenerator * (endDate-startTime)
    randomDate=time.strftime(dateFormat,time.localTime(randomTime))
    return randomDate
#display result
print("Random Date=",getRandomDate("1/1/2016","12/12/2018"))