import random
x = "Kuk"


def myfunc():
 x = "penis"
 print("min " + x)

myfunc()

print("min " + x )

"""global x kan man lägga till för att göra varenda x i din kod till det x som du definerar som global.

T.ex. skrev du global x i def myfunc() så hade x = penis.

Dock ifall du skrev global x innan def myfunc() så hade x = kuk  
genom hela koden."""

#define X 
x = 5 

#Display X 
print(x)

#Display TYPE 
print(type(x))

#define x as something in a quote 
x = "literally anything"

#Display x
print(x)

#Display what TYPE x is
print(type(x))

"""Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset                                                  #These are the different types you can use while programming.
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview"""

import random

print(random.randrange(1, 10))

""" Hur i hela jävla helvete fungerar slicing lmao och när fan ska man egentligen använda det??? XDDDD """

a = "hello, world!"
print(a[0])

b = "hello, world!"
print(b[1:5])

#To get the lenght of a string use len()

c = "Hello, World!"

print(len(c))

#strip() tar bort mellanslaget i början o slut
 
d = " Hello, world! "

print(d.strip()) #Behöver ej vara något i strip().

#You can replace stuff with replace() function.

a = "Hello, World!"

print(a.replace("H", "J"))


"""when writing text and you want to know if a specific
phrase or character exists in the text you can use this. Hence the "true" thingy"""

txt = "Hata data tufft o vara full, vi kan supa utan att ha kul"

x  = "Hata" in txt

print(x)

#you can combine strings and numbers using the format() method. 

age = 23 

txt = "my name is Carl, and I am {}"

print(txt.format(age))

#format() klarar av att ha ett oändligt nummer av argument sålänge de är placerade i rätt ordning.

quantity = 3

itemno = 0.531215120

price = 49.99

myorder = "I want {} pieces of item {} for {} dollars." 
print(myorder.format(quantity, itemno, price))

#If you wanna use " inside of a text you can do so by using \"literally anything\" 

txt = "We are the so called \" Kallzor gang \" of this school" 
print(txt) 

"""Named Indexes
You can also use named indexes by entering a name inside the curly brackets {carname}, 
but then you must use names when you pass the parameter values txt.format(carname = "Ford"):"""

#Example

myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))


#Boolean values. True or false expressions.
print(10 > 9)

print (10 == 9)

print(9 < 10)

#It's possible to force the value to change. If you write that 9 = 10 instead of 9 == 10 it means that you're changeing the value 9 to be = 10.

#Du kan fortsätta med det här och göra "if statements" och "else" statements. t.ex.

a = 200
b = 100 
if b > a: 
    print("b is greater than a")
else: 
    print("b is not greater than a")

""" One more value, or object in this case, evaluates to False, 
and that is if you have an object that is made from a class with a __len__ 
function that returns 0 or False"""

class hatadata: 
    def __len__(self):
        return 0
myobj = hatadata()

print(bool(myobj))

#You can print functions that returns A Boolian value.

def myfunc():
    return True
print(myfunc())

#Det är möjligt att runna kod baserat på Boolean svaret ur en funktion (?) 
def myFunction():
    return True
if myFunction():
    print("YES!")
else:
    print("NO!")

#Du kan använda isinstance() funtkionen och se ifall ett objekt är en integer eller inte.

x = 200
print(isinstance(x, int)) # DETTA GER = TRUUUUE

#One more object or value evaluates to "False", and that's if you have an object that is made from a class with "__len__" function returns 0 or "False"

class myClass():
    def __len__(self):
     return 0
                                      #Detta ska egentligen bli "False men det ger mig ett True value. Förstår inte riktigt varför.
myobj = myClass()
print(bool(myobj))


def myFunc() :
    return True                   #Funkar ej heller???? 
print(myFunc())

#Detta är hur du ska använda och skapa en dictionary. Hella mysigt.

thisdict = {
    "brand": "Ford",
    "model": "Mustang",                                        #Detta ska funka också men det kan nog vara för att jag printat ut så jävla mycket skit så att programmet bah orkar inte lmao.
    "Year": 1964
    }
print(thisdict)

#Det här är hur du får upp information och söker på keywords i dictionaryn.
x = thisdict("model")
print(x)
#Det går också att göra en get() som kan ge dig samma resultat. 

x = thisdict.get("model")
print(x)

#Du kan även ändra värdet på ett specifikt item genom att hänvisa till dess nyckelnamn

thisdict["year"] = 2018
print(thisdict)  #Detta gör så att året ändras från 1964 till 2018.

#Att skriva alla värden i dictionären en och en

for x in thisdict:
    print(thisdict[x])                       #Detta gör så att alla VÄRDEN blir utprintade. Alltså "Ford, Mustang, 1964". 

#För att skriva ut båda "Keys" och "Values/värden" så kan man använda sig av items() metoden:

for x, y in thisdict.items():
    print(x, y)                             #Detta printar ut "Brand   Ford,  model    Mustang,    year   1964". Alltså inte bara ena. Jag antar att man kan använda sig av Y istället för X ifall du ska printa ut "keys" istället för "Values"

    #Såhär kan du checka för en specifik nyckel som är present in the dictionary. You should use the "in" keyword for that:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",                                        
    "Year": 1964
    }
if "model" in thisdict: 
    print("Yes, 'model' is one of the keys in the thisdict dictionary") #Detta är vad den säger.


#To determine how many items (key-value pairs) a dictionary has, use the len() function.
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964                              #This gives an answer "3" since there are in total 3 items in this dictionary.
}

print(len(thisdict))

#You can also add an item to the dictionary by using a new index key and assigning it a value:

thisdict["colour"] = "Red"
print(thisdict)                                   #This adds a new item to the dictionary.

#And this is how you remove items from the list by using the "pop()" method.

thisdict.pop("model")                    #This removes the model item. (Aka it removes bot the Value and Key. So the word model and Mustang goes away"

#The popitem() method removes the last inserted item. 
thisdict.popitem()                     #Kinda self-explanatory

#The del keyword removes the item with the specific key name. Aka: 
del thisdict["model"] #Since it removes the entire "ITEM" and not just a value or key it removes the entire thing from the dictionary. 

#You can also use the clear() method to empty the dictionary.
thisdict.clear()
#it does what it's suppose to. Clears the entire thing.

#You can also copy a dictionary using the copy() method:
mydict = thisdict.copy()
#This makes mydict the exact same as your thisdict.

#Another way to make a copy is using the built-in function dict():
mydict = dict(thisdict)
#This does the exact same thing but using a the built in system to do so.

#This is something called "Nested dictionaries" which means a dictionary that contains multiple dictionaries: 
myfamily = {
    "child1" : {
        "name" : "Emil", 
        "Year" : 2004 
        },
    "child2" : {
        "name"  : "Tobias",
        "Year" : 1997
        },
    "child3" : {
        "Name" : "Carl",
        "Year" : 1996
        }
    }
print(myfamily)

#Or, if you wanna nest already existing dictionaries together:

child1 = {
    "name" : "Emil",
    "Year" : 2004
    }
child2 = {
    "Name" : "Tobias",
    "Year" : 1997
    }
child3 = {
    "Name" : "Carl",
    "Year" :  1996
    }
myfamily = {
    "child1" : child1,
    "child2" : child2,
    "child3" : child3
    }
#Jesus christ this took long to write but it's good to know. 

#It's also possible to use the "dict()" constructor to make a new dictionary: 
thisdict = dict(brand = "Ford", model = "Mustang", Year = 1964)
#Note that keywords are not string literals. 
#Note the use of equals rather than colon for the assignment.

#Now we are going to talk about if and else statements.

#Elif is a keyword in python of saying "if the previous conditions were not true, then try this condition."

a = 33
b = 33 
if b > a:
     print("b is greater than a")
elif a == b:
    print("b and a are equal")                          #Detta kommer ge svaret att b and a are equal since the if statement is not true but the elif statement is. 


#Else is a keyword that catches anything which isn't caught by the perciding conditions.
a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("b and a are equal")
else:
    print("a is greater than b")                  #This guarantees that either of these are correct and your program will run unless there are multiple correct answers in the equation.
#It's also important to note that the "elif" command is not needed in order for this program to run. If the "if" statement is not true but the "else" statement is, the "elif" statement is not needed.

#It's possible to have multiple statements in one line. For example:
a = 330
b = 300 
print("a") if a > b else print ("=") if a == b else print("b")
#This will print you the answer "=" since a == b. and the program will ignore the rest. (Does not look very attractive tho lmao but you can basically flex with a 1 line if, else meme.

#There's a "and" keyword that works as a logical operator, and is used to combine conditional statements:
a = 200
b = 33
c = 500

if a > b and c > a:
    print("both conditions are True")

#There is also the "or" keyword that also works as a logical operator, and is used for the same reason:
a = 200
b = 33 
c = 500
if a > b or a > c:
    print("At least one of the conditions are True")

#There are also "Nested if's" that contains if statments inside of if statements.

x = 41

if x > 10:
    print("Above 10, ")
    if x > 20:
        print("and also above 20!")
else: 
            print("but not above 20")


#The pass statement. "if" statements cannot be empty, but if you for some reason have an "if" statement with no content, but the "pass" statement to avoid getting an error:
a = 33
b = 200
if b > a:
    pass
#Normally this would post an "error" if you tried to run it.

#Now we're getting into the "while" and "for" loops which will be interesting!

#With the "while" loop we can execute a set of statements  as long as a condition is true.

i = 1
while i < 6:
    print(i)
    i += 1
#This prints out "1   2   3   4   5" but downwards since it's suppose to loop until you get to the number that's just below "6". 

#The break statement:
#With the "break" statement we can stop the loop when the condition is true:
i = 1 
while i < 6:
     print(i)
     if i == 3:
         break
     i += 1
#The "continue" statement we can stop the current iteration, and continue with the next:

i = 0
while i < 6:
    print(i)
    i += 1
    if i == 3:
        continue
    print(i)                          #It will print all the numbers up to 5 EXCEPT NUMBER 3. IT WILL SKIP THE NUMBER YOU SAY i IS EQUAL TOO.

i = 1 
while i < 6:
     print(i)
     i += 1
else:
    print("i is no longer less than 6")
#This prints out every number down to 5 and after 5 it prints out "i is no longer less than 6"

"""A "for" loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set or a string):
This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.
With the "for" loop we can execute a set of statements, once for each item in a list, tuple, set etc."""

#Example print each fruit in a fruit list:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
#This lists every fruit and it looks hella fkn good.

#looping through a string. Even strings are iterable objects, they contain a sequence of characters:
for x in "banana":
    print(x)
#This basically just writes out "b a n a n a" in a vertical line (aka downwards). 

#The break statement does the same as before.
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
     break
#It prints banana but stops there and leaves "cherry" out. 

#Exit the loop when "x" is "banana", but this time the break comes before the print:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)                                      #This function prints only out "apple" since it breaks when it reaches "banana". So when "x" is to be printed only apple shows up.

#The continue statement: Do not print len
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)                           #This prints out "apple" and "cherry" but leaves out "banana" from the print.

"""The range() function:
To loop through a set of code a specified number of times, we can use the range() function,
The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number."""

#Example:
for x in range(6):
    print(x)                           #This is a quicker way to print "0  1  2  3  4  5" in vertical.

#The "range(6)" function defaults from 0 - 5 and not 1 - 6.
for x in range(2, 6):
    print(x)
#This means that this prints out "2  3  4  5" 

for x in range(2, 30, 3):
    print(x)
#This prints out "2  5  8  etc.." So if you want every number from "x, y" you can just add any number and it will make that jump instead of 1 every time.

#Else in for loop: The "else" keyword in a "for" loop specifies a block of code to be executed when the loop is finished

#Example, print all numbers from 0 to 5, and print message when loop has ended:

for x in range(6):
    print(x)
else:
    print("Finally finished!")
#This counts from 0-5 and ends with a "finally finished!" message.

#Nested loops: as the name describes it's a loop inside of a loop. The "inner loop" will be executed one time for each iteration of the "outer loop":

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x,y)
#This prints out "red apple, red banana, red cherry, big apple, big banana etc..." 

#The "pass" statement. "for" loop cannot be empty, but if you for some reason have a "for" loop with no content, put the in the "pass" statement to avoid getting an error.

for x in [0, 1, 2]:
    pass
#If you would have an empty loop like this it would result in an error. So "pass" statement avoids this problem.


""" THIS PART IS ABOUT FUNCTIONS AND ARE VERY IMPORTANT TO LEARN. EVEN THO I ALREADY KNOW MUCH OF THIS
IT'S IMPORTANT TO TAKE NOTES IF I EVER STRUGGLE TO REMEMBER SOMETHING ABOUT IT"""

#Creating a and calling on a function
def my_function():
    print("hello from a function")

my_fucntion()
#This just prints out "Hello from a function".

"""Arguments

Information can be passed into functions as arguments.

Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.

The following example has a function with one argument (fname). When the function is called, we pass along a first name, 

which is used inside the function to print the full name. Example:"""

def my_function(fname):
    print(fname + "Refsnes")

my_function("Emil")
my_function("Tobias")
my_functuib("Carl")
#Detta visar namnet + Refsnes

"""Parameters or Arguments?
The terms parameter and argument can be used for the same thing: information that are passed into a function.

From a function's perspective:

A parameter is the variable listed inside the parentheses in the function definition.

An argument is the value that is sent to the function when it is called."""

"""By default, a function must be called with the correct number of arguments.
Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less. Example:"""


def my_function(fname, lname):
    print(fname + " " + lname)

my_function("Emil", "Refsnes")
# IMPORTANT TO NOTE. IF YOU DON'T MAKE ENOUGH ARGUMENTS IT WILL NOT WORK. AKA YOU CAN'T JUST WRITE "Emil" AND NOT THE lname CUZ THEN THE PROGRAM WILL ERROR.


"""Arbitrary Arguments, *args
If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

This way the function will receive a tuple of arguments, and can access the items accordingly:"""

#Example: if the number of arguments is unknown, add a * before the parameter name:
def my_function(*kids):
    print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

#This will print out "The youngest child is Linus" since it starts counting from "0" and not "1". 

#You can also send arguments with the key = value syntax. This way the order of the arguments does not matter.

def my_function(child3, child2, child1):
    print("they youngest child is " + child3)

my_fuction(child1 = "Emil", child2 = "Pontus", child3 = "Carl")

"""Arbitrary Keyword Arguments, **kwargs
If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.

This way the function will receive a dictionary of arguments, and can access the items accordingly:"""

#Example: If the number of keyword arguments is unknown, add a double ** before the parameter name:
def my_function(**kid):
    print("And his last name is " + kid["lname"])

my_function(fname = "Carl", lname = "Pryssgård")
#This function will only print out the "lname" since I don't know beofre hand how many arguments I will have it's fine either way since I used the ** statement.


#Default Parameter Value

#If we call the function without argument, it uses the default value:

def my_function(country = "Sweden"):
    print("I am from " + country)

my_function("Finland")
my_function("India")
my_function()                                      #Here it will use the default value that is Sweden.
my_function("Canada")
#This will print out "I am from Finland", "I am from India", "I am from Norway", "I am from Canada".

"""Passing a List as an Argument
You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.

E.g. if you send a List as an argument, it will still be a List when it reaches the function:"""

#Example:
def my_function(food):
    for x in food:
        print(x)
fruits = ["Apples", "Banana", "Cherry"]

my_function(fruits)                                             #This will list all the fruits up from start to finish. Strange.

#Return values: To let a function return a value, use the "return" statement:
def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(5))
print(my_function(9))
                                                      #This will print out the answers: 15 , 25 , 45. 




"""Recursion!!!!!!!!!!!!!!!!!!!!!
Python also accepts function recursion, which means a defined function can call itself.

Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.

The developer should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates, or one that uses excess amounts of memory or processor power. However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.

In this example, tri_recursion() is a function that we have defined to call itself ("recurse"). We use the k variable as the data, which decrements (-1) every time we recurse. The recursion ends when the condition is not greater than 0 (i.e. when it is 0).

To a new developer it can take some time to work out how exactly this works, best way to find out is by testing and modifying it."""

#Example of recursion:

def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k -1)
    else:
        result = 0
        return result
print("\n\nRecursion Example Results")
tri_recursion(6)
"""This will print out "Recursion Example Results 1  3  6  10  15  21" and the numbers in a vertical line. 
Really difficult to understand and not so obvious as much of the stuff from before."""
 

#Lambda functions are a small anonymous function. A lambda function can take any number of arguments, but can only have one expression.

#Lambda arguments : expression

x = lambda a : a + 10
print(x(5))

#This prints out 15 since it adds 10 to the variable as stated. 

x = lambda a, b : a * b
print(x(5, 6))
#This will print out the answer 30 since a * b = 30 in this case.

x = lambda a, b, c : a + b + c 
print(x(5, 6, 7))
#This will print out 12 since a + b + c = 12 in this case.

"""Why Use Lambda Functions?
The power of lambda is better shown when you use them as an anonymous function inside another function.

Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:"""

def myfunc(n):
    return lambda a : a * n                      #Use this function definition to make a function that always doubles the number you send in. (You can also make it tripple or w/e you want)

mydoubler = myfunc(2)
print(mydoubler(11))

#This will result in it printing 22. 
#You can also use the same program to print multiple answers. Just create a new one below it and call it "mytrippler" instead. Just gotta print two things tho instead of one.



#Looping Array Elements. You can use the "for in" loop to loop through all the elements of an array. Example: Print each item in the "cars" array.

cars = ["Ford", "Volvo", "BMW"]

for x in cars:
    print(x)
#this just prints out the 3 words vertically after eachother. 

#You can also use the "append()" method to add an element to an array.

cars.append("Honda")
#This is just adds the "Honda" to the "cars" array. 

#You can also "pop()" method away an element from the array.

cars.pop(1) #Removes "Volvo" from the "cars" array.

#Or you can also just use the "remove()" method for the same effect basically.
cars.remove("Volvo")
#NOTE: the list's "remove()" only removes the first occurrence of the specified value.

"""Array Methods!!!!!!!
Python has a set of built-in methods that you can use on lists/arrays.

Method	Description
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the first item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list"""


# IMPORTANT!!! CLASSES BOIIIIII


"""Python Classes/Objects
Python is an object oriented programming language.

Almost everything in Python is an object, with its properties and methods.

A Class is like an object constructor, or a "blueprint" for creating objects."""

#To create a "class" you use the keyword "class" XDDD

class Myclass:
    x = 5
print(Myclass)
#This just prints out "<class '__main__.Myclass'>" idk why but it does lol

#Create object:

class Myclass:
    x = 5

p1 = Myclass()
print(p1.x)
#This will print out the int value "5". Maybe it's different cuz i'm using an object.

"""The __init__() Function
The examples above are classes and objects in their simplest form, and are not really useful in real life applications.

To understand the meaning of classes we have to understand the built-in __init__() function.

All classes have a function called __init__(), which is always executed when the class is being initiated.

Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:"""

#Example: Create a class named Person, use the __init__() function to assing values for name and age:

class Person:
    def __init__(self, name, age):
        self.name = name
        self. age = age
p1 = Person("John", 36)
print(p1.name)
print(p1.age)
#This prints out "John 36" vertically. Seems really important to learn so learn this shit boi

#Object methods 
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()
#This prints out "Hello my name is John" as expected. 
#NOTE: The "self" parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.

#The "self" parameter:
"""The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:"""

class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age
    def myfunc(abc):
        print("Hello my name is " + abc.name)
p1 = Person("John", 36)
p1.myfunc()
#This also prints out "Hello my name is John"

#You can modify and delete object properties. 
p1.age = 40 #To change age.

del p1.age #To delete age.

del p1 #To delete the entire object instead of the property.

#The "class" definition can not be empty but using the "pass" statement you can bypass this.


"""Python Inheritance
Inheritance allows us to define a class that inherits all the methods and properties from another class.

Parent class is the class being inherited from, also called base class.

Child class is the class that inherits from another class, also called derived class."""

"""Create a Parent Class
Any class can be a parent class, so the syntax is the same as creating any other class:
Example
Create a class named Person, with firstname and lastname properties, and a printname method:"""

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()
#This will print out "John Doe" horizontally and not vertically because of the "print()" layout.

#To creat a child Class: You can creat a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class:

class Student(Person):
    pass
#Use the "pass" keyword when you do not want to add any other properties or methods to the class. Now the Student class has the same properties as the Person class.

"""class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):                                   Detta finns tidigare som exempel men detta är classen som "Student" har kopierats ifrån
    print(self.firstname, self.lastname)"""

class Student(Person):
    pass

x = Student("Mike", "Olsen")
x.printname()

#This will print out Mike Olsen just like in the class before but with the new "student" class that inherited the "Person" class. 

#Add the __init__() function: So far we have created a child class that inherits the properties and methods from its parent. We want to add the __init__() function to the child class (instead of the pass keyword).

#NOTE: The __init__() function is called automatically every time the class is being used to create a new object.

class Student(Person):
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
#add properties etc


"""When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.

Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.

To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:"""

#Example:
class Student(Person):
 def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)


#Now we have successfully added the __init__() function, and kept the inheritance of the parent class, and we are ready to add functionality in the __init__() function.

#Use the "super()" function. This function will make it so that the child class inherits all the methods and properties from its parent:

