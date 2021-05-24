#!/usr/bin/env python
# coding: utf-8

# In[1]:


1/7


# In[4]:


d = int(10/7)
r = 10%7
for i in range(20):
    print(d,end="")
    d = int(r*10/7)
    r = (r*10)%7


# In[27]:


maxCounter = 0
answer = 0
for d in range(2,1000):
    multiplier = 10 ** len(str(d))
    divisor = int(multiplier/d)
    rest = multiplier%d
    drSet = {(divisor,rest)}
    #print(str(d) + " -> ",end="")
    counter = 0
    while True:
        #print(divisor,end="")
        divisor = int(rest*10/d)
        rest = (rest*10)%d
        if (divisor,rest) in drSet:
            break
        drSet.add((divisor,rest))
        counter += 1
        if counter > maxCounter:
            maxCounter = counter
            answer = d
    #print()
print(maxCounter)
print(answer)


# In[26]:


1/983


# In[28]:


d = int(1000/answer)
r = 1000%answer
for i in range(1000):
    print(d,end="")
    d = int(r*10/answer)
    r = (r*10)%answer


# In[ ]:




