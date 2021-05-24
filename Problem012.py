#!/usr/bin/env python
# coding: utf-8

# In[42]:


import math
 
def countDivisors(n) :
    cnt = 0
    for i in range(1, int(math.sqrt(n)) + 1) :
        if (n % i == 0) :
            if (n / i == i) :
                cnt = cnt + 1
            else:
                cnt = cnt + 2
    return cnt

tnumber = 1
n = 2
while countDivisors(tnumber) <= 500:
    tnumber += n
    n += 1

print(tnumber)


# In[ ]:




