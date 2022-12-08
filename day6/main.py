from collections import Counter
from typing import List, AnyStr


def read_file(name) -> List[AnyStr]:
    with open(name) as f:
        return [line.replace('\n', '') for line in f.readlines()]


def signal_processing():
    lines = read_file('input.txt')
    length = 14
    for line in lines:
        for i in range(len(line)):
            counter = Counter(line[i:i+length])
            all_good = True
            for char, count in counter.items():
                if count > 1:
                    all_good = False
                    break
            if all_good:
                print(f'line {i+length}')
                break


if __name__ == '__main__':
    signal_processing()
