from typing import List, AnyStr


def read_file(name) -> List[AnyStr]:
    with open(name) as f:
        return f.readlines()


def template():
    lines = read_file('example.txt')
    for line in lines:
        trimmed = line.replace('\n', '')
        print(trimmed)


if __name__ == '__main__':
    template()
