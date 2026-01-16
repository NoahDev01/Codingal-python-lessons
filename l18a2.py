import random
import time
def getRandomdate(startdate,enddate):
    print("randomdate between",startdate," and ",enddate)
    randomGenerator=random.random()
    dateformat='%m/%d/%Y'
    starttime=time.mktime(time.strptime(startdate,dateformat))
    endtime=time.mktime(time.strptime(enddate,dateformat))
    randomtime=starttime+randomGenerator*(endtime-starttime)
    randomdate=time.strftime(dateformat,time.localtime(randomtime))
    return randomdate
print("randomdate=",getRandomdate("1/1/2023","12/8/2024"))


    