#!/usr/bin/env python
# coding: utf-8

# In[19]:


#Write a python program to find the factorial of a number.
series = int(input ("Please enter number for Fibonacci series? "))  

a = 0    
b = 1  
count = 0  
  
if series <= 0:        #checking if the number is valid
    print ("Please enter a Valid number")   

else:  
    print ("The fibonacci sequence of the numbers is:")  # Generating Fibonacci series 
    while count < series:  
        print(a)  
        c = a + b   
        a= b 
        b= c 
        count += 1  


# In[1]:


#  Write a Python program to get the third side of right-angled triangle from two given sides
import math

a = float(input("Enter base: "))
b = float(input("Enter height: "))
x = float(input("Enter angle: "))

c = math.sqrt(a ** 2 + b ** 2)

print("Hypotenuse =", c)


# In[2]:


# Write a python program to check whether a given string is palindrome or not

#Input any string from user
string=input("please enter the string") 

#slicing the string from last and storing in String2
string2=string[-1::-1]

#checking if the string are same 
if(string==string2):
    print("It is a palindrome")
else:
    print("It is not a palindrome")


# In[3]:


# Write a python program to find whether a number is prime or composite.
num= int(input("Enter number"))

if (num==0 or num==1):                 # checking the entered number if it zero or one
    print("Number is neither composite nor Prime")
elif num>1 :
        if(num%2 == 0):                #checking if the entered number can have factors
            print(num,"is composite number")
        else:
            print(num, "is prime number")


# In[4]:


#Write a python program to print the frequency of each of the characters present in a given string
Input_str=input("Enter the string")
x=set()
result=''

for i in Input_str:
    if i not in x:
        x.add(i)
        result=result+str(Input_str.count(i))+i
print("The count of the alphabet is :" +result)


# In[ ]:




