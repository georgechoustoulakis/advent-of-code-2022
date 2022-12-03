from typing import List, AnyStr


def read_file(name) -> List[AnyStr]:
    with open(name) as f:
        return f.readlines()


def calculate_priority(item: str):
    if item.isupper():
        return ord(item) - 38
    else:
        return ord(item) - 96


def rucksacks_part_1():
    rucksacks = read_file('input.txt')
    score = 0
    for rucksack in rucksacks:
        trimmed = rucksack.replace('\n', '')
        half = int(len(trimmed) / 2)
        first_compartment, second_compartment = trimmed[:half], trimmed[half:]
        common_items = list(set(first_compartment) & set(second_compartment))
        priority = calculate_priority(common_items[0])
        score += priority

    print(f'the sum of priorities is {score}')


def split_in_groups_of_n(list, n):
    return [list[i:i + n] for i in range(0, len(list), n)]


def rucksacks_part_2():
    rucksacks = read_file('input.txt')
    score = 0
    grouped_per_3 = split_in_groups_of_n(rucksacks, 3)
    for group in grouped_per_3:
        first = group[0].replace('\n', '')
        second = group[1].replace('\n', '')
        third = group[2].replace('\n', '')
        common_items = list(set(first) & set(second) & set(third))
        priority = calculate_priority(common_items[0])
        score += priority

    print(f'the sum of badge priorities is {score}')


if __name__ == '__main__':
    rucksacks_part_1()
    rucksacks_part_2()
