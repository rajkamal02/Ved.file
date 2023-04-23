#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[5]:


df=pd.read_csv("D:\\LNCT MCA  2nd sem\\R programming\\adult_income.csv") #we are entr the csv file and copy the path 
df #data fream describe the file 


# In[7]:


df.info() #if we want to see the all data row and collum datatype and all data numarical and classical value


# In[8]:


df.isnull() #if we want to see the all data null value AND  data fream  


# In[10]:


df.isnull().sum() # if allover datacount the if avavible null value numbers 


# In[11]:


df.tail() #describe the lower 5 row data show


# In[12]:


df.head() #top upper valude discribe 


# In[13]:


df.describe()# if we want to see the all value data dtype and count , mean , Quantine data 


# In[14]:


df.describe().sum().sum() #all over data sum and describe 


# In[16]:


sns.lineplot(df["sex"])


# In[17]:


sns.countplot(["sex"])


# In[20]:


sns.lineplot(df["age"],df["sex"])


# In[23]:


sns.scatterplot(df["capital.loss"],df["capital.gain"])


# In[24]:


sns.lineplot(df["capital.loss"],df["capital.gain"])


# In[27]:


sns.lineplot(df["age"],df["education.num"],hue=df["income"])


# In[28]:


sns.scatterplot(df["age"],df["education.num"],hue=df["income"])


# In[30]:


sns.distplot(df["age"])


# In[36]:


sns.pairplot(df)


# In[38]:


sns.heatmap(df.isnull())


# In[ ]:




