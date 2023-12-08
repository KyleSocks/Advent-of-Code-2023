import math

# Function to find the LCM of two numbers
def lcm(a, b):
    return (a * b) // math.gcd(a, b)

# Function to find the LCM of a list of numbers
def lcm_of_list(numbers):
    lcm_result = 1
    for i in range(len(numbers)):
        lcm_result = lcm(lcm_result, numbers[i])
    return lcm_result

def part_1(patterns, pairs):
    node = 'AAA'
    steps = 0
    while node != 'ZZZ':
        index = steps % len(patterns)
        steps += 1
        left, right = pairs[node]
        if patterns[index] == 'L':
            node = left
        else:
            node = right
    return steps

def helper(patterns, pairs, node):
    steps = 0
    while node[-1] != 'Z':
        index = steps % len(patterns)
        steps += 1
        left, right = pairs[node]
        if patterns[index] == 'L':
            node = left
        else:
            node = right
    return steps

def part_2(pattern, pairs):
    steps = 0
    distances_to_end = {}

    for key in pairs.keys():
        if key.strip()[-1] == 'A':
            dist = int(helper(pattern,pairs,key))
            distances_to_end[key] = dist

    return(lcm_of_list(list(distances_to_end.values())))

def main():
    file = open('input.txt').read().strip()
    pattern, maps = file.split('\n\n')

    lr_pairs = {} # {node_name : tuple(left,right)}
    for line in maps.split('\n'):
        node_name, strpair = line.split('=')
        pair = tuple(x.strip() for x in strpair.strip()[1:-1].split(','))
        lr_pairs[node_name.strip()] = pair

    print(part_1(pattern,lr_pairs))
    print(part_2(pattern,lr_pairs))
    return 0

if __name__ =='__main__':
    main()