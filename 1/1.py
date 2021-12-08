import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
with open(filename) as f:
    lines = f.readlines()
    last = -1
    increases = 0
    for i in [int(i) for i in lines]:
        if i > last and last != -1:
            increases += 1
        last = i
    print(increases)