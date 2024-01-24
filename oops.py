#class: A blueprint for creating objects of a particular type
#method: Regular funtion that are part of a class
#attribute: Variables that hold data that are part of a class
#objects: A specific instance of a class
#inheritance: Means by which a class can inherit capabilities from another class
#composition: Means of building complex objects out of other objects

#create basic class
class Book:
    def __init__(self,title):
        self.title = title
        
#creating instance of the class
book1=Book("Bhagavad Gita") #why we are passing only one argument when the funtion is accepting two arguments? Ans: self is passed automatically
book2=Book("Ramayana")
print(book1) #prints the memory location of the object
print(book1.title) #prints the title of the book1

#Instance methods and attributes

class Libre:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
#creating instance method
    def getprice(self): #every method must be defined inside the class
        if hasattr(self,"_discount"):
            return self.price-(self._discount*self.price)
        else:
            return self.price
    def getauthor(self):
        return self.author
    def setdiscount(self,amount):
        self._discount=amount #_discount is a private variable. #What is a private variable? Ans: A private variable is a variable that can be accessed only inside the class

l1=Libre("Bhagavad Gita","Veda Vyasa",100)
l2=Libre("Ramayana","Valmiki",200)

print(l1.getprice()) #prints the price of the book1
print(l1.getauthor()) #prints the author of the book1
l1.setdiscount(0.25)
print(l1.getprice()) #prints the price of the book1 after discount

class Newspaper:
    def __init__(self,name):
        self.name=name
        
n1=Newspaper("Times of India")
n2=Newspaper("The Hindu")
print(n1) #prints the memory location of the object
print(n1.name) #prints the name of the newspaper

#using type() to inspect the object type

print(type(n1.name)) #prints the type of the name of the newspaper
print(type(n1)) #prints the type of the object

#comparing type() of object
print(type(book1)==type(book2)) #returns a boolean result
print(type(book1)==type(n1))

#use isinstance to compare a specific instance to a known type
print(isinstance(n1,Newspaper)) #returns a boolean result
print(isinstance(book1,Book))
print(isinstance(n2,Book))
print(isinstance(n2,object)) #n2 is object

#class methods and static methods and members

class book:
    BOOK_TYPES=("Hardcover","Paperback","Ebook") #class variable
    
    #double underscore is used to make the variable private, it's hidden from other classes
    __booklist=None #private variable
    
    #adding a "CLASS METHOD" that also returns books type list #instead of recieving object as first argument, it recieves class as first argument
    @classmethod #decorator
    def get_book_types(cls): #cls is used to refer to the class
        return cls.BOOK_TYPES
    
    #creating a static method
    def getbooklist():
        if book.__booklist==None: #if the booklist is empty
            book.__booklist=[] #create an empty list
        return book.__booklist #return the list as output of the function getbooklist() #what is the use of this function? Ans: It is used to create a singleton object. #what is a singleton object? Ans: A singleton object is an object that is created only once and used throughout the program
    
    def set_title(self,newtitle):
        self.newtitle=newtitle #instance variable
    def __init__(self,title,booktype): #What is the primary purpose of the init method? #to initialize the instance content such as properties and variables
        self.title=title
        if(not booktype in book.BOOK_TYPES): #using class name with reference to the class variable
            raise ValueError(f"{booktype} is not a varlid booktype") #f is used to format the string #{booktype} is used to print the value of the variable booktype
        else:
            self.booktype=booktype
            
#accessing the class attribute:
print("Book types: ", book.get_book_types()) #prints the book types
            
#creating some book instances
b1=book("Title1","Hardcover")
b2=book("Title2","Paperback")

#use static method to access a singleton object
thebooks=book.getbooklist() #thebooks is a list #what is book.getbooklist()? Ans: It is a static method
thebooks.append(b1)
thebooks.append(b2)
print(thebooks)

#inheritance and composition in python
#inheritence defines a way for a given class to be able to inherit the methods and properties of another class.
#composition is a way to combine objects or classes into more complex data structures or software implementations.

class Publication:
    def __init__(self,title,price):
        self.title=title
        self.price=price

class Period(Publication):
    def __init__(self,title,price,period,publisher):   #Period class inherits the properties of the Publication class
        super().__init__(title,price)       #What is the purpose of the init method? Ans: To initialize the instance content such as properties and variables
        self.period=period
        self.publisher=publisher
    
class books(Publication): #books class inherits the properties of the Publication class
    def __init__(self, title, author, price):
        super().__init__(title,price) #super() is used to call the init method of the parent class
        self.author=author
        
class magzine(Period):
    def __init__(self,title,publisher,price,period):    #magzine class inherits the properties of the Period class
        super().__init__(title,price,publisher,period)
        
class newspaper(Period):    #newspaper class inherits the properties of the Period class
    def __init__(self,title,publisher,price,period):
        super().__init__(title,price,publisher,period)
        
book3=books("Bhagwat Gita","Veda Vyasa", 100)
mag=magzine("Times of India","Times Group",50,"Weekly")
news=newspaper("The Hindu","The Hindu Group",25,"Daily")
print(book3.author)
print(mag.publisher)
print(news.period)

#Abstract Base Classes
#Abstract Base Classes or ABCs are a way of forcing classes to implement particular methods from an interface without actually forcing them to inherit from that interface.

from abc import ABC, abstractmethod
class GraphicShapre(ABC): #why we are defining graphic shape, if it not having any input arguments? Ans: It is an abstract class #If it is having no arguments, then why we need to define it, we can make Circle and Square class independently? Ans: We can make Circle and Square class independently, but we are defining GraphicShape class because we want to make sure that Circle and Square class should have calcarea method.
    
    def __init__(self):
        super().__init__()
    @abstractmethod #decorator #what is a decorator? Ans: A decorator is a function that takes another function and extends the behavior of the latter function without explicitly modifying it.
    def calcarea(self):
        pass
    
class Circle(GraphicShapre):
    def __init__(self,radius):
        self.radius=radius
    def calcarea(self):
        return 3.14*(self.radius**2)
    
class Square(GraphicShapre):
    def __init__(self,side):
        self.side=side
    def calcarea(self):
        return self.side*self.side
    
c=Circle(10)
s=Square(10)
print(c.calcarea())
print(s.calcarea())

#Multiple Inheritance

class A:
    def __init__(self):
        super().__init__()
        self.prop1="prop1"
        self.name="A"
        
class B:
    def __init__(self):
        super().__init__()
        self.prop2="prop2"
        self.name="B"
        
class C(A,B): #C inherits the properties of A and B
    def __init__(self):
        super().__init__()
        
    def showprops(self): #why we are defining showprops method as previous we were not defining any method to print results in above code?
        print(self.prop2)
        print(self.prop1)
        print(self.name)  #A will be printed as it is defined after B in the class C #what is the reason behind this? Ans: Because C inherits the properties of A and B, and A is defined before B in the class C 
        
c=C()
c.showprops()

#Interfaces in Python
#Interfaces are a way of enforcing the structure of an object. They specify the names of methods and properties that the object must have. They don't specify what those methods and properties should do.

from abc import ABC, abstractmethod
class GraphicShapre(ABC):
    def __init__(self):
        super().__init__()
    @abstractmethod 
    def calcarea(self):
        pass
    
class JSONify(ABC):
    @abstractmethod
    def to_json(self):
        pass
    
class Circle(GraphicShapre, JSONify): #what is JSONify? Ans: JSONify is an interface #can we write something else instead of JSONify to get output in JSON format? Ans: Yes, we can write anything else instead of JSONify to get output in JSON format
    def __init__(self,radius):
        self.radius=radius
        
    def calcarea(self):
        return 3.14*(self.radius**2)
    
    def to_json(self):
        return f"{{\"Circle\":{str(self.calcarea())}}}" #what is the use of this function? Ans: It is used to convert the output of the calcarea() method into JSON format
    #what is JSON? Ans: JSON stands for JavaScript Object Notation. JSON is a lightweight format for storing and transporting data. JSON is often used when data is sent from a server to a web page.
    #what does f mean in the above code? Ans: f is used to format the string
    #what does str mean in the above code? Ans: str is used to convert the output of the calcarea() method into string format
    #how the above

