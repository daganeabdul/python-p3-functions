#!/usr/bin/env python3

def greet_programmer():
    print(f"Hello, programmer!")
greet_programmer()    

def greet(name):
    print(f"Hello, {name}!")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

greet_with_default()
greet_with_default("sunny")    

def add(num1, num2):
    return num1 + num2
sum = add(45,55)
print(f"{sum}")

def halve(number):
   if not isinstance(number, (int, float)):
       return None
   return number/2
   
print(f"{halve(4)}")
print(f"two")