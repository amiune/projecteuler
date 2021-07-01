#!/usr/bin/env python
# coding: utf-8

# In[142]:


p3All,p4All,p5All,p6All,p7All,p8All = [],[],[],[],[],[]
for n in range(200):
    p3Tmp = n*(n+1)/2
    if p3Tmp >= 1000 and p3Tmp <= 9999: p3All.append((str(int(p3Tmp)),3))
    p4Tmp = n*n
    if p4Tmp >= 1000 and p4Tmp <= 9999: p4All.append((str(int(p4Tmp)),4))
    p5Tmp = n*(3*n-1)/2
    if p5Tmp >= 1000 and p5Tmp <= 9999: p5All.append((str(int(p5Tmp)),5))
    p6Tmp = n*(2*n-1)
    if p6Tmp >= 1000 and p6Tmp <= 9999: p6All.append((str(int(p6Tmp)),6))
    p7Tmp = n*(5*n-3)/2
    if p7Tmp >= 1000 and p7Tmp <= 9999: p7All.append((str(int(p7Tmp)),7))
    p8Tmp = n*(3*n-2)
    if p8Tmp >= 1000 and p8Tmp <= 9999: p8All.append((str(int(p8Tmp)),8))
        
pAll = p3All.copy()
pAll.extend(p4All)
pAll.extend(p5All)
pAll.extend(p6All)
pAll.extend(p7All)
pAll.extend(p8All)


# In[143]:


len(pAll)


# In[144]:


s1, s2 = set(),set()
for p in pAll:
    s1.add(p[0][:2])
    s2.add(p[0][2:])
s3 = s1.intersection(s2)


# In[145]:


print(len(s1))
print(len(s2))
print(len(s3))


# In[146]:


pIntersection = []
for p in pAll:
    if p[0][:2] in s3 and p[0][2:] in s3:
        pIntersection.append(p)


# In[147]:


len(pIntersection)


# In[148]:


count = [0,0,0,0,0,0,0,0,0]
penta = [[],[],[],[],[],[],[],[],[]]
for p in pIntersection:
    count[p[1]] += 1
    penta[p[1]].append(p[0])
mul = 1
for i in count:
    print(i)
    if i > 0: mul *= i
print(mul)


# In[149]:


def findPath(number, remaining, cycle):
    if len(remaining) == 0:
        if cycle[0][:2] == cycle[-1][2:]:
            print(cycle)
    for i in remaining:
        for p in penta[i]:
            if p[:2] == number[2:]:
                newcycle = cycle.copy()
                newcycle.append(p)
                newremaining = remaining.copy()
                newremaining.remove(i)
                findPath(p, newremaining, newcycle)


# In[151]:


for p in penta[3]:
    findPath(p, [4,5,6,7,8], [p])


# In[152]:


8256 + 5625 + 2512 + 1281 + 8128 + 2882


# In[ ]:




