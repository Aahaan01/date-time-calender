import random
import time

startdate=input("Please enter the starting date in yyyy/mm/dd")
enddate=input("Please enter the ending date in yyyy/mm/dd")

randomdate=random.random()
#print(randomdate)
format="%m%d%y"
starttime=time.mktime(time.strptime(startdate,format))
endtime=time.mktime(time.strptime(enddate,format))
randomtime=starttime+randomdate*(endtime-starttime)
x=time.strptime(format,time.localtime(randomtime))
print(x)