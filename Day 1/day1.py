import re

testing = False

if testing:
    data = r'Day 1/ex.txt'
else:
    data = r'Day 1/data.txt'

def parseData(data):
    with open(data) as f:
        data = f.read().splitlines()
    return data

def day1(data):
    part1sum = 0
    part2sum = 0
    digits = {'one' : '1',
              'two' : '2',
              'three' : '3',
              'four' : '4',
              'five' : '5',
              'six' : '6',
              'seven' : '7',
              'eight' : '8',
              'nine' : '9'}
    data = parseData(data)
    for line in data:
        part1calibration = ''
        part2calibration = ''
       
        digitRegex = re.compile(r'\d|one|two|three|four|five|six|seven|eight|nine')
        digitRegexReversed = re.compile(r'\d|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin')
        part2firstdigit = digitRegex.search(line).group()
        part2seconddigit = digitRegexReversed.search(line[::-1]).group()
        if part2firstdigit in digits.keys():
            part2calibration += digits[part2firstdigit]
        else:
            part2calibration += part2firstdigit
        if part2seconddigit[::-1] in digits.keys():
            part2calibration += digits[part2seconddigit[::-1]]
        else:
            part2calibration += part2seconddigit

        part2sum += int(part2calibration)

    print(part2sum)

day1(data)
