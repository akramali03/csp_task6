car = 3
cars = "Class"

print(car, cars) # print statement

#this is a comment

# below is a for loop 

alphabet = "Akram Ali"
for x in alphabet:
  print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#below is an if else statement

a = 10
b = 40

if a > b:
    print ("a is greater than b")
else:
        print ("a is not greater than b")

# below is an example of variables and datatypes in python

x = 5       #integer
y = "John"  #str
c = 8.9     #float
print(x)
print(y)
print(z)

# converting the datatypes in python

a = 10

b = str(a)
print(b)

c = float(a)
print(c)

z = 7.0

x = int(z)
print (x)


#functions

def greeting():  #declaring the function
     print ("Hi welcome")
     print ("to the class")

greeting()  #calling the function

#function - argument - parameter

def greeting(name): #parameter
     print("hello" + name)

    greeting("akram") #argument
     

def add(number1, number2): #parameter
     print (number1 + number2)

     add(100,200) #argument

# String methods in python

name = "Hello world"

x = name.capitalize()

print (x)

txt = "I love apples, apple are my favorite fruit"

y = txt.count("apple")

print(y)

demo = "Hello, welcome to my world."

s = demo.index("welcome")

print(s)


