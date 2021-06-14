#!/usr/bin/env python
# coding: utf-8

# In[1]:


cardValue = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10,'J':11,'Q':12,'K':13,'A':14}


# In[74]:


def getHighestCardValue(cards):
    cards = sorted(cards, key=lambda card: cardValue[card[0]])
    return cardValue[cards[-1][0]]


# In[86]:


def maxOfAKind(cards):
    maxOfAKind = []
    counter = 1
    cards = sorted(cards, key=lambda card: cardValue[card[0]])
    for i in range(1,5):
        if int(cardValue[cards[i][0]]) == int(cardValue[cards[i-1][0]]): counter += 1
        else: 
            maxOfAKind.append((counter, int(cardValue[cards[i-1][0]])))
            counter = 1
    maxOfAKind.append((counter, int(cardValue[cards[4][0]])))
    maxOfAKind = sorted(maxOfAKind)
    return maxOfAKind[-1], maxOfAKind[-2]


# In[87]:


def onePair(cards):
    max1, max2 = maxOfAKind(cards)
    if max1[0] == 2 and max2[0] == 1: return True, max1, max2
    return False, max1, max2


# In[88]:


def twoPairs(cards):
    max1, max2 = maxOfAKind(cards)
    if max1[0] == 2 and max2[0] == 2: return True, max1, max2
    return False, max1, max2


# In[89]:


def threeOfAKind(cards):
    max1, max2 = maxOfAKind(cards)
    if max1[0] == 3: return True, max1, max2
    return False, max1, max2


# In[90]:


def straight(cards):
    cards = sorted(cards, key=lambda card: cardValue[card[0]])
    for i in range(1,5):
        if int(cardValue[cards[i][0]]) != int(cardValue[cards[i-1][0]]) + 1: return False
    return True


# In[91]:


def flush(cards):
    for i in range(1,5): 
        if cards[i][1] != cards[i-1][1]: return False
    return True


# In[92]:


def fullHouse(cards):
    max1, max2 = maxOfAKind(cards)
    if max1[0] == 3 and max2[0] == 2: return True, max1, max2
    return False, max1, max2


# In[93]:


def fourOfAKind(cards):
    max1, max2 = maxOfAKind(cards)
    if max1[0] == 4: return True, max1, max2
    return False, max1, max2


# In[94]:


def straightFlush(cards):
    if flush(cards) and straight(cards): return True
    return False


# In[95]:


def getHandValue(cards):
    if straightFlush(cards): 
        return 9_000_000 + getHighestCardValue(cards)
    isFourOfAKind, max1, _ = fourOfAKind(cards)
    if isFourOfAKind: 
        return 8_000_000 + max1[1]
    isFullHouse, max1, max2 = fullHouse(cards)
    if isFullHouse: 
        return 7_000_000 + max1[1]*100 + max2[1]
    if flush(cards): 
        return 6_000_000 + getHighestCardValue(cards)
    if straight(cards): 
        return 5_000_000 + getHighestCardValue(cards)
    isThreeOfAKind, max1, max2 = threeOfAKind(cards)
    if isThreeOfAKind: 
        return 4_000_000 + max1[1]*100 + max2[1]
    isTwoPairs, max1, max2 = twoPairs(cards)
    if isTwoPairs: 
        return 3_000_000 + max1[1]*100 + max2[1]
    isOnePair, max1, max2 = onePair(cards)
    if isOnePair: 
        return 2_000_000 + max1[1]*100 + max2[1]
    return 1_000_000 + getHighestCardValue(cards)


# In[97]:


player1Wins = 0
with open("p054_poker.txt", "r") as f:
    lineCounter = 0
    for line in f:
        hand1 = line[:14].split()
        hand2 = line[15:29].split()
        
        hand1Value = getHandValue(hand1)
        hand2Value = getHandValue(hand2)
        
        winner = 0
        if hand1Value > hand2Value:
            winner = 1
        elif hand1Value < hand2Value:
            winner = 2
        else:
            hand1 = sorted(hand1, key=lambda card: cardValue[card[0]])
            hand2 = sorted(hand2, key=lambda card: cardValue[card[0]])
            for i in range(5):
                hand1Value = getHighestCardValue(hand1[:4-i])
                hand2Value = getHighestCardValue(hand2[:4-i])
                if hand1Value != hand2Value:
                    if hand1Value > hand2Value:
                        winner = 1
                    elif hand1Value < hand2Value:
                        winner = 2
                    break
        
        print("{}vs{} -> Player {} wins: {} vs {}".format(sorted(hand1, key=lambda card: cardValue[card[0]]),
                                                sorted(hand2, key=lambda card: cardValue[card[0]]), winner,
                                                hand1Value, hand2Value))
        
        if winner == 1:
            player1Wins += 1
        lineCounter += 1
print(player1Wins)


# In[ ]:





# In[ ]:




