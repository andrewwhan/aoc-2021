import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
with open(filename) as f:
    lines = f.readlines()
    num_len = len(lines[0][:-1]) # ignore newline character at end
    counts = [{0:0, 1:0} for x in range(num_len)]
    for i in range(len(lines)):
        for j in range(num_len):
            counts[j][int(lines[i][j])] += 1
    gamma_string = ''.join(['0' if x[0] > x[1] else '1' for x in counts])
    epsilon_string = ''.join(['1' if x[0] > x[1] else '0' for x in counts])
    gamma = int(gamma_string, 2)
    epsilon = int(epsilon_string, 2)
    print(gamma * epsilon)