import re,math

def parseData(data):
    with open(data) as f:
        data = f.read().split('\n\n')

    leftright = list(data[0])

    direction = {'L' : 0,
                'R' : 1}

    for i,char in enumerate(leftright):
        leftright[i] = direction[char]

    mapRegex = re.compile(r'(\w+) = \((\w+), (\w+)\)')
    maps = mapRegex.findall(data[1])

    clean_maps = {}

    for map in maps:
        clean_maps[map[0]] = (map[1],map[2])

    return leftright,clean_maps

def part1(data):
    data = parseData(data)
    instructions,nodes = data
    current_position = 'AAA'
    count = 0 
    while current_position != 'ZZZ':
        for instruction in instructions:
            current_position = nodes[current_position][instruction]
            count += 1
            if current_position == 'ZZZ':
                return count
            
def get_steps(position,instructions,nodes):
    count = 0
    while True:
        for instruction in instructions:
            position = nodes[position][instruction]
            count += 1
            if position[-1] == 'Z':
                return count
            
def part2(data):
    data = parseData(data)
    instructions,nodes = data

    current_positions = [node for node in nodes.keys() if node[-1] == 'A']
    counts = {}
    for position in current_positions:
        counts[position] = get_steps(position,instructions,nodes)
    lcm = 1
    for i in counts.values():
        lcm = math.lcm(lcm,i)
    return lcm

testing = False

if testing:
    data = r'Day 8/ex2.txt'
else:
    data = r'Day 8/data.txt'

print(part1(data))
print(part2(data))