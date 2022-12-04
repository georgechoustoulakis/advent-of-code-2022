from typing import List, AnyStr


def read_file(name) -> List[AnyStr]:
    with open(name) as f:
        return f.readlines()


def camp_cleanup():
    lines = read_file('input.txt')

    contained = 0
    overlap = 0

    for line in lines:
        trimmed = line.replace('\n', '')
        parts = trimmed.split(',')
        assert len(parts) == 2

        person_1 = [int(i) for i in parts[0].split('-')]
        person_2 = [int(i) for i in parts[1].split('-')]

        if person_1[0] >= person_2[0] and person_1[1] <= person_2[1] \
                or person_2[0] >= person_1[0] and person_2[1] <= person_1[1]:
            contained += 1

        # part 2
        range_1 = range(person_1[0], person_1[1] + 1, 1)
        range_2 = range(person_2[0], person_2[1] + 1, 1)
        if len(set(range_1) & set(range_2)):
            overlap += 1

    print(f'amount contained = {contained}')
    print(f'amount overlapped = {overlap}')


if __name__ == '__main__':
    camp_cleanup()
