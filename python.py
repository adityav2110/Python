print("Hello Aditya, how are you?")

#basic datatypes in python like int, float, string, boolean, sequence, dictionary, tuple, set, etc.
myint = 7
float = 7.0
string = "Hello"
boolean = True
list = [1,2,3,4,5]
tuple = (1,2,3,4,5)
dictionary = {"one":1,"two":2,"three":3,"four":4,"five":5}
set = {1,2,3,4,5}
print(myint)
print(float)
print(string)
print(boolean)
print(list)
print(tuple)
print(dictionary)
print(set)

#we can redefine the variables with different datatypes as well in python like below:
myint = "Hello"
float = 7
string = 7.0
boolean = [1,2,3,4,5]
list = True
tuple = {1,2,3,4,5}
dictionary = (1,2,3,4,5)
set = {"one":1,"two":2,"three":3,"four":4,"five":5}
print(myint)
print(float)
print(string)
print(boolean)
print(list)
print(tuple)
print(dictionary)
print(set)

#slicing in python
mystring = "Hello Aditya"
print(mystring[0]) #prints entity at 0th index #H
print(mystring[-1]) #prints entity at -1th index #a
print(mystring[0:5]) #prints entity from 0th index to 4th index #Hello
print(mystring[6:]) #prints entity from 6th index to end #Aditya
print(mystring[:5]) #prints entity from start to 4th index #Hello
print(mystring[:-1]) #prints entity from start to -2th index #Hello Adity
print(mystring[-5:]) #prints entity from -5th index to end #ditya
print(mystring[::2]) #prints entity from start to end with step size 2 #HloAiy
print(mystring[::-1]) #prints entity from start to end with step size -1 #aytidA olleH
print(mystring[::-2]) #prints entity from start to end with step size -2 #atd le
print(mystring[0:9:2]) #prints entity from 0th index to 4th index with step size 2 #HloAi
print(mystring[0:4:-2]) #prints entity from 0th index to 4th index with step size -2 #empty string How? because it is going from 0th index to 4th index with step size -2, so it is not able to find any entity in between 0th and 4th index
print(mystring[4:0:-2]) #prints entity from 4th index to 0th index with step size -2 #ol

#accessing the elements of dictionary using keys
mydictionary = {"one":1,"two":2,"three":3,"four":4,"five":5} #dictionary is a key value pair data structure in python where key is unique and value can be duplicate but key cannot be duplicate in dictionary.
print(mydictionary["one"]) #prints value of key "one" #1 #if key is not present then it will throw error
del mydictionary["one"] #deletes the key value pair from dictionary
print(mydictionary) #prints dictionary #{"two":2,"three":3,"four":4,"five":5}

#Functions in python: Functions are the block of code which can be called multiple times in a program. Functions are used to avoid the code redundancy in a program. And makes code more modular.

def myfunction():
    print("Hello Aditya")
    
myfunction() #calling the function #Hello Aditya
print(myfunction()) #prints the function #Hello Aditya #None
print(myfunction)#prints none
print(type(myfunction())) #prints the type of function #Hello Aditya #None #<class 'NoneType'>

#Functions with arguments
def myfunction2(a , b):
    print(a+b)
myfunction2(2,3) #calling the function #5
print(myfunction2(2,3)) #prints the function #5 #None #Why none? because function is not returning anything.

#Functions with return statement
def myfunction3(a):
    return a*a*a
myfunction3(3) #calling the function #27
print(myfunction3(3)) #prints the function #27 #None is not here because function is returning something.

