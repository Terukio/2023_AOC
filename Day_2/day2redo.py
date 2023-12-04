import re

testing = False

if testing:
    data = r'Day_2/ex.txt'
else:
    data = r'Day_2/data.txt'

class Game:
    def __init__(self,id,game):
        self.id = id + 1
        self.game = game
        self.colors = {}
        self.count_colors()
        self.power = self.determine_power()

    def count_colors(self):
        blockRegex = re.compile(r'(\d+) (red|green|blue)')
        blocks = blockRegex.findall(self.game)
        for count,color in blocks:
            self.colors.setdefault(color,0)
            self.colors[color] = max(self.colors[color],int(count))
    
    def is_valid(self):
        if self.colors['red'] <= 12 and self.colors['green'] <= 13 and self.colors['blue'] <= 14:
            return True
        return False
    
    def determine_power(self):
        power = 1
        for count in self.colors.values():
            power *= count
        return power
        
def parseData(data):
    with open(data) as f:
        data = f.read().splitlines()
    games = []
    for index,game in enumerate(data):
        game = game.split(':')
        games.append(Game(index,game[1]))
    return games

def day2(data):
    part1sum = 0
    part2sum = 0
    games = parseData(data)
    for game in games:
        if game.is_valid():
            part1sum += game.id
        part2sum += game.power
    print(part1sum,part2sum)

day2(data)