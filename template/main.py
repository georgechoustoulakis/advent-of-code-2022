from typing import List, AnyStr


def read_file(name) -> List[AnyStr]:
    with open(name) as f:
        return [line.replace('\n', '') for line in f.readlines()]


def template():
    lines = read_file('example.txt')
    for line in lines:
        print(line)


if __name__ == '__main__':
    template()
