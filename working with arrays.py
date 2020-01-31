#!/usr/bin/env python
# coding: utf-8

# In[1]:


import array as arr
a=arr.array('d',[1.1,3.5,4.5])
print(a)


# In[3]:


import array as arr
print("array using array package")
a=arr.array('i',[2,4,6,8])
print(a)
import numpy as np
import matplotlib.pyplot as plt
print("array using numpy")
a=np.array([1,2,3])
print(np.log(a))


# In[4]:


l=[[1,2,3],[3,6,9],[2,4,6]]
a=np.array(l)
print(a)
print(a.shape)


# In[5]:


d=([1,2,3],[3,6,9])
print(type(d))
a=np.array(d)
print(d)



# In[6]:


z=np.ones((1,2))
print(z)


# In[7]:


r=np.random.random((1,1))
print(r)


# In[8]:


f=np.full((4,4),5)
print(f)


# In[15]:


a=np.matrix('1,2,3,4;4,5,8,9;4,2,7,3;4,8,2,1')
print(a)
a.getI()


# In[20]:


A = np.matrix('1 3 5 7;2 4 6 8;1 4 7 0;2 5 8 11')
print("Original Array:")
print("\n",A)
print("\nTranspose",A.transpose())

Amax, Amin = A.max(), A.min()
x = (A - Amin)/(Amax - Amin)
print("After normalization:")
print(x)


# In[24]:


import math
l=([1,2,3],[3,6,9],[2,4,6])
a=np.array(l)
print(a)
c=1/math.tan(1)
d=1/math.tan(2)
e=1/math.tan(3)
print(c)
print(d)
print(e)


# In[25]:


import numpy as np
x = np.array([1., 2., .2, .3])
print("Original array: ")
print(x)
r1 = np.reciprocal(x)
r2 = 1/x
assert np.array_equal(r1, r2)
print("Reciprocal for all elements of the said array:")
print(r1)


# In[1]:


# lambda function
#profit and loss
print("Enter buying price and sellng price")
buyp=float(input())
sellp=float(input())
loss=lambda bp,sp: bp-sp
print("Loss is",loss(buyp,sellp))
profit=lambda bp,sp: sp-bp
print("Profit  is",profit(buyp,sellp))

#simple intrest
p=float(input("Simple Intrest \n enter principal"))
r=float(input("Enter rate"))
t=float(input("Enter time"))

si= lambda p,r,t: (p*r*t)/100
print("Simple Intrest ",si(p,r,t))

#compound intrest
p=float(input("Compound Intrest \n enter principal"))
r=(float(input("Enter annual intrest rate (in percent)")))/100
t=float(input("Enter time"))
n=float(input("Number of times intrest is computed"))

pri= lambda p,r,t,n: p*pow((1+(r/n)),n*t)
print("Final Amount :", pri(p,r,t,n))


# In[8]:


import numpy as np
detail=[[1,10000,30,15],[2,5000,38,10],[3,9800,42,12],[4,5600,35,5]]
det=np.array(detail)
print(det)


# In[9]:


age=det[ : ,2]
print(age)
young= age.min()
for i in range(len(age)) :
    if (det[i,2] == young) :
        print("youngest employee",i+1)


# In[10]:


exp=det[ : ,3]
highexp=exp.max()
for i in range(4) :
    if (det[i,3] == highexp) :
        print("Most experienced",i+1)


# In[11]:


val=0
c=0
for i in range(4):
    if(det[i,2]>=30 and det[i,2]<=40):
        val=val +det[i,1]
        c=c+1
print(val/c)


# In[12]:


f=0
info= input("enter the salary")
info= int(info)
for i in range(3):
    if(info == det[i,1]):
        print("reg no", det[i,0],"\n age: ", det[i,2], "\n experience in years : ",det[i,3] )
        f=f+1
if(f==0):
    print("no such entry exists")


# In[ ]:




