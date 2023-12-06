import sys
import re
from collections import defaultdict

class conversion_table:
    def __init__(self, chunk):
        lines = chunk.split('\n')[1:]
        self.chart: list[tuple[int,int,int]] = [[int(i) for i in line.split()] for line in lines]

    def convert_ranges(self, ranges):
        converted_ranges = []
        for (dest, source, size) in self.chart:
          src_end = source + size
          new_range = []
          while ranges:
            (start,end) = ranges.pop()
            '''
            [start                                 end)
                     [source    src_end]
            [BEFORE ][INTER            ][AFTER        )
            '''
            before = (start,min(end,source))
            inter = (max(start, source), min(src_end, end))
            after = (max(src_end, start), end)
            if before[1]>before[0]:
              new_range.append(before)
            if inter[1]>inter[0]:
              converted_ranges.append((inter[0]-source+dest, inter[1]-source+dest))
            if after[1]>after[0]:
              new_range.append(after)
          ranges = new_range
        return converted_ranges + ranges


def main():
    D = open('..\\input.txt').read().strip()
    L = D.split('\n')

    parts = D.split('\n\n')
    seed, *others = parts
    seed = [int(x) for x in seed.split(':')[1].split()]

    Fs = [conversion_table(s) for s in others]

    P2 = []
    pairs = list(zip(seed[::2], seed[1::2]))
    for start, size in pairs:
        # inclusive on the left, exclusive on the right
        # e.g. [1,3) = [1,2]
        # length of [a,b) = b-a
        # [a,b) + [b,c) = [a,c)
        R = [(start, start+size)]
        for f in Fs:
            R = f.convert_ranges(R)
        P2.append(min(R)[0])
    print(min(P2))
    return 0

if __name__ == '__main__':
    main()