from bs4 import BeautifulSoup
import re

f = open("""./KaKan_ton1.txt""", 'r', encoding='UTF8')
fTxt = f.read()

#1KyokuSpliter
KyokuSplit = fTxt.split('='*40)
#kyoku = 0 에는 metadata가 들어감
kyoku = 8
nPlayer = 1
KyokuSSplit = KyokuSplit[kyoku].split('\n')

#DoraIndicator[] =
#ReachIndicator[] =

#N번 플레이어 배패
KyokuAllHais = KyokuSplit[kyoku].split('Initial Hands:')
InitialHands = KyokuAllHais[1].split('\n')
nPlayerInitialHands = re.findall(r"[^A-Za-z0-9: ]+", InitialHands[nPlayer+1])
Haibo = [line for line in KyokuSSplit if 'Player' in line]

#N번 플레이어 버림패
def PlayerKawa(nPlayer):
    Kawa = []
    for line in Haibo:
        if 'Player ' + str(nPlayer) + ": Discard " in line:
            Kawa.append(line[-3])
    return Kawa

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
        elif 'Player '+ str(nPlayer) +': KaKan' in line:
            Tsumo.remove(Haibo[idx-1][-3])
        elif 'Player '+ str(nPlayer) +': AnKan' in line:
            Tsumo.remove(Haibo[idx-1][-3])
        elif 'Player '+ str(nPlayer) +': MinKan' in line:
            Tsumo.remove(Haibo[idx-1][-3])
            
    return Tsumo

#N번 플레이어 받은패
def PlayerNaki(nPlayer):
    Naki = {}
    for idx, line in enumerate(Haibo):
        NakiInfo = line.split(': ')
        if 'Player '+ str(nPlayer) +': Chi ' in line:
            Naki[NakiInfo[1]] = re.findall(r"[^A-Za-z0-9: ]+", NakiInfo[2])
        elif 'Player '+ str(nPlayer) +': Pon ' in line:
            Naki[NakiInfo[1]] = re.findall(r"[^A-Za-z0-9: ]+", NakiInfo[2])
        elif 'Player '+ str(nPlayer) +': KaKan' in line:
            Naki[NakiInfo[1]] = re.findall(r"[^A-Za-z0-9: ]+", NakiInfo[2])
        elif 'Player '+ str(nPlayer) +': AnKan' in line:
            Naki[NakiInfo[1]] = re.findall(r"[^A-Za-z0-9: ]+", NakiInfo[2])
        elif 'Player '+ str(nPlayer) +': MinKan' in line:
            Naki[NakiInfo[1]] = re.findall(r"[^A-Za-z0-9: ]+", NakiInfo[2])
            
    return Naki

TotalTurn = len(PlayerKawa(nPlayer))

#N번 플레이어 n순 손패
def nPlayerHands(nTurn, nPlayer):
    Hand = nPlayerInitialHands[:]
    for Turn in range(nTurn):
        Hand.append(PlayerTsumo(nPlayer)[Turn])
        print(Hand)
        print(PlayerKawa(nPlayer))
        Hand.remove(PlayerKawa(nPlayer)[Turn])

    Hands = Hand + list(PlayerKawa(nPlayer)[nTurn-1])
    Hands.sort()
    return(Hands)

#print(nPlayerHands(TotalTurn))
#print(PlayerNaki(nPlayer))
#마작 버림패 최대 수 24매

def listStretcher(lList: list, lLenth: int):
    numStretch = lLenth - len(lList)
    if numStretch < 0:
        print("Cannot make list shorter.")
    else:
        for idx in range(numStretch):
            lList.append('')

    return lList

numStretch = {'maxKawa':24, 'maxNaki':4*4, 'maxHand':14}
#print(PlayerKawa(nPlayer))
#print(listStretcher(PlayerKawa(nPlayer), 24))

#N순 모든 버림패
def AllKawaNaki(nTurn, nPlayer):
    Kawa = {0: [], 1: [], 2: [], 3: []}
    Naki = {0: [], 1: [], 2: [], 3: []}
    turn = 0
    for line in Haibo:
        NakiInfo = line.split(': ')
        if ": Discard " in line:
            while turn <= nTurn:
                if int(line[7]) == nPlayer:
                    turn += 1
            #if turn > nTurn:
             #   break
            Kawa[int(line[7])].append(line[-3])
        elif (': Chi ' in line or ': Pon ' in line
                or ': KaKan' in line or ': AnKan' in line
                or ': MinKan' in line):
            Naki[int(line[7])] = re.findall(r"[^A-Za-z0-9: ]+", NakiInfo[2])

    alKawa = []
    for idx in range(4):
        alKawa = alKawa + listStretcher(Kawa[idx], numStretch['maxKawa']) + listStretcher(Naki[idx], numStretch['maxNaki'])

    return alKawa

nTurn = 1

Youtput = nPlayerHands(nTurn, nPlayer)[-1]
Xinput = nPlayerHands(nTurn, nPlayer) + AllKawaNaki(nTurn, nPlayer)

print(Xinput)

''''''


class kyokuHaibo:
    def __init__(self, nTurn, nPlayer):
        self.nTurn = 0
        self.nPlayer = 0

    pass
