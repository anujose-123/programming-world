#!/usr/bin/env python
# coding: utf-8

# In[2]:


mylist=["lion","tiger","rat","ant"]
print(mylist)
        


# In[3]:


mylist.append("elephant")
print(mylist)


# In[5]:


mylist.clear()
print(mylist)


# In[11]:


mylist=["apple","orange","banana"]
list=mylist.copy()
print(list)


# In[13]:


print(len(mylist))


# In[17]:


names=["anu","anju","ann"]
job=["doctor","teacher","minister"]
names.extend(job)
print(names)


# In[14]:


mylist.insert(1,"grapes")
print(mylist)


# In[18]:


names.pop()
print(names)


# In[19]:


names.pop(2)
print(names)


# In[20]:


names.remove("teacher")
print(names)


# In[21]:


names.reverse()
print(names)


# In[26]:


mylist.sort()
print(mylist)


# In[50]:


list1=[2,30,4]
list2=[20,5,10]
list3.append(list1+list2)
print(list3)


# In[28]:


mytuple=("apple","banana","orange")
print(mytuple)


# In[29]:


print(len(mytuple))


# In[30]:


thistuple=tuple(("ann","anu","anju"))
print(thistuple)


# In[40]:


s1=(5,10,8)
print(max(s1))
print(min(s1))


# In[39]:


A=(5,7)
B=(8,4)
if A>B:print("A is bigger than B")
else:print("B is bigger")


# In[46]:


c=("doctor","patient","attender")
(d,p,attender)=c
print(d)
print(p)


# In[ ]:




