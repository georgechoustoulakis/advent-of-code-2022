from typing import List, AnyStr


def read_file(name) -> List[AnyStr]:
    with open(name) as f:
        return [line.replace('\n', '') for line in f.readlines()]


def tree_house():
    lines = read_file('input.txt')
    size = len(lines)
    count = 0
    for x, line in enumerate(lines):
        for y, char in enumerate(line):
            if y == 0 or y == size - 1 or x == 0 or x == size - 1:
                # Visible from the edge.
                count = count + 1
                continue

            if all(int(i) < int(char) for i in line[0:y]):
                count = count + 1
                # Visible from the left.
                continue
            if all(int(i) < int(char) for i in line[y + 1:size]):
                # Visible from the right.
                count = count + 1
                continue
            if all(int(lines[i][y]) < int(char) for i in range(0, x)):
                # Visible from the top.
                count = count + 1
                continue
            if all(int(lines[i][y]) < int(char) for i in range(x + 1, size)):
                # Visible from the bottom.
                count = count + 1
                continue
            # Not visible.

    print('count was', count)


def ideal_position():
    lines = read_file('input.txt')
    size = len(lines)
    highest_score = 0
    for x, line in enumerate(lines):
        for y, char in enumerate(line):
            left = 0
            # Look left.
            if y != 0:
                for i in line[0:y][::-1]:
                    left += 1
                    if int(i) >= int(char):
                        break
            right = 0
            # Look right.
            if y != size:
                for i in line[y + 1:size]:
                    right += 1
                    if int(i) >= int(char):
                        break
            top = 0
            # Look top.
            if x != 0:
                for i in reversed(range(0, x)):
                    top += 1
                    if int(lines[i][y]) >= int(char):
                        break
            down = 0
            # Look down.
            if x != 0:
                for i in range(x + 1, size):
                    down += 1
                    if int(lines[i][y]) >= int(char):
                        break
            score = left * right * top * down
            if score > highest_score:
                highest_score = score
    print(f'highest scenic score is {highest_score}')


if __name__ == '__main__':
    tree_house()
    ideal_position()
