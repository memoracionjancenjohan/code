#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


s = pd.Series([3, -5, 7, 4], index=['a', 'b', 'c', 'd'])
s


# In[5]:


data = {'Country': ['Belgium', 'India', 'Brazil'],
       'Capital': ['Brussels', 'New Delhi', 'Brasilia'],
       'Population': [11190846, 1303171035, 207847528]}

df = pd.DataFrame(data, columns=['Country', 'Capital', 'Population'])
df


# In[6]:


Global_PS4_sales = pd.Series([10.0, 30.2, 35.9, 73.6, 91.6, 94.7], index=[2014, 2015, 2016, 2017, 2018, 2019])
Global_PS4_sales


# In[7]:


data = {'Character': ['Killua', 'Kurapika', 'Gon', 'Chrollo', 'Hisoka'],
       'Nen': ['Kanmuru', 'Jail Chain', 'Jajanken', 'Bandit Secret', 'Bungee Gum'],
       'Nen Type': ['Transmuter', 'Conjurer', 'Enhancer', 'Specialist', 'Transmuter'],
       'Votes': [7488, 7000, 2472, 1904, 1144]}

HxH_Popularity_Poll = pd.DataFrame(data, columns=['Character', 'Nen', 'Nen Type', 'Votes'])

HxH_Popularity_Poll


# In[8]:


HxH_Popularity_Poll.to_csv('MyDataframe.csv')


# In[9]:


aqd = pd.read_csv('aqd.csv')
aqd


# In[14]:


aqd.head() #If left blank, only counts the first 5 rows


# In[15]:


aqd.tail()#If left blank, only counts the last 5 rows


# **Python Demo 2**

# Subsetting -> certain element (1)

# In[16]:


s = Global_PS4_sales
s


# In[17]:


df = HxH_Popularity_Poll
df


# In[18]:


s[2016]


# In[20]:


# iloc - m row, n column indexes
df.iloc[[3],[2]]


# In[22]:


# loc - m row index, column name
df.loc[[2], ['Nen']]


# Slicing -> getting a portion

# In[23]:


s


# In[27]:


s[3:6]


# In[25]:


df


# In[28]:


df[2:3]


# In[29]:


df.loc[:,['Nen Type']]


# In[30]:


df.loc[[0,1], ['Character', 'Votes']]


# Indexing -> with given conditions

# In[31]:


s


# In[32]:


s[s>30]


# In[ ]:


df


# In[33]:


df.loc[(df['Votes']>1000)&(df['Votes']<5000)]


# In[34]:


df.loc[df['Nen Type']=='Transmuter']


# In[35]:


df.loc[(df['Nen']=='Kanmuru'), ['Character']]


# In[36]:


df.loc[df['Nen Type']=='Transmuter', ['Character', 'Nen', 'Votes']]

