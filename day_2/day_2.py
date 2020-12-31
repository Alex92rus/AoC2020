

def process_policy(policy, password_rows):
    valid = 0
    for password_row in password_rows:
        splitted_password_row = password_row.split()
        low, up = splitted_password_row[0].split('-')
        character = splitted_password_row[1][:-1]
        password = splitted_password_row[2]
        if policy(low, up, character, password):
            valid += 1
    return valid


def get_file_content(filename):
    with open(filename, 'r+') as f:
        return f.read().splitlines()


def solve_part_two(password_rows):
    policy_two = lambda low, up, character, password: (password[int(low) - 1] == character) != (
                password[int(up) - 1] == character)
    print('the valid passwords against the second policy are {}'.format(process_policy(policy_two, password_rows)))


def solve_part_one(password_rows):
    policy_one = lambda low, up, character, password: int(low) <= len([x for x in password if x == character]) <= int(
        up)
    print('the valid passwords against the first policy are {}'.format(process_policy(policy_one, password_rows)))


if __name__ == '__main__':
    password_rows = get_file_content('day_2.txt')
    solve_part_one(password_rows)
    solve_part_two(password_rows)