import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
    days = int(sys.argv[2])
with open(filename) as f:
    lines = f.readlines()
    fish_dict = {i:0 for i in range(9)}
    fishen = lines[0].split(',')
    for fish in fishen:
        fish = int(fish)
        fish_dict[fish] += 1
    print(fish_dict)
    for i in range(days):
        new_fish_dict = {i:0 for i in range(9)}
        for j in range(1, 9):
            new_fish_dict[j-1] = fish_dict[j]
        new_fish_dict[6] += fish_dict[0]
        new_fish_dict[8] = fish_dict[0]
        fish_dict = new_fish_dict
    print(sum(fish_dict.values()))