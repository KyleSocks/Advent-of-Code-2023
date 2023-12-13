import copy
class puzzle:
    def __init__(self, input):
        print('puzzle:')
        self.lines = input.split('\n')
        self.left_columns = self.hasVerticalReflection()
        self.above_rows = self.hasHorizontalReflection()
        self.score = self.left_columns + (self.above_rows * 100)
        if not self.score:
            print(input)
        print('score: ',self.score)
        print('\n')
        print('*******************************************')

    def hasHorizontalReflection(self):
        temp = self.lines.copy()
        reflection_indices = []
        for i in range(1, len(temp)-1):
            start = temp[0:i]
            end = temp[-1:i-1:-1]
            if len(start) > len(end):
                start = start[len(start)-len(end):]
            if len(end) > len(start):
                end = end[len(end)-len(start):]
            if start == end:
                reflection_indices.append(i)
        skip = 1
        if len(reflection_indices):
            for line in self.lines.copy():
                if line == temp[reflection_indices[0]]:
                    if skip:
                        skip = 0
                    else:
                        print('-' * len(temp[0]))
                print(line)
            return max(reflection_indices)
        else:
            return 0

    def hasVerticalReflection(self):
        temp = self.lines.copy()
        first = temp[0]
        reflection_indices = []
        has_reflection = False
        for i in range(1, len(first)-1):
            start = first[0:i]
            end = first[-1:i-1:-1]
            if len(start) > len(end):
                start = start[len(start)-len(end):]
            if len(end) > len(start):
                end = end[len(end)-len(start):]
            if start == end:
                reflection_indices.append(i)
                has_reflection = True

        if has_reflection:
            for t in temp[1:]:
                for j in reflection_indices:
                    start = t[0:j]
                    end = t[-1:j-1:-1]
                    if len(start) > len(end):
                        start = start[len(start)-len(end):]
                    if len(end) > len(start):
                        end = end[len(end)-len(start):]
                    if start != end:
                        reflection_indices.remove(j)

        if len(reflection_indices):
            for line in self.lines.copy():
                print(line[0:reflection_indices[0]], '|', line[reflection_indices[0]:-1])
            return max(reflection_indices)
        else:
            return 0

        



def main():
    file = open('input.txt').read().strip()
    groups = file.split('\n\n')

    puzzles = [puzzle(group) for group in groups]
    scores = []
    for x in puzzles:
        scores.append(x.score)

    print('part 1: ', sum(scores))
    return 0

if __name__ =='__main__':
    main()