print("Welcome")
a = 50
b = 30.3
print("a: "+str(a))
print("b: "+str(b))

if(a>100):
    print("Not Found")
elif(a<100):
    print("Found")
else:
    print("Not exceute")

count=0
while(count<9):
    print("Count is: ",str(count))
    count=count+1
else:
    print("Count is less than the defined value")

mlist=[12,20,40,"Sam"]
for t in mlist:
    print("mlist: ",str(t))

print("12 in mlist: ",12 in mlist)

data1 = [1,2,3]
data2 = [1,2,3]
print("data1 in data2: ",data1 in data2)
data3=data1
print("data1 is data2: ",data1 is data2)
print("data1 is data3: ",data1 is data3)
print("id of data1: ",id(data1))
print("id of data2: ",id(data2))
print("id of data3: ",id(data3))
a="I want ice cream"
b='I want ice cream'
c="""welcome to python
welcome to mdc"""
print(a)
print(b)
print(c)
print(dir(str))

print("***********list example")
mlist=[1,2,3.3,5,"Smaple"]
print("mlist: ",mlist)
#print("length of mlist: ",mlist.len())
print(mlist[0])
print(mlist[-1])
print(mlist.index(3.3))
mlist.append("sam")
print("mlist: ",mlist)
mlist.insert(2,3.2)
print("mlist: ",mlist)
mlist.remove(3.2)
print("mlist: ",mlist)
mlist.reverse()
print("mlist: ",mlist)
nlist = mlist.copy()
print("nlist: ",nlist)
extendList = mlist.extend(nlist)
print("extendList: ",extendList)
print("extendList: ",mlist)
#mlist.sort()
#print("sorted list: ",mlist)
#mlist.pop()
#print("popped list: ",mlist)
x=[1,2,[2,3,4],"sam"]
print(type(x))
for i in x:
    print(type(i))

mtup=(1,2,3,4,"sam",3.4)
print(type(mtup))


import sys
mlist=[1,2,3,True,"true","abcd",3.4]
mtup=(1,2,3,True,"true","abcd",3.4)
print(sys.getsizeof(mlist))
print(sys.getsizeof(mtup))
print("**********example of set*********")
odds=set([1,3,5,7,9])
even=set([2,4,6,8])
prino=set([2,3,5,7])
print(odds | even)
print(odds.union(prino))
print(odds.intersection(prino))
print(odds & prino)
print(odds - prino)
print(prino - odds)

print("*****exmple of disctionary****")
addr={'emno':11274784,'name':'saurav','loc':'Mumbai'}
print(addr)
addr1=dict(emno=112946758,name='saurav',loc='Mumbai')
print(addr1)
for key in addr.keys():
    value=addr[key]
    print(key,"=",value)
for key,val in addr.items():
    print(key,"=",value)    
x=["car","bus","truck"]
print(x)
a,b,c=x
print(a)
print(b)
print(c)
sam="welcome to accenture"
d=sam.split(" ")
print(d)
d.sort()
print(d)
d.sort(reverse=True)
print(d)
print("********exmaple of time******")
import time
print(time.time())
print(time.localtime(time.time()))
print(time.asctime())
time.sleep(2)
print("****exaple of datetime******")
import datetime
mdate=datetime.date(2017,7,6)
print(mdate)
print(type(mdate))
tday=datetime.date.today()
print(tday)
print(tday.year)
print(tday.day)
print("*******Calendar********")
import calendar
print(calendar.month(1947,8))
print(calendar.calendar(2017))
print(calendar.isleap(2017))
print("pow(2*3): ",pow(2,3))
print("**********user define function********")
def disp(name):
    return name
print(disp("saurav"))
print(disp([1,2,3]))
def ldisp(x):
    for x,y in enumerate(x):
        print(x,"-",y)
ldisp([2,3,4,5])

def student(name, *score):
    print(name)
    print(score)
student("saurav",20,4,60)
print("**********lambda function********")

def expo(x):
    return x**2

print(expo(5))

mlam = lambda x:x**2
print(mlam(5))

def add(x,y):
    return x+y
print(add(10,20))
add = lambda x,y:x+y
print(add(10,20))

maxi = lambda x,y: x if x>y else y
print(maxi(4,9))
print("********map example*******")
n=[2,4,6]
print(list(map(lambda x:x**2,n)))
print("********filetr example*********")
mlist=[1,2,3,4,5,6,7,88,44,55,33]
evenlist=list(filter(lambda x:(x%2==0),mlist))
print(evenlist)
print("********reduce function example************")
from functools import reduce
print(reduce(lambda x,y:x*y,n))

print("*******file examle*******")
fob=open("c:/pydemo/sample.txt",'r')
print(fob.mode)
print(fob.read())
print(fob.seek(0,0))
print(fob.tell())
print(fob.seek(0,2))
print(fob.seek(2,0))
print(fob.read())
print(fob.readline())
print(fob.seek(0,0))
print(fob.readlines())
fob.close()
ob=open("c:/pydemo/demo.txt",'w')
s="welcome to python mdc, welcome to accenture"
lst=s.split(",")
print(lst)
ob.writelines(lst)
ob.close()
###### manipulating with excel
###open cmd run the command -- pip install xlrd
import xlrd
loc="c:/pydemo/demo.xlsx"
xlfo=xlrd.open_workbook(loc)
sheet=xlfo.sheet_by_index(0)
print(sheet.cell_value(1,1))
print(sheet.nrows)
print(sheet.ncols)
for cols in range(sheet.ncols):
    print(sheet.cell_value(0,cols))
    
for rows in range(sheet.nrows):
    print(sheet.cell_value(rows,0))
print(sheet.name)
####csv file
import csv
with open("c:/pydemo/democsv.csv",'r') as f:
    r=csv.reader(f,delimiter=",")
    for row in r:
        print(row)
############class example##########################
class Sample:
    def setdata(self, empid, empname):
        self.empid=empid
        self.empname=empname
    def getdata(self):
        print(self.empid)
        print(self.empname)

obj=Sample()
obj.setdata(101,"Saurav")
obj.getdata()
print(dir(Sample))
print(Sample.__name__)
print(dir(obj))