#Functions with default arguments
def power(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result
print(power(2)) #calling the function #2
print(power(2,3)) #calling the function #8
print(power(x=3, num=2)) #calling the function #8

#Functions with variable length arguments
def summation(*args):
    result = 0
    for i in args:
        result = result + i
    return result
print(summation(1,2,3,4,5)) #calling the function #15
print(summation(1,2,3,4,5,6,7,8,9,10)) #calling the function #55
print(type(summation(1,2,3,4,5))) #calling the function #15 #<class 'int'>

#Conditoinal statements in python
#keywords: if, elif, else #Comparision operators: ==, !=, >, <, >=, <=
x=10
y=20
if x<y:
    print("x is less than y")
elif x>y:
    print("x is greater than y")
else:
    print("x is equal to y")
    
#Conditional statements of "a if b else c" form
result="x is greater than y" if x>y else "x is less than or equal to y"
print(result) #prints the result #x is less than or equal to y

#match-case statements in python 3.10
#keywords: match, case, break
#match-case statements are used to replace the if-elif-else statements #IMPORTANT
value="one"
match value:
    case "one":
        result=1
    case "two":
        result=2
    case "three":
        result="3" #we can use different datatypes in match-case statements
    case _: #default case
        result="-1"
print(result) #prints the result #1

#Loops in python
#keywords: for, while, break, continue, pass

#while loop
i=1
while i<=5:
    print(i, end=" ")
    i=i+1 #to print output in same line we can use print(i, end=" ")
#for loop
for i in range(1,6): #right side of range is open ended
    print(i)
for i in range(1,6,2): #range(start, end, step)
    print(i)
    
#using for loop on list
list=[1,2,3,4,5]
for i in list:
    print(i, end=" ")
    print(" ")
    
#break and continue statements
for i in range(1,10):
    if i==7:
        break
    print(i, end=" ")
    print(" ")
    
for i in range(1,10):
    if i%2==0: #if i is even then continue (skip) the iteration
        continue
    print(i, end=" ")
    print(" ")

#for loop with enumerate function #IMPORTANT
weekdays=["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
for i, day in enumerate(weekdays):
    print(i, day)
    
#pass statement
for i in range(1,10):
    pass #pass statement is used to avoid the error of empty block of code

#List comprehension in python IMPORTANT
#List comprehension is used to create new list from existing list
#syntax: new_list=[expression for item in list]
list=[1,2,3,4,5]
new_list=[i*i for i in list]

#class in python
#class is a blueprint of an object
class Vehicle():
    def __init__(self, bodystyle): #what is self? #self is an instance of class #What does instance of class mean? #Instance of class means object of class.
        self.bodystyle=bodystyle #what is self.bodystyle=bodystyle mean? #self.bodystyle is an instance variable and bodystyle is a local variable
        
    def drive(self,speed):
        self.mode="driving" #why driving is in double quotes and speed is in no quotes? #because driving is a string and speed is an integer.
        #but for both we have not defined any datatype of driving and speed? 
        self.speed=speed
        
class Car(Vehicle):
    def __init__(self, enginetype):
        super().__init__("Car") #super() is used to call the parent class constructor #Where is constructor in python? #Constructor is __init__ method in python.
        self.wheels=4 #What is wheel here? #wheel is an instance variable. #What is instance variable? #Instance variable is a variable which is defined inside the constructor. Is wheel a variable associated with object of class? #Yes
        self.doors=4 #can we define instance variable outside the constructor? #Yes
        #can we define local variable outside the constructor? #Yes
        #is it required to define construrctor? #No
        self.enginetype=enginetype
        
    def drive(self, speed):
        super().drive(speed) #super() is used to call the parent class method #Where is method in python? #Method is a function defined inside the class.
        print("Driving my", self.enginetype, "car at", self.speed, "kmph")
        
class Bike(Vehicle):
    def __init__(self, enginetype, hassidecar): #What is hassidecar here? #hassidecar is a local variable.
        super().__init__("Bike")
        if (hassidecar): #in if statement varible can act as boolean and by default it is true.
            self.wheels=3
        else: #in else statement variable can act as boolean and by default it is false.
            self.wheels=2
        self.doors=0
        self.enginetype=enginetype
    
    def drive(self, speed):
        super().drive(speed) #super() is used to call the parent class method #Where is method in python? #Method is a function defined inside the class.
        print("Driving my", self.enginetype, "bike at", self.speed, "kmph")
        
car1=Car("gasoline") 
car2=Car("diesel")
Bike1=Bike("gasoline", False) #both car and bike have single input argument in constructor, then why Car1=Car("gasoline") and Bike1=Bike("gasoline", False) are having unequal number of arguments? #Because Bike1=Bike("gasoline", False) is having local variable hassidecar as well.
print(car1.bodystyle)
print(car1.wheels)
print(car1.doors)
print(car1.enginetype)
print(Bike1.bodystyle)   
print(Bike1.wheels)
print(Bike1.enginetype)
car1.drive(30)
car2.drive(40)
Bike1.drive(50)

#Exception handling in python
#keywords: try, except, else, finally, raise, assert, with, as, from, import.
try:
    # Code that might raise exceptions
    result = 10 / 2  # Potential ZeroDivisionError, ValueError

except ZeroDivisionError:
    print("Division by zero is not allowed!")
    #raise  # Re-raise the exception for further handling if needed

except ValueError:
    print("Invalid input! Please enter a valid integer.")

else:
    print("Result:", result)

finally:
    print("This code always executes, regardless of exceptions.")
    print("Performing cleanup tasks here (if any)")
    
#Working with files in python
#keywords: open, close, read, write, append, seek, tell, flush, truncate, readline, readlines, writelines, with, as, from, import.
def file():
    #open a file and if doesn't exists then make one.
    myfile=open("textfile.txt", "w+") #w+ is used to open the file in write mode and + is used to create the file if it doesn't exists.
    for i in range(0,10):
        myfile.write("this is some text\n")
    #closing a file when done with it.
    myfile.close()
print(file())


#working with OS path utilities
import os
from os import path
import datetime
from datetime import date, time, timedelta
import time
from zipfile import ZipFile

def main():
    #print the name of the OS
    print(os.name)
    #check for item existence
    print("Item exists: " + str(path.exists("textfile.txt")))
    
    #check for item type
    print("Item is a file: " + str(path.isfile("textfile.txt")))
    
    #check for item is directory
    print("Item is a directory: " + str(path.isdir("textfile.txt")))
    
    #getting the path of the file
    print("Item path: " + str(path.realpath("textfile.txt")))
    
    #splitting the path and file
    print("Item path and name: " + str(path.split(path.realpath("textfile.txt")))) #split() - returns the tuple of path and file
    
    #get modification time
    t = time.ctime(path.getmtime("textfile.txt")) #time.ctime() - returns the time in human readable format #getmtime() - returns the time in seconds since modification
    print(t)
    print(datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))) #datetime.datetime.fromtimestamp() - returns the time in human readable format
    
    #calculate how long ago the item was modified
    td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("textfile.txt")) #datetime.datetime.now() - returns the current time
    #datetime.datetime.now() - datetime.datetime.fromtimestamp() - returns the difference between two dates #IMPORTANT(basically substracting two dates)
    print("It has been " + str(td) + " since the file was modified") #timedelta() - returns the difference between two dates
    print("Or, " + str(td.total_seconds()) + " seconds") #total_seconds() - returns the difference between two dates in seconds
