###exception handing
try:
    1/0
except:
    print("Divide by zero error")
#--------------------------------------#
try:
    1/0
except ZeroDivisionError as e:
    print(e)
#------------------------------------#
try:
    print(b)
except NameError as e:
    print(e)
#---------------------------------------#
lst=[1,2,3,4,5]
try:
    print(lst[4])
except KeyError as e:
    print(e)
except IndexError as e:
    print(e)
except:
    print("Unkmown Error")
finally:
    print("This block will run in any case")
#---------------------------------------------#
#######decorator
import time

def calctime(f):
    def wrap(*arg, ** kwargs):
        start=time.time()
        result=f(*arg, ** kwargs)
        end= time.time()
        print(f.__name__+" took "+str((end-start)*1000))
        return result
    return wrap
@calctime
def calcsum(a,b):
    result = a+b
    print(result)

@calctime
def calcsub(a,b):
    result = a-b
    print(result)

calcsum(10,20)
calcsub(10,20)
#---------------------------------------------------#
#####context manager##################
try:
    o=open("c:/pydemo/abc.txt",'w')
    o.write("Welcome to day 2 python")
finally:
    o.close()

with open("c:/pydemo/abc.txt",'w') as f:
    f.write("Hello")
#---------------------------------------#
class filemange:
    def __init__(self,name):
        self.name=name
    def __enter__(self):
        self.file=open(self.name,'w')
        return self.file
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

with filemange("xyz.txt") as f:
    f.write("welcome to contex manager")
#-----------------------------------------#
from contextlib import contextmanager
@contextmanager
def filemanage(name):
    try:
        f=open(name,'w')
        yield f
    finally:
        f.close()

with filemanage("welcome.txt") as f:
    f.write("Welcome to day 2 session")
#--------------------------------------------#
