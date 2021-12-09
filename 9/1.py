import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
with open(filename) as f:
    lines = f.readlines()
    line_len = len(lines[0][:-1])
    heightmap = [[0 for j in range(line_len)] for i in range(len(lines))]
    for i, l in enumerate(lines):
        for j, c in enumerate(l.split()[0]):
            heightmap[i][j] = c
    risklevel = 0
    for j in range(line_len):
        for i in range(len(lines)):
            val = int(heightmap[i][j])
            if i-1 >= 0 and int(heightmap[i-1][j]) <= val:
                continue
            elif i+1 < len(lines) and int(heightmap[i+1][j]) <= val:
                continue
            elif j-1 >= 0 and int(heightmap[i][j-1]) <= val:
                continue
            elif j+1 < line_len and int(heightmap[i][j+1]) <= val:
                continue
            else:
                risklevel += val + 1
    print(risklevel)