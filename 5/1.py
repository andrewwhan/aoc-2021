import sys
from collections import Counter

if len(sys.argv) > 1:
    filename = sys.argv[1]
with open(filename) as f:
    lines = f.readlines()
    x_max = 0
    y_max = 0
    filled_spaces = []
    for line in lines:
        start, _, end = line.split()
        start = tuple(int(x) for x in start.split(','))
        end = tuple(int(x) for x in end.split(','))
        # Find max coordinates for building 2d array
        x_max = max(x_max, start[0], end[0])
        y_max = max(y_max, start[1], end[1])

        d_x = end[0] - start[0]
        d_y = end[1] - start[1]
        line_len = max(abs(d_x), abs(d_y))
        step = (int(d_x/line_len), int(d_y/line_len))
        if step[0] == 0 or step[1] == 0:
            for i in range(line_len+1):
                filled_spaces.append(tuple(map(lambda x, y: x + i*y, start, step)))
    print(len([x for x in Counter(filled_spaces).values() if x > 1]))