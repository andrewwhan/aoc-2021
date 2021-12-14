import sys
from statistics import mean

if len(sys.argv) > 1:
    filename = sys.argv[1]
with open(filename) as f:
    lines = f.readlines()
    crabs = [int(x) for x in lines[0].split(',')]
    # Best alignment was actually 480 not 481
    alignment = round(mean(crabs))
    fuel = 0
    for crab in crabs:
        dist = abs(alignment - crab)
        fuel += (dist*(dist+1))/2
    print(fuel)