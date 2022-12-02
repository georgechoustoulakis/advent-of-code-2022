def read_file(name):
    with open(name) as f:
        return f.readlines()


def template():
    lines = read_file('example.txt')
    print(lines)


if __name__ == '__main__':
    template()
