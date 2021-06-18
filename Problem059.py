#!/usr/bin/env python
# coding: utf-8

# In[140]:


with open("p059_cipher.txt ", "r") as f:
    asciiValues = [int(x) for x in f.readline().split(",")]


# In[ ]:


bestCount = 0
bestKey = ""
bestText = ""
for k1 in range(ord('a'),ord('z')+1):
    for k2 in range(ord('a'),ord('z')+1):
        for k3 in range(ord('a'),ord('z')+1):
            
            tmpKey = str(chr(k1)) + str(chr(k2)) + str(chr(k3))
            largeTmpKey = tmpKey*485
            
            generatedText = ""
            for i in range(len(asciiValues)):
                generatedText += str(chr(asciiValues[i]^ord(largeTmpKey[i])))
            
            count = generatedText.count(" and")
            if count > bestCount:
                bestCount = count
                bestKey = tmpKey
                bestText = generatedText


print("Key: " + bestKey)
print("Decrypted text: " + bestText)
answer = 0
for c in bestText: answer += ord(c)
print(answer)


# In[ ]:





# In[ ]:




