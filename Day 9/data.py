import math,re,fractions

testing = False

if testing:
    data = r'Day 9/ex.txt'
else:
    data = r'Day 9/data.txt'

def parseData(data):
    numRegex = re.compile(r'[\-\d+]+')
    with open(data) as f:
        data = f.read().splitlines()
    histories = []
    for line in data:
        histories.append([int(i) for i in numRegex.findall(line)])
    return histories

def extrapolated_value(history):
    n = 0
    differences_history = [history[0]]
    differences = history
    while len(set(differences)) != 1:
        differences = [j - i for i, j in zip(differences, differences[1:])]
        differences_history.append(differences[0])
        n += 1
    differences_history.append(0)
    extrapolated = 0
    for i,difference in enumerate(differences_history[::-1]):
        temp_extrapolated = 0
        temp_extrapolated += fractions.Fraction(difference,math.factorial(len(differences_history) - 1 - i))
        for i in range((n + 1) - i):
            temp_extrapolated *= (len(history) - i)
        extrapolated += temp_extrapolated
    return extrapolated

def day9(data):
    histories = parseData(data)
    print(sum([extrapolated_value(history) for history in histories]))
    print(sum([extrapolated_value(history[::-1]) for history in histories]))

day9(data)