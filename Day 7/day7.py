import re,itertools

testing = False

if testing:
    data = r'AoC 2023/Day 7/ex.txt'
else:
    data = r'AoC 2023/Day 7/data2.txt'

class Hand:
    def __init__(self,hand,bid):
        self.hand = hand
        self.bid = int(bid)
        self.rank = 1
        self.jack_rank = 1
        self.kind = self.kind()
        self.jack_kind = self.jack_kind()
    
    def kind(self):
        dict_hand = {}
        for card in self.hand:
            dict_hand.setdefault(card,0)
            dict_hand[card] += 1
        if 5 in dict_hand.values():
            return 6
        elif 4 in dict_hand.values():
            return 5
        elif 3 in dict_hand.values():
            if 2 in dict_hand.values():
                return 4
            else:
                return 3
        elif 2 in dict_hand.values():
            if len(dict_hand) == 3:
                return 2
            else:
                return 1
        else:
            return 0
        
    def jack_kind(self):
        dict_hand = {}
        for card in self.hand:
            dict_hand.setdefault(1,0)
            dict_hand.setdefault(card,0)
            dict_hand[card] += 1
        if 5 in dict_hand.values():
            return 6
        elif 4 in dict_hand.values():
            if dict_hand[1] == 1 or dict_hand[1] == 4:
                return 6
            else:
                return 5
        elif 3 in dict_hand.values():
            if 2 in dict_hand.values():
                if dict_hand[1] == 2 or dict_hand[1] == 3:
                    return 6
                else:
                    return 4
            else:
                if dict_hand[1] == 1 or dict_hand[1] == 3:
                    return 5
                else:
                    return 3
        elif 2 in dict_hand.values():
            if len(dict_hand) == 3 or (len(dict_hand) == 4 and dict_hand[1] == 0):
                if dict_hand[1] == 2:
                    return 5
                elif dict_hand[1] == 1:
                    return 4
                else:
                    return 2
            else:
                if dict_hand[1] == 2 or dict_hand[1] == 1:
                    return 3
                else:
                    return 1
        else:
            if dict_hand[1] == 1:
                return 1
            else:
                return 0

        
    def beats(self,hand2):
        if self.kind > hand2.kind:
            return True
        elif self.kind == hand2.kind:
            for i in range(5):
                if int(self.hand[i]) > int(hand2.hand[i]):
                    return True
                elif int(self.hand[i]) < int(hand2.hand[i]):
                    return False
            return False
        return False
    
    def jack_beats(self,hand2):
        if self.jack_kind > hand2.jack_kind:
            return True
        elif self.jack_kind == hand2.jack_kind:
            for i in range(5):
                if int(self.hand[i]) > int(hand2.hand[i]):
                    return True
                elif int(self.hand[i]) < int(hand2.hand[i]):
                    return False
            return False
        return False
        
handRegex = re.compile(r'([\w\d]{5}) (\d+)')

with open(data) as f:
    data = f.read()
    data = handRegex.findall(data)

hands = []

for hand in data:
    hand,bid = hand
    hand = list(hand)
    for i,card in enumerate(hand):
        if card == 'A':
            hand[i] = 14
        elif card == 'T':
            hand[i] = 10
        elif card == 'J':
            hand[i] = 11
        elif card == 'Q':
            hand[i] = 12
        elif card == 'K':
            hand[i] = 13
    hands.append(Hand(hand,bid))

comparisions = list(itertools.combinations(hands, 2))

for comparision in comparisions:
    hand1,hand2 = comparision
    if hand1.beats(hand2):
        hand1.rank += 1
    else:
        hand2.rank += 1

hands2 = []

for hand in data:
    hand,bid = hand
    hand = list(hand)
    for i,card in enumerate(hand):
        if card == 'A':
            hand[i] = 14
        elif card == 'T':
            hand[i] = 10
        elif card == 'J':
            hand[i] = 1
        elif card == 'Q':
            hand[i] = 12
        elif card == 'K':
            hand[i] = 13
    hands2.append(Hand(hand,bid))

comparisions2 = list(itertools.combinations(hands2, 2))
for comparision2 in comparisions2:
    hand1,hand2 = comparision2
    if hand1.jack_beats(hand2):
        hand1.jack_rank += 1
    else:
        hand2.jack_rank += 1
    

total_winnings = sum([hand.rank * hand.bid for hand in hands])
total_jack_winnings = sum([hand2.jack_rank * hand2.bid for hand2 in hands2])

print(total_winnings)
print(total_jack_winnings)