#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Precompute a lot of cubes and check if they have the same number of digits and the same digits


# In[21]:


digitsDict = {}
for n in range(345,10000):
    cube = n*n*n
    digitsCount = [0,0,0,0,0,0,0,0,0,0,0]
    for c in str(cube):
        digitsCount[int(c)] += 1
    h = "".join([str(x) for x in digitsCount])
    if h in digitsDict:
        digitsDict[h][0] += 1
    else:
        digitsDict[h] = [1, cube]
        
    if digitsDict[h][0] == 5:
        print(digitsDict[h][1])
        break


# In[ ]:




