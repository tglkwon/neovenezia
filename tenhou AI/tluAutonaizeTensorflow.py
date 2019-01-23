#!/usr/bin/env python
# coding: utf-8

# In[1]:


f = open("""./kakan_ton1_1.txt""", 'r', encoding='UTF8')
print(f.read())


# In[14]:


from bs4 import BeautifulSoup
import re

f = open("""./kakan_ton1_1.txt""", 'r', encoding='UTF8')
fTxt = f.read()

#1KyokuSpliter
KyokuSplit = fTxt.split('='*40)
kyoku = 1
KyokuSSplit = KyokuSplit[kyoku].split('\n')
nPlayer = 0

#DoraIndicator[] = 

#N번 플레이어 버림패
def PlayerKawa(nPlayer):
    Kawa = []
    for line in KyokuSSplit:
        if 'Player ' + str(nPlayer) + ": Discard " in line:
            Kawa.append(line[18:-2])
    return Kawa

#N번 플레이어 배패
KyokuAllHais = KyokuSplit[kyoku].split('Initial Hands:')
InitialHands = KyokuAllHais[1].split('\n')
nPlayerInitialHands = re.findall(r"[^A-Za-z0-9: ]+", InitialHands[nPlayer+1])
Haibo = [line for line in KyokuSSplit if 'Player' in line]

#N번 플레이어 쯔모패
def PlayerTsumo(nPlayer):
    Tsumo = []
    for idx, line in enumerate(Haibo):
        if 'Player '+ str(nPlayer) +': Draw ' in line:
            Tsumo.append(line[-3])
        elif 'Player '+ str(nPlayer) +': Chi ' in line:
            Tsumo.append(Haibo[idx-1][-3])    
        elif 'Player '+ str(nPlayer) +': Pon ' in line:
            Tsumo.append(Haibo[idx-1][-3])
        elif 'Player '+ str(nPlayer) +': KaKan ' in line:
            #Tsumo.remove(Haibo[idx-1][-3])
            pass
        elif 'Player '+ str(nPlayer) +': AnKan ' in line:
            pass
        elif 'Player '+ str(nPlayer) +': MinKan ' in line:
            pass
            
    return Tsumo

'''#N번 플레이어 받은패
def PlayerNaki(nPlayer):
    Naki = {}
    for line in Haibo:
        if 'Player '+ str(nPlayer) +': Draw ' in line:
            #Naki[].append(line[-3])
        elif 'Player '+ str(nPlayer) +': Pon ' in line:
            #Draw.append(line[29:30])
        elif 'Player '+ str(nPlayer) +': Chi ' in line:
            #Draw.append(line[29:30])
        elif 'Player '+ str(nPlayer) +': Kan ' in line:
            #Draw.append(line[29:30])
            
    return Naki'''

#N번 플레이어 n순 손패
def Hands(nTurn):
    nPlayerHands = nPlayerInitialHands
    #Nsun n 순
    TotalTurn = len(PlayerKawa(nPlayer))
    for nTurn in range(TotalTurn):
        nPlayerHands.append(PlayerTsumo(nPlayer)[nTurn])
        nPlayerHands.remove(PlayerKawa(nPlayer)[nTurn])
        nPlayerHands.sort()

print(nPlayerHands)

#마작 버림패 최대 수 24매


# In[ ]:




