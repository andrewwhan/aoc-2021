from functools import reduce
import sys
from collections import Counter

def go_downstream(i,j,heightmap,visited):
    if (i,j) in visited:
        return heightmap[i][j][1]
    visited.append((i,j))
    val = int(heightmap[i][j][0])
    if i-1 >= 0 and int(heightmap[i-1][j][0]) < val:
        low_point = go_downstream(i-1, j, heightmap, visited)
        heightmap[i][j][1] = low_point
        return low_point
    elif i+1 < len(heightmap) and int(heightmap[i+1][j][0]) < val:
        low_point = go_downstream(i+1, j, heightmap, visited)
        heightmap[i][j][1] = low_point
        return low_point
    elif j-1 >= 0 and int(heightmap[i][j-1][0]) < val:
        low_point = go_downstream(i, j-1, heightmap, visited)
        heightmap[i][j][1] = low_point
        return low_point
    elif j+1 < len(heightmap[0]) and int(heightmap[i][j+1][0]) < val:
        low_point = go_downstream(i, j+1, heightmap, visited)
        heightmap[i][j][1] = low_point
        return low_point
    else:
        low_point = (i,j)
        heightmap[i][j][1] = low_point
        return low_point

if len(sys.argv) > 1:
    filename = sys.argv[1]
with open(filename) as f:
    lines = f.readlines()
    line_len = len(lines[0][:-1])
    heightmap = [[[0,0] for j in range(line_len)] for i in range(len(lines))]
    for i, l in enumerate(lines):
        for j, c in enumerate(l.split()[0]):
            heightmap[i][j][0] = c
    visited = []
    for j in range(line_len):
        for i in range(len(lines)):
            val = int(heightmap[i][j][0])
            if val == 9:
                continue
            elif (i,j) in visited:
                continue
            else:
                go_downstream(i,j,heightmap,visited)
    basin_dict = Counter([x[1] for y in heightmap for x in y])
    basin_dict.pop(0)
    print(reduce((lambda x, y: x* y), sorted(basin_dict.values(),reverse=True)[:3]))