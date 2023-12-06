import time as t

def calculate(time:int, dist:int):
    winning_pairs = [] # [(speed,distance)]
    for speed in range(time):
        if speed != 0:
            time_left = time - speed
            distance = speed * time_left
            if distance > dist:
                winning_pairs.append((speed,distance))

    return winning_pairs

def smart_calc(time:int, dist:int)-> int:
    min_speed = 0
    for speed in range(time):
        if speed != 0:
            time_left = time - speed
            distance = speed * time_left
            if distance > dist:
                min_speed = speed
                break
    max_speed = 0
    for speed in range(time)[::-1]:
        if speed != 0:
            time_left = time - speed
            distance = speed * time_left
            if distance > dist:
                max_speed = speed
                break

    return max_speed - min_speed + 1


def main():
    file = open('input.txt').read().strip()
    lines = file.split('\n')
    times, distances = lines

    times = [int(x) for x in times.split(':')[1].split()]
    distances = [int(x) for x in distances.split(':')[1].split()]

    pairs = list(zip(times, distances))
    total = 1

    for time, distance in pairs:
        ways_to_win = calculate(time, distance)
        total *= len(ways_to_win)

    print(total)

    #part 2
    time2 = int(''.join(str(num) for num in times))
    distance2 = int(''.join(str(num) for num in distances))
    
    start_time = t.time()
    problem_2 = len(calculate(time2, distance2))
    end_time = t.time()
    print(problem_2)
    print('new method took ', end_time - start_time, ' seconds')

    start_time = t.time()
    problem_2 = smart_calc(time2,distance2)
    end_time = t.time()
    print(problem_2)
    print('new method took ', end_time - start_time, ' seconds')
    return 0

if __name__ =='__main__':
    main()