c=Circle(20)
print(c.to_json())
print(Circle(10).to_json())

#Composition in Python

class Book:
    def __init__(self,title,price,author=None):
        self.title=title
        self.price=price
        
        self.author=author
        
        self.chapters=[]
        
    def addchapter(self,chapter):
        self.chapters.append(chapter)
        
    def getbookpagecount(self):
        result=0
        for ch in self.chapters:
            result+=ch.pages
        return result
        
class Author():
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    
    def __str__(self):
        return f"{self.fname} {self.lname}"
    
class Chapter:
    def __init__(self,name,pages):
        self.name=name
        self.pages=pages

auth=Author("Leo","Tolstoy")
b1=Book("War and Peace",39.0,auth)
b1.addchapter(Chapter("Chapter 1",125))
b1.addchapter(Chapter("Chapter 2",97))

print(b1) #prints the memory location of the object
print(b1.author)
print(b1.title)
print(b1.getbookpagecount())

#Magic Methods in Python
#Magic methods are special methods which have double underscores at the beginning and end of their names. They are also known as dunders.
#Customise object behavior and integrate with the language
#defines how objects are represented as strings
#control access to attribute values, both for get and set
#built in methods that are called to implement basic operations (like comparision and equality testing capabilities)
#allow objects to be called as functions

class book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
        
        #using __str__ method to return a string
    def __str__(self):
        return f"{self.title} by {self.author}, costs {self.price}"
    
    #using __repr__ method to return an object representation
    def __repr__(self):
        return f"title={self.title}, author={self.author},price={self.price}"
    
b1=book("War and Peace","Leo Tolstoy",39.0)
b2=book("The Catcher in the Rye","JD Salinger",29.0)
print(b1) #prints the output of the __str__ method #WHY it is not returning memory location of b1? Ans: Because we have defined __str__ method in the class book
#It means it will return memory location of b1, if __str__ method is not used? Ans: Yes 
print(b2) #by-default print() always calls __str__ method
print(str(b1))
print(repr(b2))

class book:
    def __init__(self,title,author,price):
        super().__init__()
        self.title=title
        self.author=author
        self.price=price
        
    #using __eq__ method to check equality between two objects
    def __eq__(self, value):
        if not isinstance(value,book):
            raise ValueError("Can't compare book to a non-book")
        return (self.title==value.title and self.author==value.author and self.price==value.price)
    
    #the __ge__ establishes >= relationship with another object
    def __ge__(self,value):
        if not isinstance(value,book):
            raise ValueError("Can't compare book to a non-book")
        return self.price>=value.price
    
    #the __lt__ establishes < relationship with another object
    def __lt__(self,value):
        if not isinstance(value,book):
            raise ValueError("Can't compare book to a non-book")
        return self.price<value.price
    
b1=book("War and Peace","Leo Tolstoy",39.0)
b2=book("The Catcher in the Rye","JD Salinger",29.0)
b3=book("War and Peace","Leo Tolstoy",39.0)
b4=b1

print(b1==b3) #prints True
print(b1==b2) #prints False
print(b1==b4) #prints True
# print(b1==39.0) #prints ValueError: Can't compare book to a non-book
print(b1>=b2) #prints True
print(b1<b2) #prints False

#SORTING OBJECTS
books=[b1,b2,b3,b4]
books.sort() 
print([book.title for book in books]) #prints the title of the books in sorted order

#Accessing Object Attributes
class book:
    def __init__(self,title,author,price):
        super().__init__()
        self.title=title
        self.author=author
        self.price=price
        self._discount=0.1
        
    #__getattribute__ is called whenever any attribute of a class is retrieved
    #dont directly access the attribute name otherwise a recursive loop is created
    #instead use the super() function to retrieve it
    def __getattribute__(self,name):
        if name=="price":
            p=super().__getattribute__("price")
            d=super().__getattribute__("_discount")
            return p-(p*d)
        return super().__getattribute__(name)
    
    #__setattr__ is called whenever any attribute value is set
    #dont set the attribute value directly otherwise a recursive loop causes a crash
    def __setattr__(self,name,value):
        if name=="price":
            if type(value) is not float:
                raise ValueError("The price attr must be a float")
        return super().__setattr__(name,value)
    
    #__getattr__ is called whenever __getattribute__ is called and an attribute can't be found
    def __getattr__(self,name):
        return name+" is not here!"
 
