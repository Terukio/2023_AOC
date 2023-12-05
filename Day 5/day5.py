import time

testing = False

if testing:
    data = r'Day 5/ex.txt'
else:
    data = r'Day 5/data.txt'

def parseData(data):
    with open(data) as f:
        data = f.read().split('\n\n')
    for i, group in enumerate(data):
        data[i] = group.split(':')
    data2 = []
    data2.append([int(j) for j in data[0][1].split()])
    for i in range(1,8):
        data2.append(clean_up_map(data[i][1][1:]))
    return data2

def clean_up_map(map):
    map = map.split('\n')
    maps = []
    for ind_map in map:
        ind_map = ind_map.split()
        destination,source,ran = [int(i) for i in ind_map]
        maps.append((source,destination,ran))
    return maps

def resource_map(resource,resource_map):
    for map in resource_map:
        source,destination,ran = map
        if source <= resource and resource <= source + (ran - 1):
            destination = destination + (resource - source)
            return destination
    return resource

def day5(data):
    start = time.time()
    data = parseData(data)
    locations = 10**1000
    for seed in data[0]:
        for i in range(7):
            seed = resource_map(seed,data[i + 1])
        locations = min(locations,seed)
    print('Part 1:',locations)
    print('Part 1 Elapsed Time:',round(time.time() - start,4),'seconds.')

    seeds = [i for i in range(data[0][0],data[0][0] + data[0][1])] + [i for i in range(data[0][2],data[0][2] + data[0][3])]
    total_seeds = len(seeds)
    start2 = time.time()
    locations = 10**1000
    for i,seed in enumerate(seeds):
        if i % 1_000_000 == 1:
            print('Seed:',i,'Total Seeds:',total_seeds)
            print(locations)
        for i in range(7):
            seed = resource_map(seed,data[i + 1])
        locations = min(locations,seed)
        
    print('Part 2:',locations)
    print('Part 2 elapsed time:',round(time.time() - start2,4),'seconds.')
    print('Total elapsed time:',round(time.time() - start,4),'seconds.')
day5(data)
