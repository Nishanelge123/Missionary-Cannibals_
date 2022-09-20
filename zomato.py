#!/usr/bin/env python
# coding: utf-8

# In[ ]:


if 'bar' in {'foo':1,'bar':2,'baz':3}:
    print(1,end=' ')
    print(2,end=' ')
    if 'a' in 'qux':
        print(3,end=" ")
print(4,end='')


# In[ ]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as pl

df=pd.read_csv("C:\\Users\\DELL\\Downloads\\archive\\zomato.csv")


# In[ ]:


df.head()


# In[ ]:


df.info()


# In[ ]:


# df.drop(['phone','dish_liked','menu_item','url'],axis=1,inplace=True)
# df


# In[ ]:


df.isnull().sum()


# In[ ]:


df.drop(['phone','dish_liked','menu_item','url'],axis=1,inplace=True)
df.head()


# In[ ]:


df.rename(columns = {'approx_cost(for two people)':'approx_cost','listed_in(type)':'listed_type','listed_in(city)':'listed_city'}, inplace = True)


# In[ ]:


df.columns


# In[ ]:


df.dropna(inplace = True)


# In[ ]:


df1 = df.dropna(axis=1,how='all')
df1.head()


# In[ ]:


df1['name'].unique()


# In[ ]:


df1["rate"].unique()


# In[ ]:


def rate(val):
    if val == "NEW" or val == "-":
        return np.nan
    else:
        val = str(val).split("/")
        val = val[0]
        return float (val) 
df1["rate"] = df1["rate"].apply(rate)
df1["rate"].head(5)


# In[ ]:


df1["approx_cost"].unique()


# In[ ]:


def approx_cost(val):
    val = str(val)
    if "," in val:
        val = val.replace(",","")
        return float(val)
    else:
        return float(val)
df1["approx_cost"] = df1["approx_cost"].apply(approx_cost)
df1["approx_cost"].head()


# In[ ]:


df1['name'].unique()


# In[ ]:


def name(val):
    if "-" in val:
        val=val.replace("-","")
        return val
    else:
        return val
df1["name"] = df1["name"].apply(name)
df1["name"].unique()


# In[ ]:


df1["name"].str.replace('-|New','')


# In[ ]:


df1['online_order'].unique()


# In[ ]:


sns.countplot(x='online_order',data=df1)


# In[ ]:


import matplotlib.pyplot as plt
plt.figure(figsize=(10,5))
sns.countplot(x='book_table',data=df1)
plt.show()


# In[ ]:


# sns.barplot(x='', y='rate', data=tips, estimator=np.std)
df1.groupby('book_table')[['rate']].mean()


# In[ ]:


# df1.groupby('book_table')['rate']
sns.barplot(x = 'name', y = 'rate',data = df1)
plt.show()


# In[ ]:




