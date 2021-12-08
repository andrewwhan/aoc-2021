import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
with open(filename) as f:
    lines = [int(i) for i in f.readlines()]
    window = 3
    # initial sum of the first 3 values
    windowsum = sum(lines[0:window])
    last = windowsum
    increases = 0
    for i in range(0, len(lines) - window):
        # when the window slides, remove the first value from 
        # the window and add the new one we're sliding into
        windowsum -= lines[i]
        windowsum += lines[i+window]
        if windowsum > last:
            increases += 1
        last = windowsum
    print(increases)