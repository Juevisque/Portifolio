 
import datetime
from time import sleep 

# >>>>> Variables

#nome, idade, bonito = "Cleiton", 80, True

#x, y = int(input("Digite sua senha: ")), int(input("Digite sua outra senha: "))

# patrick = spongeBob = sand = squidward = 30
# print(patrick, spongeBob, sand, squidward)





# >>>>> String methods

#name = "agora deu o krai mesmo viu"

#print(len(name))
#print(name.find("d"))
#print(name.capitalize())
#print(name.upper())
#print(name.lower())
#print(name.isdigit())
#print(name.isalpha())
#print(name.count("a"))
#print(name.replace("a","o"))
#print(name*4)





# >>>>> type casting

# x = 1
# y = 2.0
# z = "3"

# print(float(x))
# print(str(y))
# print(int(z))





# >>>>> input

# name = input("What's your name? ")
# age = int(input("How old are you? "))
# height = float(input("How tall are you? "))

# print("Hello", name, "You are", age, "year old and ", height, "cm tall")





# >>>>> Math functions

import math

#pi = 3.14
# x = 1
# y = 2
# z = 3

#print(round(pi))
#print(math.ceil(pi))
#print(math.floor(pi))
# print(abs(pi)) # How far is from 0
# print(pow(pi, 2))
# print(math.sqrt(pi))
# print(max(x,y,z))
# print(min(x,y,z))





# String slicing = Index[start:stop:step] and slice(start,stop,step) 

#>>> Index[]

# name = "joão lucas"

# first_name = name[:4]

# last_name = name[5:]

# reverse_name = name[::-1]

# funky_name = name[::2]

# print(first_name)
# print(last_name)
# print(reverse_name)
# print(funky_name)

#>>> slice()

# website = "https://google.com"
# website1 = "https://wikpedia.com"

# slice = slice(8,-4)

# print(website[slice])
# print(website1[slice])




# >>>>> if statement

# age = int(input("How old are you? "))

# if age == 100:
#     print("You are a centuary old!")
# elif age >= 18:
#     print("You are an adult!")
# elif age < 0:
#     print("You haven't been born yet!")
# else:
#     print("You are a child!")





# >>>>> logical operators (and,or,not)

# temp = int(input("What is the temperature outside? "))

# if not(temp >= 0 and temp <= 30):
#     print("The temperature is bad today!")
# elif not(temp < 0 or temp > 30):
#     print("The temperature is good today!")





# >>>>> While loop

# name = ""

# while len(name) == 0:
#     name = input("Enter your name: ")

# print("Hello", name)




# >>>>> For Loop

# for i in range(10):
#     print(i+1)

# for i in range(50, 100+1,2):
#     print(i)

# for i in "joão Lucas":
#     print(i)

# import time

# for seconds in range(10,0,-1):
#     print(seconds)
#     time.sleep(1)
# print("Kaboom!")





#>>>>> Nested loop = (Loop in a Loop)

# rows = int(input("How many rows?: "))
# columns = int(input("How many columns?: "))
# symble = input("what symble?: ")

# for i in range(rows):
#     for j in range (columns):
#         print(symble, end="")
#     print()





#>>>>> Loop control statements [break,continue,pass]

#>>> break = used to terminate the loop intirely
# while True:
#     name = input("Enter your name: ")
#     if name != "":
#         break

#>>> continue = skips to the next iteneration of the loop
# phone = "11 12345 6789"
# for i in phone:
#     if i == " ":
#         continue
#     print(i, end="")

#>>> pass = does nothing, acts like a place holder
# for i in range(1,21):
#     if i == 13:
#         pass
#     else:
#         print(i)





# >>>>> list

# food = ["pizza","hamburgers","hot dog","spaghetti","pudding"]

# food[0] = "sushi"

# food.append("ice cream")
# food.remove("hot dog")
# food.pop()
# food.inset(0,"cake")
# food.sort() #alphabetical order
# food.clear()

# for x in food:
#     print(x)





#>>>>> 2D lists = a list of lists

# drinks = ["coffee","soda","tea"]
# dinner = ["pizza","hot dog","hamburger"]
# dessert = ["cake","ice cream"]

# food = [drinks,dinner,dessert]

# print(food[1][1]) #first index is for the lists, and the second one is for the topic in the list






#>>>>> Tuples = collection which is ordered and unchangeble, used to group together related data

# student = ("joão",15,"male")

# print(student.count("joão"))
# print(student.index("male"))

# for x in student:
#     print(x)

# if "joão" in student:
#     print("joão is here!")





#>>>>> Set = collection which is unordered, unindexed. No duplicated values

#utensils = {"fork","spoon","knife"}
#dishes = {"bowl","plate","cup","knife"}

# utensils.add("napkin")
# utensils.remove("fork")
# utensils.clear()
#utensils.update(dishes)
#dinner_table = utensils.union(dishes)

#print(utensils.difference(dishes))
#print(utensils.intersection(dishes))

# for x in utensils:
#     print(x)





# dictionary = a changeble, unordered collection of unique key:value pairs. Fast because they use hashing, allow us to access a value quickly

#capitals = {"USA":"Whashington DC",
#            "India":"New Dehli",
#            "China":"Beijing",
#            "Russia":"Moscow"}

#capitals.update({"Germany":"Berlin"})
#capitals.update({"USA":"Las Vegas"})
#capitals.pop({"China"})
#capitals.clear()

#print(capitals["Germany"])
#print(capitals.get("germany"))
#print(capitals.keys())
#print(capitals.values())
#print(capitals.items())

#for key, value in capitals.items():
#    print(key,value)





# *args = (Argumnents) prameter that will pack all arguments into a tuple, useful so that a function can accept a varying amount of arguments

#def add(*bro):
#    sum = 0
#    bro = list(bro)
#    bro[0] = 0
#    for i in bro:
#        sum+=i
#    return sum
#
#print(add(1,6,4,3,5))





# **kwargs = (KeyWordArguments)parameter that will pack all arguments into a dictionary, useful so that a function can accept a varying amount of keyword argument

#def hello(**jojo):
#    print("Hello",end=" ")
#    for key,value in jojo.items():
#        print(value,end=" ")

#hello(Title="Mr.",first="joão",middle="Lucas",middle2="Ferreira",last="Mendes")





# str.format() = optional method that gives users more control when displaying output

#number = 1000

#print("The number is {:.3f}".format(number))
#print("The number is {:,}".format(number))
#print("The number is {:b}".format(number))
#print("The number is {:o}".format(number))
#print("The number is {:X}".format(number))
#print("The number is {:E}".format(number))





# Decorators = make adding extra featured to function a lot more easier and versitale
# from functools import wraps
# from time import perf_counter, sleep

# def get_time(func):

#     def wrapper(*args, **kwargs):
#         start_time = perf_counter()
#         func(*args,*kwargs)
#         end_time = perf_counter()
#         total_time = round(end_time - start_time, 2)

#         print(total_time, 'secounds')
#     return wrapper

# @get_time #-- Decorator
# def do_something(param: str):
#     sleep(1)
#     print(param)

# if __name__ == '__main__':
#     do_something('hello!')

