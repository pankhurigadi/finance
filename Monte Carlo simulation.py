#!/usr/bin/env python
# coding: utf-8

# In[12]:


#Run a Monte Carlo simulation in Python to approximate the daily stock price of Netflix (ticker="NFLX")


#import relevant libraries
import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
from scipy.stats import norm
get_ipython().run_line_magic('matplotlib', 'inline')

#forecast netflix's future stock price
ticker= "NFLX"
data=pd.DataFrame()
data[ticker]=wb.DataReader(ticker,data_source='yahoo',start='2010-1-1')['Adj Close']#estimating

log_returns=np.log(1+data.pct_change()) #obtain simple logarithmic returns
log_returns.tail()


#plot of stock price
data.plot(figsize=(10,6));

#plot of log returns. Graph indicates a normal distribution of returns with stable mean
log_returns.plot(figsize=(10,6));


# In[16]:


#calculate mean and variance of returns
u=log_returns.mean()
u


# In[17]:


var=log_returns.var()
var


# In[19]:


#calculate drift and stdev to be used in Brownian motion formula to approximate future returns
drift=u-(0.5*var)
drift


# In[20]:


stdev=log_returns.std()
stdev


# In[21]:


#check types for drift and stdev
type(drift)


# In[22]:


type(stdev)


# In[23]:


#convert the values for drift and stdev into numpy arrays. Obtain same result by adding '.values'
np.array(drift)


# In[24]:


stdev.values


# In[25]:


norm.ppf(0.95)#create a variable that corresponds to difference between mean and events (standard deviation)
#event has 95% chance of occuring, distance = 1.65 standard deviations


# In[26]:


#create a random variable 'x'
x=np.random.rand(10,2) #2 arguments for a multi-dimensional array (10x2 matrix)
x


# In[27]:


#include 'x' in ppf matrix to obtain distance from mean corresponding to each of these randomly generated probabilities.
norm.ppf(x)


# In[28]:


z=norm.ppf(np.random.rand(10,2))
z
#used the randomly generated probabilities from x to calculate distances from mean zero


# In[29]:


#specify time intervals
t_intervals=1000 #forecasting stock price for upcoming 1000 days
iterations=10 #produce 10 series of future stock price predictions

#dailyreturns=e^r
#r=drift + stdev*z


dailyreturns=np.exp(drift.values + stdev.values*norm.ppf(np.random.rand(t_intervals,iterations)))
dailyreturns

#This generates a 100x10 array of random future stock prices.


# In[30]:


#create price list: price(t) = price(0)*simulated daily return(t)
#Then, price(t+1)=price(t)*simulated daily return (t+1)


#Use first stock price equal to last price in our dataset, reflects current market price. Let this be S0
S0=data.iloc[-1] #last value in the table.
S0


# In[31]:


price_list=np.zeros_like(dailyreturns) #create array with same dimensions as dailyreturns array, and fill with zeros.
price_list


# In[32]:


#Replace zeros with expected stock prices using a loop
price_list[0]=S0 #set first row of prices equal to current market price
price_list 


# In[33]:


#Set up a loop starting at day1 & ending at day1000
for t in range(1,t_intervals):
    price_list[t]=price_list[t-1]*dailyreturns[t]
    
price_list


# In[35]:


plt.figure(figsize=(10,6))
plt.plot(price_list);
#This generates a graph of 10 possible stock price paths of expected stock price of Netflix.




# In[ ]:




