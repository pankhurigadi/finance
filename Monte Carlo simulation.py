
#Run Monte carlo simulations in Python using this template to approximate the daily future prices of a stock.

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
data[ticker]=wb.DataReader(ticker,data_source='yahoo',start='2010-1-1')['Adj Close']

log_returns=np.log(1+data.pct_change()) #obtain simple logarithmic returns
log_returns.tail()


#plot of stock price
data.plot(figsize=(10,6));

#plot of log returns. Graph indicates a normal distribution of returns with stable mean
log_returns.plot(figsize=(10,6));

#calculate mean and variance of returns
u=log_returns.mean()
u

var=log_returns.var()
var

#calculate drift and stdev to be used in Brownian motion formula to approximate future returns
drift=u-(0.5*var)
drift

stdev=log_returns.std()
stdev

#check types for drift and stdev
type(drift)
type(stdev)

#convert the values for drift and stdev into numpy arrays. Obtain same result by adding '.values'
np.array(drift)
stdev.values

#create a variable that corresponds to difference between mean and events (standard deviation)
norm.ppf(0.95)  #event has 95% chance of occuring, distance = 1.65 standard deviations

#create a random variable 'x'
x=np.random.rand(10,2) #2 arguments for a multi-dimensional array (10x2 matrix)
x

#include 'x' in ppf distribution to obtain distance from mean corresponding to each of these randomly generated probabilities.
norm.ppf(x)

#use the randomly generated probabilities from x to calculate distances from mean zero
z=norm.ppf(np.random.rand(10,2))
z

#specify time intervals
t_intervals=1000 #forecasting stock price for upcoming 1000 days
iterations=10 #produce 10 series of future stock price predictions

#dailyreturns=e^r
#r=drift + stdev*z
#Use the two formulas above to calculate daily returns array.
dailyreturns=np.exp(drift.values + stdev.values*norm.ppf(np.random.rand(t_intervals,iterations)))
dailyreturns
#This generates a 100x10 array of random future stock prices.


#create price list: price(t) = price(0)*simulated daily return(t)
#Then, price(t+1)=price(t)*simulated daily return (t+1)
#Use first stock price equal to last price in our dataset, reflects current market price. Let this be S0
S0=data.iloc[-1] #last value in the table.
S0

price_list=np.zeros_like(dailyreturns) #create array with same dimensions as dailyreturns array, and fill with zeros.
price_list

#Replace zeros with expected stock prices using a loop
price_list[0]=S0 #set first row of prices equal to current market price
price_list 

#Set up a loop starting at day1 & ending at day1000
for t in range(1,t_intervals):
    price_list[t]=price_list[t-1]*dailyreturns[t]
    
price_list

plt.figure(figsize=(10,6))
plt.plot(price_list);
#This generates a graph of 10 possible stock price paths of expected stock price of Netflix.




