from typing import List, AnyStr


def read_file(name) -> List[AnyStr]:
    with open(name) as f:
        return f.readlines()


def supply_stacks():
    lines = read_file('input.txt')
    trimmed = [line.replace('\n', '') for line in lines]

    indexes_row = next(item for item in trimmed if item.startswith(' 1'))
    reference = trimmed.index(indexes_row)
    stack_rows = trimmed[:reference]
    action_rows = trimmed[reference + 2:]

    indexes_length = len(indexes_row.replace(' ', ''))
    stacks = [[] for _ in range(indexes_length)]

    for stack in range(indexes_length):
        for row in reversed(stack_rows):
            try:
                value = row[stack * 4 + 1]
            except IndexError:
                break
            if value == ' ':
                break
            else:
                stacks[stack].append(value)

    split_action_rows = [row.split(' ') for row in action_rows]
    for action in split_action_rows:
        amount = int(action[1])
        source = int(action[3]) - 1
        destination = int(action[5]) - 1

        # part 1
        # for _ in range(amount):
        #     stacks[destination].append(stacks[source].pop())

        # part 2
        items_to_move = []
        for _ in range(amount):
            items_to_move.append(stacks[source].pop())
        for item in reversed(items_to_move):
            stacks[destination].append(item)

    stacks_on_top = ''
    for stack in stacks:
        stacks_on_top += stack[len(stack) - 1]
    print(stacks_on_top)


if __name__ == '__main__':
    supply_stacks()
