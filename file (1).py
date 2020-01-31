#!/usr/bin/env python
# coding: utf-8

# In[4]:


mydict={1:"datascience",2:"datamining",3:"databank",4:"dataglove",5:"40atalink$",6:"data-driven",7:"data",8:"database",9:"beautiful",10:"wonderful",11:"overfull",12:"chock-full",13:"overfull",14:"full",15:"topfull",16:"brimfull",
        17:"adored",18:"Alfred",19:"Alreds@",20:"ancred",21:"aredes",22:"avered",23:"abjoint",24:"abjointed",25:"abjointing",26:"abjoints",27:"absinth",28:"absinthe",29:"absinthes",30:"barred",31:"beared",32:"beered",33:"birred",34:"blared",35:"bredda",
        36:"discriminating",37:"disapproving@",38:"insomnia",39:"omnivore",40:"apple",41:"orange",42:"icecream",43:"bat",44:"cat",45:"dog",46:"bournvita",47:"basketball",48:"concentration",49:"computer",50:"diminishing",51:"integer",52:"costly",53:"daily",
        54:"orange", 55:"one", 56:"Ate", 57:"ace", 58:"ice",59:"vowel",60:"semivowel", 61:"breded",62:"mission",63:"misconstruction",64:"misconception",65:"misinformation",66:"misrepresentation", 67:"misinterpretation15",68:"misperception",69:"misappropriation",
        70:"disgusting",71:"disturbing",72:"disappointing",}


# In[13]:


f=open("mydict.txt","w")
f.write(str(mydict))
f.close()


# In[35]:


import re
f=open("mydict.txt","r")
l1 = f.read()
print(type(l1))
f.close()
import ast
d1 = ast.literal_eval(l1)
print(type(d1))
#print(d1)
for x in d1.values():
    if(re.findall("^data",x)):
        print(x)


# In[38]:


import re
f=open("mydict.txt","r")
l1 = f.read()
print(type(l1))
f.close()
import ast
d1 = ast.literal_eval(l1)
print(type(d1))
#print(d1)
for x in d1.values():
    if(re.findall("ful$",x)):
        print(x)


# In[51]:


import re
f=open("mydict.txt","r")
l1 = f.read()
print(type(l1))
f.close()
import ast
d1 = ast.literal_eval(l1)
print(type(d1))
#print(d1)
for x in d1.values():
    if(re.findall("red",x)):
        print(x)


# In[45]:


import re
f=open("mydict.txt","r")
l1 = f.read()
print(type(l1))
f.close()
import ast
d1 = ast.literal_eval(l1)
print(type(d1))
#print(d1)
for x in d1.values():
    if(re.findall("^mis.*ion$",x)):
        print(x)


# In[49]:


import re
f=open("mydict.txt","r")
l1 = f.read()
print(type(l1))
f.close()
import ast
d1 = ast.literal_eval(l1)
print(type(d1))
#print(d1)
for x in d1.values():
    if(re.findall("omni",x)):
        print(x)


# In[57]:


import re
f=open("mydict.txt","r")
l1 = f.read()
print(type(l1))
f.close()
import ast
d1 = ast.literal_eval(l1)
print(type(d1))
#print(d1)
for x in d1.values():
    if(re.findall("^a",x)):
        print(x)


# In[ ]:




