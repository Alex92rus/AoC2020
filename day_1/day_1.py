from collections import defaultdict


def get_file_content(filename):
    with open(filename, 'r+') as f:
        return f.read().splitlines()

def solve_part_one(lines):
    complement = defaultdict(int)
    for i in range(len(lines)):
        complement[parse_line(i, lines)] = 1

    for i in range(len(lines)):
        second_number = parse_line(i, lines)
        if complement[2020 - second_number] == 1 and second_number != 1010:
            print('The multiplication of the three sum is {}'
                  .format((2020 - second_number) * second_number))
            break

def solve_part_two(lines):
    for i in range(len(lines)):
        complement = defaultdict(int)
        target = 2020 - parse_line(i, lines)
        for j in range(i + 1, len(lines)):
            if complement[target - parse_line(j, lines)] == 1:
                print('The multiplication of the three sum is {}'
                      .format(parse_line(i, lines) * (target - parse_line(j, lines)) * parse_line(j, lines)))
                break
            else:
                complement[parse_line(j, lines)] = 1


def parse_line(i, lines):
    return int(lines[i])


if __name__ == '__main__':

    lines = get_file_content('day_1.txt')
    solve_part_one(lines)
    solve_part_two(lines)