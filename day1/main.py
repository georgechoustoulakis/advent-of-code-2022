from utils import *


def highest_calories():
    lines = read_file('input.txt')
    sums = [0]
    index = 0
    for line in lines:
        if line == '\n':
            index = index + 1
            sums.append(0)
        else:
            sums[index] += int(line)
    print(f'highest calories is {max(sums)}')

    top_3 = sorted(sums)[len(sums) - 3:]
    print(f'top 3 together are {sum(top_3)}')


if __name__ == '__main__':
    highest_calories()
