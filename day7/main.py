from typing import List, AnyStr


def read_file(name) -> List[AnyStr]:
    with open(name) as f:
        return [line.replace('\n', '') for line in f.readlines()]


total_under_100k = 0

minimal_needed = None
small_enough_dirs = []


class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.files = []
        self.dirs = []
        self.total_size = None

    def find_dir_with_name(self, name):
        for directory in self.dirs:
            if directory.name == name:
                return directory
        raise 'No dir found'

    def print_directory(self, previous_tab=''):
        print(f'{previous_tab}- {self.name} (dir)')
        tab = previous_tab + '  '
        for file in self.files:
            print(f'{tab}- {file.name} (file, size={file.size})')
        for directory in self.dirs:
            directory.print_directory(tab)

    def calculate_totals(self) -> int:
        global total_under_100k
        global small_enough_dirs
        total = 0
        for file in self.files:
            total += file.size
        for directory in self.dirs:
            total += directory.calculate_totals()
        if total <= 100000:
            total_under_100k += total
        self.total_size = total
        return self.total_size

    def calculate_minimal_file_to_delete(self):
        global minimal_needed
        if minimal_needed is not None:
            if self.total_size >= minimal_needed:
                small_enough_dirs.append(self.total_size)
        for directory in self.dirs:
            directory.calculate_minimal_file_to_delete()


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size


def find_space():
    global total_under_100k
    global minimal_needed
    lines = read_file('input.txt')
    root = Directory('root', None)
    current_dir = root
    for line in lines:
        parts = line.split(' ')
        if parts[0] == '$':
            if parts[1] == 'cd':
                if parts[2] == '..':
                    current_dir = current_dir.parent
                elif parts[2] == '/':
                    pass
                else:
                    current_dir = current_dir.find_dir_with_name(parts[2])
        elif parts[0] == 'dir':
            current_dir.dirs.append(Directory(parts[1], current_dir))
        else:
            current_dir.files.append(File(parts[1], int(parts[0])))

    # part 1
    root.print_directory()
    root.calculate_totals()
    print('total sizes under 100k', total_under_100k)

    # part 2
    minimal_needed = 30000000 - (70000000 - root.total_size)
    root.calculate_minimal_file_to_delete()
    print('smallest_dir', min(small_enough_dirs))


if __name__ == '__main__':
    find_space()
