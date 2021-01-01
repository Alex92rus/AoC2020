

def find_seat_id(line):
    min_row = 0
    max_row = 127
    for area in line[:7]:
        if area == 'B':
            min_row = (min_row + max_row) // 2
        if area == 'F':
            max_row = (min_row + max_row) // 2
    min_seat = 0
    max_seat = 7
    for seat in line[7:]:
        if seat == 'R':
            min_seat = (min_seat + max_seat) // 2
        if seat == 'L':
            max_seat = (min_seat + max_seat) // 2
    seat_id = max_row * 8 + max_seat
    return seat_id


def solve_part_one(filename):
    with open(filename, 'r+') as f:
        lines = f.read().splitlines()
    max_seat_id = 0
    for line in lines:
        seat_id = find_seat_id(line)
        if max_seat_id < seat_id:
            max_seat_id = seat_id
    return max_seat_id


def solve_part_two(filename):
    with open(filename, 'r+') as f:
        lines = f.read().splitlines()
    seat_ids = []
    for line in lines:
        seat_id = find_seat_id(line)
        seat_ids.append(seat_id)
    seat_ids.sort()
    for i in range(len(seat_ids)):
        if seat_ids[i] != seat_ids[i + 1] - 1:
            return seat_ids[i] + 1

if __name__ == '__main__':
    print('The max seat id is {}'.format(solve_part_one('day_5.txt')))
    print('The missing seat id is {}'.format(solve_part_two('day_5.txt')))
