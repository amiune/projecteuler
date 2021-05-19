#!/usr/bin/env python
# coding: utf-8

# In[2]:


sum_squares = 0
for i in range(1,101):
    sum_squares += i*i

square_sum = 0
for i in range(1,101):
    square_sum += i
square_sum = square_sum * square_sum

diff = square_sum - sum_squares

print(diff)


# In[ ]:




