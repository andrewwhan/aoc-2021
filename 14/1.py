import sys
from collections import Counter

if len(sys.argv) > 1:
    filename = sys.argv[1]
    steps = int(sys.argv[2])
with open(filename) as f:
    lines = f.readlines()
    polymer = lines[0].strip()
    rule_dict = {}
    for i in range(2, len(lines)):
        pair, _, insertion = lines[i].split()
        rule_dict[pair] = insertion
    for i in range(steps):
        new_polymer = ""
        for j in range(len(polymer) - 1):
            new_polymer += polymer[j] + rule_dict[polymer[j:j+2]]
        new_polymer += polymer[-1]
        polymer = new_polymer
    element_count = Counter(polymer).values()
    print(max(element_count) - min(element_count))