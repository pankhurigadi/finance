#!/usr/bin/env python
# coding: utf-8

# In[11]:


import datetime as dt
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')
start=dt.datetime(2010,11,21)
end=dt.datetime(2020,11,21)

df=web.DataReader('TSLA','yahoo',start,end)
print(df.head())


# In[17]:


df['100ma']=df['Adj Close'].rolling(window=100,min_periods=0).mean()   #rolling method operated to average price column with window of 100
print(df.head())



# In[13]:


plt.figure(figsize=[15,10])
plt.grid(True)
plt.plot(df['Adj Close'])
plt.plot(df['100ma'])


# In[ ]:




