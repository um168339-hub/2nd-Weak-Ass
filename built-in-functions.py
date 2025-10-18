# Assignment: Basic Python Data Types & Input
# Taking input from user:
name = input("enter your name :") # name input  
age = input("enter your age :")    # age  input
hobby=str(input("enter your favourite hobby :")) # hobby input 
print("hey my name is "+name+" i am " , age ," years old and my faviourate hobby is "+hobby)
print(hobby.lower())      # convert the str into lower letter.
print(hobby.capitalize()) # convert the str into capital letter.
print(hobby.__len__())    # tell the number character of the string.

# Medium level Task
# 1.
def greet_user():
    user = input("Enter your name : ")
    print("Welcome " + user +" We are waiting for you " )


greet_user()

#2
sen = input("Enter any sentence : ")
print(sen.title())

#Little Bit Tough Task
#1
Adj = input("Enter adjective : ")
verb = input("Enter verb")
noun = input("Enter noun : ")
sen = Adj +" "+ noun + " " + verb
print(sen)

# 2.
def full_name(first,last):
    return first + last

first = input("Enter your first name : ")
last = input("Enter your last name : ")

print(full_name(first,last))