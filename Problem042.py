#!/usr/bin/env python
# coding: utf-8

# In[30]:


def isTriangle(x):
    n = 1
    while x > n*(n+1)/2:
        n += 1
    if x == n*(n+1)/2:
        return True
    return False


# In[33]:


f = open("p042_words.txt", "r")
words = f.read().split(',')
counter = 0
for word in words:
    wordSum = 0
    for letter in word.replace('"',''):
        wordSum += ord(letter) - ord('A') + 1
    if isTriangle(wordSum):
        counter += 1
print(counter)


# In[ ]:




