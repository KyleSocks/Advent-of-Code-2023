def check_adjacent(matrix, x, y):
    s = "!@#$%^&*()+/!@#$%^&*()_-="
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    for direction in directions:
        nx = x + direction[0]
        ny = y + direction[1]
        if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[x]):
            if matrix[nx][ny] in s:
                return True
    return False

def get_part_num(line, start, end):
    return int(line[start:end+1])

def find_num(matrix, x, y, dx, dy):
    s = "!@#$%^&*()+/!@#$%^&*()_-=."
    num_start_idx = 0
    num_end_idx = 0

    if dx != 0:
        if dy == 0:
            for j in range(y+dy,len(matrix[x+dx])):
                if matrix[x + dx][j] in s:
                    num_end_idx = j
                    break
            for j in range(y+dy):
                if matrix[x + dx][j] in s:
                    num_start_idx = j + 1
        if dy > 0:
            num_start_idx = y +1
            for j in range(y+dy,len(matrix[x+dx])):
                if matrix[x + dx][j] in s:
                    num_end_idx = j
                    break
        if dy < 0:
            num_end_idx = y
            for j in range(num_end_idx):
                if matrix[x + dx][j] in s:
                    num_start_idx = j + 1
    else:
        if dy > 0:
            num_start_idx = y +1
            for j in range(y+dy,len(matrix[x+dx])):
                if matrix[x + dx][j] in s:
                    num_end_idx = j
                    break
        if dy < 0:
            num_end_idx = y
            for j in range(y+dy):
                if matrix[x + dx][j] in s:
                    num_start_idx = j + 1

    if num_end_idx == 0:
        num_end_idx = len(matrix[x+dx])

    return int(matrix[x + dx][num_start_idx:num_end_idx])



def is_gear(matrix, x, y): # returns 0 if not a gear or the ratio if it is
    number_parts = 0
    gear_ratio = 1
    nx = x - 1
    ny = y
    #check the line above
    if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[x]):
        if matrix[nx][ny] in ('1','2','3','4','5','6','7','8','9','0'):
            number_parts += 1
            gear_ratio *= find_num(matrix,x,y,-1,0)
        else:
            ny = y - 1
            if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[x]):
                if matrix[nx][ny] in ('1','2','3','4','5','6','7','8','9','0'):
                    number_parts += 1
                    gear_ratio *= find_num(matrix,x,y,-1,-1)
            ny = y + 1
            if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[x]):
                if matrix[nx][ny] in ('1','2','3','4','5','6','7','8','9','0'):
                    number_parts += 1
                    gear_ratio *= find_num(matrix,x,y,-1,1)

    #check the line below
    nx = x + 1
    ny = y
    if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[x]):
        if matrix[nx][ny] in ('1','2','3','4','5','6','7','8','9','0'):
            number_parts += 1
            gear_ratio *= find_num(matrix,x,y,1,0)
        else:
            ny = y - 1
            if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[x]):
                if matrix[nx][ny] in ('1','2','3','4','5','6','7','8','9','0'):
                    number_parts += 1
                    gear_ratio *= find_num(matrix,x,y,1,-1)
            ny = y + 1
            if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[x]):
                if matrix[nx][ny] in ('1','2','3','4','5','6','7','8','9','0'):
                    number_parts += 1
                    gear_ratio *= find_num(matrix,x,y,1,1)

    nx = x
    ny = y - 1
    if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[x]):
        if matrix[nx][ny] in ('1','2','3','4','5','6','7','8','9','0'):
            number_parts += 1
            gear_ratio *= find_num(matrix,x,y,0,-1)
    ny = y + 1
    if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[x]):
        if matrix[nx][ny] in ('1','2','3','4','5','6','7','8','9','0'):
            number_parts += 1
            gear_ratio *= find_num(matrix,x,y,0,1)

    if number_parts == 2:
        return gear_ratio

    return 0



def main():
    with open('input.txt') as f:
        total_part_sum = 0
        total_gear_ratios = 0
        lines = f.readlines()
        new_num = True
        part_num = False
        num_start_idx = 9999
        num_end_idx = 0
        for i in range(len(lines)):
            if part_num:
                total_part_sum += get_part_num(lines[i], num_start_idx, num_end_idx)
            new_num = True
            part_num = False
            num_start_idx = 9999
            num_end_idx = 0
            for j in range(len(lines[i])):
                if lines[i][j] == '*':
                    total_gear_ratios += is_gear(lines,i,j)
                if lines[i][j] in ('1','2','3','4','5','6','7','8','9','0'):
                    if num_start_idx > j:
                        num_start_idx = j
                    num_end_idx = j
                    if new_num == False:
                        continue
                    if check_adjacent(lines,i,j):
                        part_num = True
                        new_num = False
                else:
                    if part_num:
                        total_part_sum += get_part_num(lines[i], num_start_idx, num_end_idx)
                    part_num = False
                    new_num = True
                    num_start_idx = 9999
                    num_end_idx = 0

    print(total_part_sum)
    print(total_gear_ratios)


if __name__ == '__main__':
    main()