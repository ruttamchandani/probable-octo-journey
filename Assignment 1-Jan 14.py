#!/usr/bin/env python
# coding: utf-8

# In[1]:


# variable assignment
invalidInput = True
invalidOption = True
start = 1
tempFlag = True

# start of prime function
def isPrime(end):
    for val in range(start, end + 1): 
        if val > 1: 
            for n in range(2, val): 
                if (val % n) == 0: 
                    break
            else: 
                print(val) 
# end of prime function

# start of fibonacci function
def recur_fibo(n):
    count = 0
    n1, n2 = 0, 1
    while count < n:
        print(n1)
        nth = n1 + n2
       # update values
        n1 = n2
        n2 = nth
        count += 1
# end of fibonacci function

# start of main code
options = {'1' : 'Option 1: Calculate fibonacci', '2' : 'Option 2: FizzBuzz', '3' : 'Option 3: Calculate prime numbers',            '4' : 'Option 4: Create vector of random numbers', '0': 'Press 0 to exit'}

while (tempFlag == True):
    for key in options:
        print (options[key])
    userSelection = input("Select an option: ")
    
    if userSelection.isnumeric():
        selectedOption = int(userSelection)
        if selectedOption == 0:
            break
        elif selectedOption == 1:
            tempEnd = input("Enter a number: ")
            if tempEnd.isnumeric():
                invalidInput = False
                end = int(tempEnd)
                print("Fibonacci sequence:")
                recur_fibo(end)  
            else:
                print("That was not a valid number")
                
        elif selectedOption == 3:
            tempEnd = input("Enter a number: ")
            if tempEnd.isnumeric():
                invalidInput = False
                end = int(tempEnd)
                print("Prime numbers: ")
                isPrime(end)
            else:
                print("That was not a valid number")
        else:
            print("Select a valid option")
    else:
        print("Select a valid option")
        
    #invalidOption = False
    #selectedOption = int(userSelection)
    #if selectedOption == 0 or 1 or 2 or 3 or 4:
        #tempFlag = False
        #break
            
#tempEnd = input("Enter a number: ")

#if tempEnd.isnumeric():
    #invalidInput = False
    #end = int(tempEnd)
    
    #print("Prime numbers: ")
    #isPrime(end)
    
    #print("Fibonacci sequence:")
    #recur_fibo(end)    
            
#else:
    #print("That was not a valid number")
# end of main code


# In[ ]:





# In[ ]:




