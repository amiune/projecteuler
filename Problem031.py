#!/usr/bin/env python
# coding: utf-8

# In[42]:


def countCoins(coins, m, n):
    #if n== 0 there is a solution
    if (n == 0): return 1
    #if n < 0 ther is no solution
    if (n < 0): return 0
    #if n > 0 and m <= 0 there is no solution with these coins
    if (m <=0 and n > 0): return 0
    #count including coins[m-1] + excluding coins[m-1]
    ret = countCoins(coins, m, n-coins[m-1]) + countCoins(coins, m-1, n)
    return ret

coins = [1,2,5,10,20,50,100,200]
m = len(coins)
N = 200
countCoins(coins,m,N)


# In[ ]:




