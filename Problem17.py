#!/usr/bin/env python
# coding: utf-8

# In[54]:


x1 = ["","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
x10 = ["", "ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]

answer = 0
for i in range(1,20):
    answer += len(x1[i])
    
    #print(str(i) + " -> " + x1[i])

for i in range(20,100):
    tmp1 = int(i/10)
    answer += len(x10[tmp1])
    tmp2 = int(i%10)
    answer += len(x1[tmp2])
    
    #print(str(i) + " -> " + x10[tmp1] + " " + x1[tmp2])


for i in range(100,1000):
    tmp1 = int(i/100)
    answer += len(x1[tmp1])
    answer += len("hundred")
    a = x1[tmp1] + " hundred"
    tmp2 = int(i%100)
    if tmp2 > 0:
        answer += len("and")
        a += " and "
        if tmp2 < 20:
            answer += len(x1[tmp2])
            a += x1[tmp2]
        else:
            tmp3 = int(tmp2/10)
            answer += len(x10[tmp3])
            tmp4 = int(tmp2%10)
            answer += len(x1[tmp4])  
            a += x10[tmp3] + " " + x1[tmp4]
            
    #print(str(i) + " -> " + a)
       
answer += len("onethousand")
print(answer)


# In[ ]:




