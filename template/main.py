from typing import List, AnyStr


def read_file(name) -> List[AnyStr]:
    with open(name) as f:
        return f.readlines()


def template():
    lines = read_file('example.txt')
    trimmed = [line.replace('\n', '') for line in lines]
    for line in trimmed:
        print(line)


if __name__ == '__main__':
    template()
