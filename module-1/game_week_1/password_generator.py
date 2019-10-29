#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 16:42:22 2019

@author: enriqueortiz
"""
""" We will create a strong password generator """ 

import random


numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

special_c = ['!', '#', '@', '%', '&', '/', '?', '*', '+', '$']

lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
         'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

upper = [x.upper() for x in lower]


#We will create a strong password. 

def create_block():
    """ let's create a 4-character block."""
    
    num = random.choice(numbers)
    special = random.choice(special_c)
    low = random.choice(lower)
    upp = random.choice(upper)
    
    summ = "".join([str(num), special, low, upp])
    
    return summ


#Nice, so the code works. Now, le'ts create three of those blocks joined by '-'
  
b1 = create_block()
b2 = b1 + "-" + create_block()
b3 = b2 + "-" + create_block()
password = b3 + random.choice(special_c) + random.choice(lower)


print("\nHi! Welcome to the super-safe password generator.")
print("\nWe will create an ultra-safe, 16-character password just for you.")
print("\nGenerating password...")
print("Generating password...")
print("Generating password...")   
print(f"\nPassword ready. \nThis is your ultra-safe password: {password}")

ask = input("Would you like to store your password in a document in your computer? ")
filename = 'books.txt'


if ask == 'yes':
    program = input("What key word would you like to associate with the password? "
                    "For example, something like 'spotify'. Write a key word: ")
    with open(filename, 'a') as file_object:
        file_object.write("\nPassword for " + program + ": " + password)
    print("\nNoted. We safely stored your password and keyword in a document called 'books.txt',"
          " which can be found in your current directory.")
        

else:
    print("Okay, no problem. Come back when you'd like to!")


    
    
    
    
    
    
    
    
    
    
    
    
    
    