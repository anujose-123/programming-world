#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#loading data sets
data=pd.read_csv("C:/Users/christ/Desktop/data.csv")
data
df1=pd.DataFrame(data)
print(df1)


# In[2]:


df1.head()


# In[3]:


df1.describe()


# In[4]:


df1.info()


# In[5]:


df1.drop(['id'], axis = 1).hist(figsize = (14,14))
plt.show()


# In[23]:


import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')
import statsmodels.api as sm
import seaborn as sns

plt.figure(figsize = (12,10))
sns.heatmap(df1.corr())
plt.show()
df1.corr()


# In[9]:


#In the data set the concavity is a bulge (a rounded swelling or protuberance that distorts,
#a flat surface - synonyms: swelling, bump, lump, protuberance) in the cell.


# In[10]:


df2 = df1[['radius_mean','perimeter_mean','area_mean','concavity_mean',
         'concave points_mean','radius_worst','perimeter_worst','area_worst',
         'concave points_worst']]


# In[11]:


a = pd.plotting.scatter_matrix(df2, figsize = (15, 10))
plt.xticks(rotation = 45)
plt.yticks(rotation = 45)
plt.show()


# In[24]:


df1.area_mean.plot(kind="line",color="g",label = 'area_mean',linewidth=1,alpha = 0.5,grid = True,linestyle = ':',figsize=(10,10))
plt.xlabel('x axis')              # label = name of label
plt.ylabel('y axis')
plt.legend(loc="upper right")
plt.title('Line Plot')            # title = title of plot
plt.show()


# In[25]:


#area mean vs compactness_mean for first 10 items
plt.subplots(figsize=(8,8))
plt.plot(df1["area_mean"][0:10],data["compactness_mean"][0:10],color="lime",alpha = 0.5, linestyle = ':')
plt.xlabel("area_mean")
plt.ylabel("compactness_mean")
plt.title("compactness_mean vs area_mean report")
plt.show()


# In[26]:


#texture_mean area_mean Scatter Plot
plt.subplots(figsize=(8,8))
plt.scatter(df1.area_mean,data.texture_mean,color="g",alpha=0.5)
plt.xlabel("area_mean")
plt.ylabel("texture_mean")
plt.title('texture_mean area_mean Scatter Plot')
plt.grid()


# In[27]:


# smoothness_mean compactness_mean Scatter Plot
plt.subplots(figsize=(8,8))
plt.scatter(df1.smoothness_mean,data.compactness_mean,color="r",alpha=0.5)
plt.xlabel("smoothness_mean")
plt.ylabel("compactness_mean")
plt.title('smoothness_mean compactness_mean Scatter Plot')
plt.grid()


# In[28]:


#compare area mean by diagnosis
df1.boxplot(column="area_mean",by="diagnosis")
plt.show()


# In[29]:


#texture mean and area mean
g = sns.jointplot(df1.texture_mean, data.area_mean, kind="kde", size=7)
plt.savefig('graph.png')
plt.show()


# In[ ]:




