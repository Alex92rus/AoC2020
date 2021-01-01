

def solve_part_one(filename):
    with open(filename, 'r+') as f:
        lines = f.read().splitlines()
    person_sets = []
    answers = 0
    for line in lines:
        if len(line) < 1:
            answers += len(set.union(*person_sets))
            person_sets = []
        else:
            current_answers = set()
            for letter in line:
                current_answers.add(letter)
            person_sets.append(current_answers)
    return answers + len(set.union(*person_sets))


def solve_part_two(filename):
    with open(filename, 'r+') as f:
        lines = f.read().splitlines()
    person_sets = []
    answers = 0
    for line in lines:
        if len(line) < 1:
            answers += len(set.intersection(*person_sets))
            person_sets = []
        else:
            current_answers = set()
            for letter in line:
                current_answers.add(letter)
            person_sets.append(current_answers)
    return answers + len(set.intersection(*person_sets))


if __name__ == '__main__':
    print('The number of questions to which anyone answered per group is {}'.format(solve_part_one('day_6.txt')))
    print('The number of questions to which everyone answered per group is {}'.format(solve_part_two('day_6.txt')))