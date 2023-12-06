def process_lines(lines):
    '''process each line while tracking some total value the problem asks for'''
    total_value = 0
    lowest_location = 9999999999
    data = [] #[{source:dest, sourcenum:destnum, ...},[...]]
    seeds = set()
    seeds2 = {}
    line_break = False
    j = -1
    for i, line in enumerate(lines):
        if i == 0:
            name, numbers = line.strip().split(':')
            nums = numbers.strip().split(' ')
            for num in nums:
                seeds.add(int(num))
                seeds2[int(num)] = int(num)
                #print(seeds)
                #print(seeds2)
        else:
            #value, d, line_break, j = 
            #print('processing ', line)
            lowest_location = process_line(line, data, line_break, j, lines, seeds, seeds2)
            total_value += 0#value
    #print(data)
    return min(seeds2.values())

def find_distance(data, seeds, seeds2):
    lowest_dist = 9999999999
    for seed in seeds:
        if seed != '':
            dist = int(seed)
            keys = data.keys()
            vals = data.values()
            val = int(seeds2[seed])
            if val in data:
                first_key = next(iter(data))
                print('converting, ', dist, data[val])
                seeds2[dist] =  int(data[val])
                #print(seeds2)
                #print(data[first_key], dist)


            if 'location' in data:
                #print(dist)
                break
            if dist < lowest_dist:
                lowest_dist = dist
    return lowest_dist

def process_line(line, data, line_break, index, lines, seeds, seeds2):
    '''break down the line with .strip().split() to do some processing
    return whatever value we are tracking and updated dict'''
    table_data = {}
    if len(line.strip()) == 0:
        #data.add({})
        return 0, data, True, index + 1

    if "map" in line:
        #print(line)
        sourcedest, t = line.strip().split(' ')
        source, t2, dest = sourcedest.strip().split('-')
        temp = {}
        temp[source] = dest
        table_data[source] = dest
        #print(data)
        last_block = {}
        last_block =  process_block(last_block, index, lines, line, seeds, seeds2)
        #shortest_len = find_distance(last_block, seeds, seeds2)
        return 0


def process_block(data, data_index, lines, mapline, seeds, seeds2):
    update_check = {}
    for c in seeds:
        update_check[c] = 0
    index = -1
    line = lines[index]
    while True:
        index += 1
        if line == mapline:
            break
        line = lines[index]
    linest = lines[index:]
    for line in linest:
        if len(line.strip()) != 0:
            dstart, sstart, rang = line.strip().split(' ')
            convert(seeds,seeds2,int(dstart),int(sstart),int(rang), update_check)
            #k = range(int(sstart),int(sstart)+int(rang))
            #m = range(int(dstart),int(dstart)+int(rang))
            '''
            for i, t in enumerate(k):
                data[k[i]]= m[i]
                #print(data)
            '''
        else:
            break

    return data

def convert(seeds, seeds2, dstart, sstart, rang, update_check):
    for seed in seeds:
        val = seeds2[seed]
        if sstart <= val < (sstart + rang):
            if update_check[seed] == 0:
                diff = val - sstart
                seeds2[seed] = dstart + diff
                update_check[seed] = 1


def main():
    with open('..\\input.txt') as f:
        lines = f.readlines()
        problem_1_value = process_lines(lines)
        print(problem_1_value)

    return 0

if __name__ == '__main__':
    main()
