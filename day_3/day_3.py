from functools import reduce

def get_file_content(filename):
    with open(filename, 'r+') as f:
        return f.read().splitlines()

def slide(right, down, lines):
    rows, columns, trees = 0, 0, 0
    while rows < len(lines):
        columns = (columns + right) % len(lines[0])
        rows += down
        if rows >= len(lines):
            break
        if lines[rows][columns] == '#':
            trees += 1
    return trees


def solve_part_one(filename='day_3.txt'):
    slope = get_file_content(filename)
    print('The number of trees when sloping 3 to the right and one forwards is {}'.format(slide(3, 1, slope)))


def solve_part_two(filename='day_3.txt'):
    slope = get_file_content(filename)
    slides = [slide(1, 1, slope),
              slide(3, 1, slope),
              slide(5, 1, slope),
              slide(7, 1, slope),
              slide(1, 2, slope)]
    print('Multiply all slides to get the answer for part 2 {}'.format(reduce((lambda x, y: x * y), slides)))


if __name__ == '__main__':
    solve_part_one()
    solve_part_two()
