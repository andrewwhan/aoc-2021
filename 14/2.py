import sys
from collections import Counter

if len(sys.argv) > 1:
    filename = sys.argv[1]
    steps = int(sys.argv[2])
with open(filename) as f:
    lines = f.readlines()
    polymer_string = lines[0].strip()
    element_count = Counter(polymer_string)
    rule_dict = {}
    for i in range(2, len(lines)):
        pair, _, insertion = lines[i].split()
        rule_dict[pair] = (pair[0]+insertion, insertion+pair[1], insertion)
    polymer_pairs = {pair:0 for pair in rule_dict.keys()}
    for i in range(len(polymer_string) - 1):
        polymer_pairs[polymer_string[i:i+2]] += 1    
    
    for i in range(steps):
        new_polymer = {pair:0 for pair in rule_dict.keys()}
        for pair, count in polymer_pairs.items():
            new_pair_1, new_pair_2, insertion = rule_dict[pair]
            new_polymer[new_pair_1] += count
            new_polymer[new_pair_2] += count
            element_count[insertion] += count
        polymer_pairs = new_polymer
    
    print(max(element_count.values()) - min(element_count.values()))