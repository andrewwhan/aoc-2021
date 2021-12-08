import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
with open(filename) as f:
    lines = f.readlines()
    horizontal = 0
    depth = 0
    aim = 0
    for l in lines:
        direction, value = l.split()
        value = int(value)
        if direction == "forward":
            horizontal += value
            depth += aim*value
        elif direction == "up":
            aim -= value
        elif direction == "down":
            aim += value
        else:
            print("huh?")
    print(horizontal*depth)