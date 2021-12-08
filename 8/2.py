import sys

def signal_is_subset(subset, superset):
    for c in subset:
        if c not in superset:
            return False
    return True

def get_signal_for_val(signal_dict, val):
    return list(signal_dict.keys())[list(signal_dict.values()).index(val)]

def sort_signal(signal):
    return ''.join(sorted(signal))

if len(sys.argv) > 1:
    filename = sys.argv[1]
with open(filename) as f:
    lines = f.readlines()
    total_value = 0
    for l in lines:
        input, output = l.split('|')
        signal_dict = dict()
        undet = []
        for val in input.split():
            if len(val) == 2:
                signal_dict[sort_signal(val)] = '1'
            elif len(val) == 3:
                signal_dict[sort_signal(val)] = '7'
            elif len(val) == 4:
                signal_dict[sort_signal(val)] = '4'
            elif len(val) == 7:
                signal_dict[sort_signal(val)] = '8'
            else:
                undet.append(val)
        # 9 contains all of 4 and is len 6
        signal_9 = next(filter(
            lambda x: len(x) == 6 and signal_is_subset(
                get_signal_for_val(signal_dict, '4'), x), undet))
        signal_dict[sort_signal(signal_9)] = '9'
        undet.remove(signal_9)
        # 3 contains all of 1 and is len 5
        signal_3 = next(filter(
            lambda x: len(x) == 5 and signal_is_subset(
                get_signal_for_val(signal_dict, '1'), x), undet))
        signal_dict[sort_signal(signal_3)] = '3'
        undet.remove(signal_3)
        # 5 is contained by 9 and is len 5
        signal_5 = next(filter(
            lambda x: len(x) == 5 and signal_is_subset(
                x, get_signal_for_val(signal_dict, '9')), undet))
        signal_dict[sort_signal(signal_5)] = '5'
        undet.remove(signal_5)
        # 2 is the only len 5 signal remaining
        signal_2 = next(filter(lambda x: len(x) == 5, undet))
        signal_dict[sort_signal(signal_2)] = '2'
        undet.remove(signal_2)
        # 6 contains all of 5 and is len 6
        signal_6 = next(filter(
            lambda x: len(x) == 6 and signal_is_subset(
                get_signal_for_val(signal_dict, '5'), x), undet))
        signal_dict[sort_signal(signal_6)] = '6'
        undet.remove(signal_6)
        # 0 is the only len 6 signal remaining
        signal_0 = next(filter(lambda x: len(x) == 6, undet))
        signal_dict[sort_signal(signal_0)] = '0'
        undet.remove(signal_0)
        out_val = ''
        for val in output.split():
            out_val += signal_dict[sort_signal(val)]
        total_value += int(out_val)
    print(total_value)