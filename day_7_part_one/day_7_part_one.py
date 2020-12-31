

def solve_part_one(filename: str):
    lines = get_file_content(filename)
    outmost_bags: set = set()
    current_outmost_bags: set = set()
    current_outmost_bags.add('shiny gold')
    while current_outmost_bags:
        next_layer = [set(parse_line(line) for line in lines if bag in line.split('contain')[1])
                      for bag in current_outmost_bags]
        current_outmost_bags = set(flatten(next_layer))
        outmost_bags = outmost_bags.union(current_outmost_bags)
    print('The different outmost bags that contain a shiny bag are: {}'.format(len(outmost_bags)))
    return len(outmost_bags)


def flatten(a_list):
    return [item for sublist in a_list for item in sublist]


def get_file_content(filename):
    with open(filename, 'r+') as f:
        return f.read().splitlines()


def parse_line(line: str):
    return line.split('contain')[0][:-6]


if __name__ == '__main__':
    solve_part_one('day_7_input.txt')