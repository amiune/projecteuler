#!/usr/bin/env python
# coding: utf-8

# In[30]:


bestN = 0
maxPandigital = 0
for n in range(1,98765):
    concat = ""
    isPandigital = True
    for i in range(1,9):
        tmp = n * i
        concat = concat + str(tmp)
        if len(concat)>9:
            isPandigital = False
            break
        elif len(concat) == 9:
            break
    
    if len(concat) != 9:
        isPandigital = False
    
    if isPandigital:
        digits = [1,0,0,0,0,0,0,0,0,0]
        for i in range(9):
            x = int(concat[i])
            digits[x] += 1
            if digits[x] > 1:
                isPandigital = False
                break
                
    if isPandigital:
        pandigital = int(concat)
        if pandigital > maxPandigital:
            bestN = n
            maxPandigital = pandigital

print(bestN)
print(maxPandigital)


# In[ ]:




