#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n = input("Enter the Number ")

def test_prime(n):
     
    if "^" in n:
        n = n.replace("^","**")
    x = eval(n)
    if (x==1):
        return False
    elif (x==2):
        return True;
    else:
        for i in range(2,x):
            if(x % i==0):
                return False
        return True             
       
test_prime(n)

