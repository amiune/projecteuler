#!/usr/bin/env python
# coding: utf-8

# In[19]:


from itertools import permutations

numbers = [1,2,3,4,5,6,7,8,9]

solutions = set()
for p in permutations(numbers):
    
    m1 = p[0]
    m2 = 1000*p[1] + 100*p[2] + 10*p[3] + p[4]
    m3 = 1000*p[5] + 100*p[6] + 10*p[7] + p[8]
    
    if m1 * m2 == m3:
        print(str(m1) + " * " + str(m2) + " = " + str(m3) )
        solutions.add(m3)
    
    m1 = 10*p[0] + p[1]
    m2 = 100*p[2] + 10*p[3] + p[4]
    m3 = 1000*p[5] + 100*p[6] + 10*p[7] + p[8]
    
    if m1 * m2 == m3:
        print(str(m1) + " * " + str(m2) + " = " + str(m3) )
        solutions.add(m3)
    
answer = 0
for i in solutions:
    answer += i
print(answer)


# In[ ]:




