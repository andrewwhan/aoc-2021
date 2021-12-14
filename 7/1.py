import sys
from statistics import median

if len(sys.argv) > 1:
    filename = sys.argv[1]
with open(filename) as f:
    lines = f.readlines()
    crabs = [int(x) for x in lines[0].split(',')]
    alignment = median(crabs)
    fuel = 0
    for crab in crabs:
        fuel += abs(alignment - crab)
    print(fuel)