b1=book("War and Peace","Leo Tolstoy",39.0)
b2=book("The Catcher in the Rye","JD Salinger",29.0)
b1.price=float(40)
#b1.price=38.0
print(b1.price) #prints 34.2
print(b1)
print(b1.random) #prints random is not here!

#Callable Objects
#callable objects are objects that can be called like functions
class book:
    def __init__(self,title,author,price):
        super().__init__()
        self.title=title
        self.author=author
        self.price=price
        
    def __str__(self):
        return f"{self.title} by {self.author}, costs {self.price}"
        
    def __call__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
        
    #__call__ and __str__ are used together to make the object callable
        
b1=book("War and Peace","Leo Tolstoy",39.0)
print(b1) #prints the output of the __str__ method
b1("Anna Karenina","Leo Tolstoy",39.0)
print(b1) #prints the output of the __str__ method

#DATA CLASSES -- NEW IN PYTHON 3.7 EASIER WAY TO CREATE CLASSES -- Kamal ki cheez hai
#Data classes are a way of automatically generating boiler-plate code for classes which store data.
from dataclasses import dataclass
@dataclass
class Book:
    title:str
    author:str
    pages:int
    price:float
    
#creating instances of the dataclass
b1=Book("War and Peace","Leo Tolstoy",1225,39.0)
b2=Book("The Catcher in the Rye","JD Salinger",234,29.0)
b3=Book("War and Peace","Leo Tolstoy",1225,39.0)

print(b1.title)
print(b2.author)
print(b1.pages)

#print book itself - dataclasses implement __repr__
print(b1)

#comparing two dataclasses - they implement __eq__
print(b1==b2)
print(b1==b3)

#change some fields
b3.title="Anna Karenina"
b3.pages=864
print(b3.title)
print(b3.pages)
print(b3)

#using post initialization
#post init is called after the object is initialized via the constructor, lets us customize additional properties
#after the object has been initialized via built-in __init__ method
from dataclasses import dataclass
@dataclass
class Book:
    title:str
    author:str
    pages:int
    price:float
    
    def __post_init__(self):
        self.description=f"{self.title} by {self.author}, {self.pages} pages"  #what is the use of this function? Ans: It is used to create a description of the book
    
#creating instances of the dataclass
b1=Book("War and Peace","Leo Tolstoy",1225,39.0)
b2=Book("The Catcher in the Rye","JD Salinger",234,29.0)
b3=Book("War and Peace","Leo Tolstoy",1225,39.0)

#use description attribute
print(b1.description)
print(b2.description) 

#using default values
#default values can be specified for attributes
from dataclasses import dataclass, field
import random
def code_func():
    return random.randint(10,40)
@dataclass
class Book:
    title:str="No Title"
    author:str="No Author"
    pages:int=0
    price:float= field(default=10.0)
    code:int=field(default_factory=code_func) #what is the use of this function? Ans: It is used to generate a random code for the book
    
b1=Book()
print(b1)
b2=Book("War and Peace","Leo Tolstoy",1225) #price is not specified so it will take default value
print(b2)

#Immutable Data Classes
#dataclasses can be made immutable by setting frozen=True

from dataclasses import dataclass
@dataclass(frozen=True) #what is the use of frozen=True? Ans: It is used to make the dataclass immutable
class ImmutableClass:
    value1:str="Value 1"
    value2:int=0
    
obj=ImmutableClass()
print(obj.value1,obj.value2) #prints Value 1 0 #why it is not printing memory location of the object? #Ans: Because we have defined __str__ method in the class ImmutableClass
#where is it defined? Ans: It is defined in the dataclass module
#obj.value1="Another value" #prints AttributeError: can't set attribute #why we are getting this error? Ans: Because the dataclass is immutable
#IMMUATABLE IN ANY SITUATION