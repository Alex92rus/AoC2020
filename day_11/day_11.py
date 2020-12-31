def game_of_life(previous_state, state, empty_token, occupied_token, no_change, skips_paths, seats):
    for i in range(1, len(state) - 1):
        for j in range(1, len(state[0]) - 1):
            neighbours = 0
            for k in range(i - 1, i + 2):
                for n in range(j - 1, j + 2):
                  if k != i or n != j and previous_state[i][j] in [empty_token, occupied_token]:
                      direction_token = find_token(previous_state, i, j, k, n, empty_token, occupied_token, no_change, skips_paths)
                      if direction_token == occupied_token:
                          neighbours += 1
            if previous_state[i][j] != no_change:
                if neighbours >= seats:
                    state[i][j] = empty_token
                if neighbours == 0:
                    state[i][j] = occupied_token
    return state


def find_token(previous_state, i, j, k, n, empty_token, occupied_token, no_change, skips_paths):
    incr_i = k - i
    incr_j = n - j
    i = i + incr_i
    j = j + incr_j
    if not skips_paths:
        return previous_state[i][j]
    while 0 <= i < len(previous_state) and 0 <= j < len(previous_state[i]):
        if previous_state[i][j] in [empty_token, occupied_token]:
            return previous_state[i][j]
        j = j + incr_j
        i = i + incr_i
    return no_change


def plane_seating(initial_seating, seats, skip_paths=False):
    current_seating = initial_seating
    occupied = 0
    iteration = 0
    while True:
        import copy
        previous = copy.deepcopy(current_seating)
        if skip_paths:
            print('part2: {}'.format(iteration))
            iteration += 1
        current_seating = game_of_life(previous, current_seating, 'L', '#', '.', skip_paths, seats=seats)
        if current_seating == previous:
            occupied = sum([sum([1 if x == '#' else 0 for x in row]) for row in current_seating])
            break
        print_seating(current_seating, iteration)  # Prints the seating grid on every iteration.
    return occupied


def print_seating(current_seating, iteration):
    print('Seating after iteration {}'.format(iteration))
    for row in current_seating:
        for seat in row:
            print(seat, end='')
        print()


def parse_input(filename):
    lines = get_file_content(filename)
    return create_dp_grid(lines)


def create_dp_grid(lines):
    grid = [['.' for i in range(len(lines[0]) + 2)] for j in range(len(lines) + 2)]
    for i in range(1, len(lines) + 1):
        for j in range(1, len(lines[0]) + 1):
            grid[i][j] = lines[i - 1][j - 1]
    return grid


def get_file_content(filename):
    with open(filename, 'r+') as f:
        return f.read().splitlines()


def solve_part_one(filename):
    parsed_input = parse_input(filename)
    print('The number of occupied seats for part one is {}'.format(plane_seating(parsed_input, 4)))


def solve_part_two(filename):
    parsed_input = parse_input(filename)
    print('The number of occupied seats for part two is {}'.format(plane_seating(parsed_input, 5, skip_paths=True)))


if __name__ == '__main__':
    solve_part_one('day_11_input.txt')
    solve_part_two('day_11_input.txt')