import regex

testing = input('Testing: ')

if testing == 'y':
    part = input('Part: ')
    if part == '1':
        data = r'Day 1/ex1.txt'
    else:
        data = r'Day 1/ex2.txt'
else:
    data = r'Day 1/data.txt'

def parseData(data):
    with open(data) as f:
        data = f.read().splitlines()
    return data

def day1(data):
    data = parseData(data)
    digitRegex = regex.compile(r'(\d|one|two|three|four|five|six|seven|eight|nine)')
    convert = {'one' : '1',
               'two' : '2',
               'three' : '3',
               'four' : '4',
               'five' : '5',
               'six' : '6',
               'seven' : '7',
               'eight' : '8',
               'nine' : '9'}
    part1sum = 0
    part2sum = 0
    for line in data:
        calibration1 = ''
        digits = digitRegex.findall(line, overlapped = True)
        for char in line:
            if char.isdecimal():
                calibration1 += char
                break
        for char in line[::-1]:
            if char.isdecimal():
                calibration1 += char
                break
        if not calibration1:
            calibration1 = 0
        calibration1 = int(calibration1)
        for i,digit in enumerate(digits):
            if not digit.isdecimal():
                digits[i] = convert[digit]
        calibration2 = int(digits[0] + digits[-1])
        part1sum += calibration1
        part2sum += calibration2

    print('Part 1:',part1sum,'| Part 2:',part2sum)

day1(data)