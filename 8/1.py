import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
with open(filename) as f:
    lines = f.readlines()
    unique_count = 0
    for l in lines:
        input, output = l.split('|')
        for val in output.split():
            if len(val) in [2,3,4,7]:
                unique_count += 1
    print(unique_count)