def process_lines(lines):
    '''process each line while tracking some total value the problem asks for'''
    total_value = 0
    data = {}
    for i, line in enumerate(lines):
        value, d = process_line(line, data)
        total_value += value
    return total_value

def process_line(line, data):
    '''break down the line with .strip().split() to do some processing
    return whatever value we are tracking and updated dict'''
    value = 0
    important = set()
    #do some prep work on data
    #pass new data to calc functions
    value = calculate_value(important, data)
    return value, data

def calculate_value(important, data):
    '''whatever calc the specific problem calls for'''
    value = 0
    for num in data:
        if num in important:
            #check for stuff or do stuff
            value = 1 if value == 0 else value * 2
    return value

def main():
    with open('..\\input.txt') as f:
        lines = f.readlines()
        problem_1_value = process_lines(lines)
        print(problem_1_value)

    return 0

if __name__ == '__main__':
    main()