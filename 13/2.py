import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
with open(filename) as f:
    lines = f.readlines()
    coord_end = lines.index('\n')
    dot_set = set()
    fold_list = []
    for i in range(coord_end):
        x,y = lines[i][:-1].split(',')
        dot_set.add((int(x),int(y)))
    for i in range(coord_end+1, len(lines)):
        axis, val = lines[i].split()[2].split('=')
        fold_list.append((axis, int(val)))
    for fold in fold_list:
        axis, val = fold
        new_dot_set = set()
        if axis == 'x':
            axis_ind = 0
        else:
            axis_ind = 1
        for dot in dot_set:
            if dot[axis_ind] > val:
                flipped_val = val - abs(val - dot[axis_ind])
                new_dot = [0,0]
                new_dot[axis_ind] = flipped_val
                new_dot[1-axis_ind] = dot[1-axis_ind]
                new_dot = tuple(new_dot)
                new_dot_set.add(new_dot)
            else:
                new_dot_set.add(dot)
        dot_set = new_dot_set
    x_max = 0
    y_max = 0
    for dot in dot_set:
        if dot[0] > x_max:
            x_max = dot[0]
        if dot[1] > y_max:
            y_max = dot[1]
    plot = [["." for i in range(x_max+1)] for j in range(y_max+1)]
    for dot in dot_set:
        plot[dot[1]][dot[0]] = "#"
    for line in plot:
        print(line)