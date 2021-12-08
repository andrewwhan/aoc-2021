import sys

class Board:
    def __init__(self, lines):
        self.bingo = {number:{'x':i, 'y':j, 'marked':False}
                for i, line in enumerate(lines)
                for j, number in enumerate(line.split())}

    def CheckWin(self, x, y):
        if len(list(filter(lambda number: number['x'] == x and 
            number['marked'], self.bingo.values()))) == 5:
                return True
        elif len(list(filter(lambda number: number['y'] == y and 
            number['marked'], self.bingo.values()))) == 5:
                return True
        else:
            return False

    def Mark(self, number):
        if number not in self.bingo.keys():
            return False
        else:
            self.bingo[number]['marked'] = True
            return self.CheckWin(self.bingo[number]['x'],
                self.bingo[number]['y'])

    def GetScore(self, number):
        unmarked = [int(x[0]) for x in filter(lambda number: not number[1]['marked'], self.bingo.items())]
        return sum(unmarked) * int(number)

if len(sys.argv) > 1:
    filename = sys.argv[1]
with open(filename) as f:
    lines = f.readlines()
    calls = lines[0].split(',')
    raw_boards = [x for x in lines[1:] if x != '\n']
    board_objs = []
    for i in range(int(len(raw_boards)/5)):
        board_objs.append(Board(raw_boards[i*5:(i+1)*5]))
    is_won = False
    while not is_won and calls:
        number = calls.pop(0)
        for board in board_objs:
            if board.Mark(number):
                is_won = True
                print(board.GetScore(number))
                