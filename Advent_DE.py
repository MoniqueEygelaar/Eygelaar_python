import collections

with open('Day1.txt') as f:
    contents = f.read()

test = 'R2, L3'
#'['132_107', '135_107', '115_112', '111_110', '117_111', '116_120', '113_118', '111_118', '115_114', '116_122']'
def walk():
    vertical = 0
    horizontal = 0
    start = 'N'
    directions = []

    for move in contents.split(','):
        print(horizontal,vertical)
        removal = move.strip()
        if start == 'N':
            if removal.startswith('R'):
                horizontal += int(removal[1:])
                start = 'E'
                continue
            else:
                horizontal -= int(removal[1:])
                start = 'W'
                continue
        if start == 'E':
            if removal.startswith('R'):
                vertical -= int(removal[1:])
                start = 'S'
                continue
            else:
                vertical += int(removal[1:])
                start = 'N'
                continue
        if start == 'W':
            if removal.startswith('R'):
                vertical += int(removal[1:])
                start = 'N'
                continue
            else:
                vertical -= int(removal[1:])
                start = 'S'
                continue
        if start == 'S':
            if removal.startswith('R'):
                horizontal -= int(removal[1:])
                start = 'W'
                continue
            else:
                horizontal += int(removal[1:])
                start = 'E'
                continue

    print(horizontal,vertical)
    print(horizontal + vertical)
    print([item for item, count in collections.Counter(directions).items() if count > 1])
    #return horizontal,vertical


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    walk()