print(main())

#using shutil module to work with files and directories
import shutil
from shutil import make_archive

def main2():
    #make a duplicate of an existing file
    if path.exists("textfile.txt"):
        #get the path to the file in the current directory
        src=path.realpath("textfile.txt")
        
        #making a backup copy by appending ".bak" to the name
        des = src+".bak"
        shutil.copy(src, des) #copy() - copies the file from source to destination
        
        #rename the original file
        os.rename("textfile.txt", "newfile.txt") #rename() - renames the file
        
        #put things into a zip archive
        root_dir, tail = path.split(src) 
        shutil.make_archive("archive", "zip", root_dir) #make_archive() - makes the zip archive
        
        #more fine-grained control over ZIP files
        with ZipFile("testzip.zip", "w") as newzip: #making newzip as an object of ZipFile class #ZipFile() - creates the zip file
            newzip.write("newfile.txt") #write() - writes the file in zip file
            newzip.write("textfile.txt.bak") 
print(main2())

#working with dates and times
from datetime import date, time
from datetime import datetime

def main3():
    #DATE OBJECTS
    #print today's date
    today=date.today() #date.today() - returns the current date
    
    #print today's date in individual components
    print("Date components: ", today.day, today.month, today.year) #today.day, today.month, today.year - returns the day, month and year respectively
    
    #print today's weekday number (0=Monday, 6=Sunday)
    days=["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
    print("Today's weekday number: ", days[today.weekday()]) #today.weekday() - returns the weekday number
    
    #DATETIME OBJECTS
    #get today's date from datetime class
    today=datetime.now() #datetime.now() - returns the current date and time
    print("The current date and time is: ", today)
    #get the current time
    t=datetime.time(datetime.now()) #datetime.time() - returns the current time
    print(t)
print(main3()) 

#Formatting time output
def main4():
    #Times and dates can be formatted using a set of predefined string
    #control codes
    now=datetime.now()
    
    #%y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
    print(now.strftime("The current year is: %Y")) #strftime() - returns the formatted date and time
    print(now.strftime("%a, %d %B, %y"))
    
    #%c - locale's date and time, %x - locale's date, %X - locale's time
    print(now.strftime("Locale date and time: %c"))
    print(now.strftime("Locale date: %x"))
    print(now.strftime("Locale time: %X"))
    
    #%I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
    print(now.strftime("Current time: %I:%M:%S %p"))
    print(now.strftime("24-hour time: %H:%M"))
print(main4())

#working with timedelta objects
from datetime import timedelta

#construct a basic timedelta and print it
print(timedelta(days=365, hours=5, minutes=1))

#print today's date
now=datetime.now()
print("Today is: "+str(now))

#print today's date one year from now
print("One year from now it will be: "+str(now+timedelta(days=365)))

#print today's date with one week ago
print("One week ago it was: "+str(now-timedelta(weeks=1)))

#create a timedelta that uses more than one argument
print("In 1000 days from now it will be: "+str(now+timedelta(weeks=2, days=3)))

#calculate the date 1 week ago, formatted as a string
t=datetime.now()-timedelta(weeks=1)
s=t.strftime("%A %B %d, %Y")
print("One week ago it was: "+s)

#working with calendar module
import calendar
from calendar import TextCalendar
from calendar import HTMLCalendar #HTMLCalendar() - creates the html calendar --not necessary
c=calendar.TextCalendar(calendar.SUNDAY) #TextCalendar() - creates the text calendar #SUNDAY - sets the first day of week as sunday
str=c.formatmonth(2021, 1, 0, 0) #formatmonth() - formats the month #2021 - year, 1 - month, 0 - number of spaces between columns, 0 - number of spaces between rows
print(str)

#loop over the days of a month
#zeroes mean that the day of the week is in an overlapping month
for i in c.itermonthdays(2021, 1): #itermonthdays() - returns the iterator for the month days
    print(i)
    
#Fetching internet data using urllib module
import urllib.request
def main5():
    #open a connection to a URL using urllib
    webUrl=urllib.request.urlopen("http://www.google.com")
    
    #get the result code and print it
    print("Result code: ", webUrl.getcode())
    
    #read the data from the URL and print it
    data=webUrl.read()
    print(data)
print(main5())