class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
x = Student("Mike", "Olsen")
x.printname()
#This will print out Mike Olsen since it copies the properties and shit from its parentclass

#By using the super() function you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.

#Adding properties: You can add for example graduation year to the Student class.

class Student(Person):
    def __init__(Self, fname, lname):
        super().__init__(fname, lname)
        self.graduationyear = 2019
x = Student("Mike", "Olsen")
print(x.graduationyear)
#Can also add the x.printname() to get his name after 2019. Add this infront of the other print to get a better looking solution.
#this prints out 2019 since that's what I asked it to do. Easy way to add something to a class.

#If you want to add another variable into the "Student" class when creating student objects you can just add another parameter in the __init__ function.

class Student(Person):
    def __init__(Self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year
x = Student("Mike", "Olsen", 2019)
#Here I add the "year" variable in the first __init__ function. 

#Adding methods. Add a method called "welcome" to the "Students" class:
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
x = Student("Mike", "Olsen", 2019)
x.welcome()


#Python Iterators!!

"""Python Iterators
An iterator is an object that contains a countable number of values.

An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.

Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__()."""

#Iterator vs Iterable: Lists, tuples, dictionaries and sets are all iterable objects. They are literal "containers" which you can get an iterator from

#Use the method "iter()" to return an iterator from a tuple, and print each value:

mytuple = ("Apple", "banana", "Cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))
#This prints out "Apple  banana  Cherry" in a horizontall way one after another!

#Strings are also iterable objects, containing a sequence of characters:

mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
#This prints out "b  a  n  a  n  a" vertically.

#You can use the "for in" loop to make this easier for you.

mytuple = ("apple", "banana", "cherry")
for x in mytuple:
    print(x)
#Detta gör exakt som det första jag skrev

mystr = "banana"
for xx in mystr:
    print(x)

#THis does exactly the same as before but with less code.
#The for loop actually creates an iterator object and executes the next() method for each loop.

"""Create an Iterator
To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.

As you have learned in the Python Classes/Objects chapter, all classes have a function called __init__(), 

which allows you to do some initializing when the object is being created.

The __iter__() method acts similar, you can do operations (initializing etc.), but must always return the iterator object itself.

The __next__() method also allows you to do operations, and must return the next item in the sequence."""

#Example: Create an iterator that returns numbers, starting with 1, and each sequence will increase by one (returning 1,2,3,4,5 etc.):

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
#This prints out "1  2  3  4  5" in a vertical line.  

"""StopIteration
The example above would continue forever if you had enough next() statements, or if it was used in a for loop.

To prevent the iteration to go on forever, we can use the StopIteration statement.

In the __next__() method, we can add a terminating condition to raise an error if the iteration is done a specified number of times:"""

#Example, stop after 20 iterations:

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)
# This prints the numbers 1-20 in a vertical line.

#NOTE: THIS PASSAGE ABOVE IS VERY DIFFICULT AND PROBABLY VERY IMPORTANT TO LEARN. PLEASE ASK FOR HELP ABOUT THIS SHIT SO YOU CAN COMPREHEND IT MORE! 

#Local scope: A variable created inside a function belongs to the "local scope" of that function, and can only be used inside that function.

def myfunc():
    x = 300
    print(x)

myfunc()

#Function inside a function. As explained in the example above, the variable x is not available outside the function, but it is available for any function inside the function:

def myfunc():
    x = 300
    def myinnerfunc():
        print(x)
    myinnerfunc()
myfunc()
#And this ofcourse prints out 300. 

#Python Try Except, The "try" block lets you test a block of code for errors. The "except" block lets you handle the error. And the "finally" block lets you execute code, regardless of the result of the try- and except blocks.

 try:
     print(x)
except:
    print("An exception occurred")
#This prints out "An exception occurred"

#Print one message if the try block raises a "NameError" and another for the other errors:
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")
#This prints out "Variable x is not defined" since that's the case in this function.

#You can use the "else" keyword to define a block of code to be executed if no errors were raised:
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
#This prints out "Hello nothing wents wrong"

#The "finally" block, if specified, will be executed regardless if the "try" block raises an error or not.
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

  #This prints "Something went wrong, The 'try except' is finished"

#Raise an exception: As a Python developer you can choose to throw an exception if a condition occurs. To throw (or raise) an exception, use the raise keyword.

#Raise an error and stop the program if x is lower than 0:
x = -1
if x < 0:
    raise Exception("Sorry, no numbers below zero")
    