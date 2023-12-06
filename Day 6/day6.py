import math

races = [(51,222),(92,2031),(68,1126),(90,1225)]
races2 = [(51926890,222203111261225)]

prod = 1

for t,r in races:
    count = 0
    sol = ((t - math.sqrt(t**2 - (4 * r)))/2,(t + math.sqrt(t**2 - (4 * r)))/2)
    add = math.floor(sol[1]) - math.floor(sol[0])
    if sol[0].is_integer():
        add -= 1
    prod *= add

print('Part 1:',prod)

prod = 1

for t,r in races2:
    count = 0
    sol = ((t - math.sqrt(t**2 - (4 * r)))/2,(t + math.sqrt(t**2 - (4 * r)))/2)
    add = math.floor(sol[1]) - math.floor(sol[0])
    if sol[0].is_integer():
        add -= 1
    prod *= add

print('Part 2:',prod)