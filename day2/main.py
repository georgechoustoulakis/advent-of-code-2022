from enum import Enum


def read_file(name):
    with open(name) as f:
        return f.readlines()


class Result(Enum):
    WIN = 1
    DRAW = 2
    LOSE = 3


def rock_paper_scissors():
    lines = read_file('input.txt')
    # rock = A | X
    # paper = B | Y
    # scissors = C | Z
    score = 0
    for line in lines:
        result = Result.DRAW
        opponent = line[0]
        selected = line[2]
        if opponent == 'A':
            if selected == 'Y':
                result = Result.WIN
            elif selected == 'Z':
                result = Result.LOSE
        elif opponent == 'B':
            if selected == 'Z':
                result = Result.WIN
            elif selected == 'X':
                result = Result.LOSE
        elif opponent == 'C':
            if selected == 'X':
                result = Result.WIN
            elif selected == 'Y':
                result = Result.LOSE

        if result == Result.WIN:
            score += 6
        elif result == Result.DRAW:
            score += 3

        if selected == 'X':
            score += 1
        elif selected == 'Y':
            score += 2
        elif selected == 'Z':
            score += 3
    print(f'the score with this strategy is {score}')


def rock_paper_scissors_part_2():
    lines = read_file('input.txt')
    # rock = A
    # paper = B
    # scissors = C
    score = 0
    for line in lines:
        result = Result.DRAW
        opponent = line[0]
        required_result = line[2]
        selected = ''

        if required_result == 'X':
            result = Result.LOSE
        elif required_result == 'Z':
            result = Result.WIN

        if result == Result.DRAW:
            selected = opponent
        elif opponent == 'A':
            if result == Result.WIN:
                selected = 'B'
            elif result == Result.LOSE:
                selected = 'C'
        elif opponent == 'B':
            if result == Result.WIN:
                selected = 'C'
            elif result == Result.LOSE:
                selected = 'A'
        elif opponent == 'C':
            if result == Result.WIN:
                selected = 'A'
            elif result == Result.LOSE:
                selected = 'B'

        if result == Result.WIN:
            score += 6
        elif result == Result.DRAW:
            score += 3

        if selected == '':
            raise Exception('Try again idiot.')
        elif selected == 'A':
            score += 1
        elif selected == 'B':
            score += 2
        elif selected == 'C':
            score += 3

    print(f'the score with part 2 is {score}')


if __name__ == '__main__':
    rock_paper_scissors()
    rock_paper_scissors_part_2()
