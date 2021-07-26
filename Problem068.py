#!/usr/bin/env python
# coding: utf-8

# In[1]:


from itertools import permutations


# In[2]:


solutions16 = []
for p in permutations(range(1,11)):
    sum1 = p[0] + p[1] + p[2]
    sum2 = p[3] + p[2] + p[4]
    sum3 = p[5] + p[4] + p[6]
    sum4 = p[7] + p[6] + p[8]
    sum5 = p[9] + p[8] + p[1]
    if sum1 == sum2 and sum2 == sum3 and sum3 == sum4 and sum4 == sum5:
        str1 = str(p[0]) + str(p[1]) + str(p[2])
        str2 = str(p[3]) + str(p[2]) + str(p[4])
        str3 = str(p[5]) + str(p[4]) + str(p[6])
        str4 = str(p[7]) + str(p[6]) + str(p[8])
        str5 = str(p[9]) + str(p[8]) + str(p[1])

        if p[0] < p[3] and p[0] < p[5] and p[0] < p[7] and p[0] < p[9]: solution = str1 + str2 + str3 + str4 + str5
        if p[3] < p[3] and p[3] < p[0] and p[3] < p[7] and p[3] < p[9]: solution = str2 + str3 + str4 + str5 + str1
        if p[5] < p[3] and p[5] < p[5] and p[0] < p[7] and p[5] < p[9]: solution = str3 + str4 + str5 + str1 + str2
        if p[7] < p[3] and p[7] < p[5] and p[7] < p[0] and p[7] < p[9]: solution = str4 + str5 + str1 + str2 + str3
        if p[9] < p[3] and p[9] < p[5] and p[9] < p[7] and p[9] < p[0]: solution = str5 + str1 + str2 + str3 + str4

        if len(solution) == 16: solutions16.append(solution)
        
solutions16.sort(reverse=True)
print(solutions16[0])


# In[ ]:




