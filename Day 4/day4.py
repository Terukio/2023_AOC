import re

testing = False

if testing:
    data = r'Day 4/ex.txt'
else:
    data = r'Day 4/data.txt'

class Card:
    def __init__(self,id,winning_numbers,player_numbers):
        self.id = int(id)
        self.winning_numbers = self.make_list(winning_numbers)
        self.player_numbers = self.make_list(player_numbers)
        self.score = self.determine_score()[1]
        self.number_of_winning_numbers = self.determine_score()[0]

    def make_list(self,numbers):
        numbers = numbers.split()
        for i,number in enumerate(numbers):
            numbers[i] = int(number)
        return numbers
    
    def determine_score(self):
        number_of_winning_numbers = 0
        for number in self.player_numbers:
            if number in self.winning_numbers:
                number_of_winning_numbers += 1
        score = (2 ** (number_of_winning_numbers - 1))
        if score < 1:
            score = 0
        return number_of_winning_numbers,score

def parseData(data):
    cards = []
    with open(data) as f:
        data = f.read()
    cardRegex = re.compile(r'Card\s+(\d+):([\d\s]+)\|([\d\s]+)')
    cardmo = cardRegex.findall(data)

    for card in cardmo:
        id,winning_numbers,player_numbers = card
        cards.append(Card(id,winning_numbers,player_numbers))
    
    return cards

def day4(data):
    cards = parseData(data)
    scores = []
    number_of_cards = {}
    for card in cards:
        scores.append(card.score)
        number_of_cards[card.id] = 1

    for id,number in number_of_cards.items():
        for _ in range(number):
            for i in range(1,cards[id - 1].number_of_winning_numbers + 1):
                if (id + i) in number_of_cards.keys():
                    number_of_cards[id + i] += 1
    
    print('Part 1:',sum(scores))
    print('Part 2:',sum(number_of_cards.values()))
    


day4(data)