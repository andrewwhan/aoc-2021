import sys
from collections import Counter

if len(sys.argv) > 1:
    filename = sys.argv[1]
with open(filename) as f:
    lines = f.readlines()
    num_len = len(lines[0][:-1]) # ignore newline character at end
    oxygen_lines = lines
    co2_lines = lines
    oxygen = ''
    co2 = ''
    for i in range(num_len):
        bit = [x[i] for x in oxygen_lines]
        if (bit.count('0') > bit.count('1')):
            oxygen_lines = list(filter(lambda line: line[i]=='0', oxygen_lines))
        else:
            oxygen_lines = list(filter(lambda line: line[i]=='1', oxygen_lines))
        if len(oxygen_lines) == 1:
            oxygen = oxygen_lines[0]
            break
    for i in range(num_len):
        bit = [x[i] for x in co2_lines]
        if (bit.count('0') <= bit.count('1')):
            co2 += '0'
            co2_lines = list(filter(lambda line: line[i]=='0', co2_lines))
        else:
            co2 += '1'
            co2_lines = list(filter(lambda line: line[i]=='1', co2_lines))
        if len(co2_lines) == 1:
            co2 = co2_lines[0]
            break
    oxygen = int(oxygen, 2)
    co2 = int(co2, 2)
    print(oxygen * co2)