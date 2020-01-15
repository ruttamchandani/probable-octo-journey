# -*- coding: utf-8 -*-
"""
Name: Dnyanai Surkutwar
Batch: MSIS 
Assignment: Project 1

Team Members: 1) Dnyanai Surkuwtar - 00001586576
              2) Resham   
              3) 
              4)
   \\\ Comments explaining what you d 
"""
import random 
from sympy import primerange

def funcFib():
    
    while True:
        usrNo = input("Give the number (n):")
        if usrNo.isnumeric() and int(usrNo)!=0:
                break
        else: 
                print("Invalid number, please put only natural numbers")
            
        ####fibNo =[range(int(usrNo))]
        ####print (fibNo[len(int(usrNo))-1] = fibNo[len(int(usrNo))-2] + fibNo[len(int(usrNo))-4])
    no1,no2 = 0,1 
    count = 0
    
    if int(usrNo)==1:
        print (usrNo)
    else:
        while count<int(usrNo):
            print (no1)
            nNo = no1 + no2
            no1 = no2
            no2 = nNo
            count += 1
    
def funcMul():
    while True:
        usrNo = input("Give the number (n):")
        if usrNo.isnumeric() and int(usrNo)!=0:
            break
        else: 
            print("Invalid number, please put only natural numbers")
        
    for i in range(1,int(usrNo),1):
            if  not i%15:
                print ("FizzBuzz")
            elif not i%5:
                print ("Buzz")
            elif not i%3:
                print ("Fizz")
            else:
                print (i)

def funcPrm():
    while True:
        usrNo = input("Give the number (n):")
        if usrNo.isnumeric() and int(usrNo)!=0:
            print (str(primerange(1,int(usrNo)))) 
            break
    
    else: 
            print("Invalid number, please put only natural numbers")
        
"""
   for i in range(int(usrNo)):
        if prime(i):
            print (i)
"""
        
   
   
        
# is it a solution for the longway?
def funcRnd():
    while True:
        usrNo = input("Give the number (n):")
        if usrNo.isnumeric() and int(usrNo)!=0 and int(usrNo)<=101:
            
            break
        else: 
            print("Invalid number, please put only natural numbers")
            
   
    lst = []
    """
    for i in range(-50,51,1):
        lst.append(i)          
         
    
        lst2 = []
    for x in lst2:
        
        if len(lst2)<int(usrNo):
            
            lst2[x].append(random.choice(lst))
    
        print (lst2)
    """
    for x in range(int(usrNo)):
        lst.append(random.randint(-50,50))


    print (lst)

    
    
def funcExit():
    print("Exiting...")

dictMenu = {'1':funcFib,'2':funcMul,'3': funcPrm,'4':funcRnd,'0': funcExit}
 
goodChoice = True
    
while goodChoice:

    print ("_"*100 + "\nOption 1: Fibonacci Series\nOption 2: Multiples of 3, 5 and both\nOption 3: Print the prime numbers \nOption 4: Print random number list of length n")
    
    
    while True:
        usrIn = input("Please give an option from the above menu or press 0 to exit: ")
        if usrIn.isnumeric():
            break
        else:
            print ("Please select the correct menu option")
    
    if usrIn in dictMenu.keys():
        if int(usrIn)==0:
            dictMenu[usrIn]()
            break
        else:
            dictMenu[usrIn]()
    else:
            print("Please give proper choice")
  
       


 