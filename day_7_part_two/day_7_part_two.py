import re


def solve_part_two(filename):
    lines = get_file_content(filename)
    graph: dict = {}
    for line in lines:
        node, neighbours = parse_line(line)
        graph[node] = neighbours
    number_of_successors = process_successors_of('shiny gold', graph)
    print('A single shiny gold bag must contain {}'.format(number_of_successors))


def process_successors_of(node: str, graph: dict):
    result = 0
    for neighbour in graph[node]:
        factor = int(neighbour[0])
        result += factor + factor * process_successors_of(neighbour[1], graph)
    return result


def get_file_content(filename: str):
    with open(filename, 'r+') as f:
        return f.read().splitlines()


def parse_line(line: str):
    node_and_edges = line.split(' bags contain ')
    node = node_and_edges[0]
    if node_and_edges[1] == 'no other bags.':
        return node, []
    edges = re.split(' (?:bags|bag)(?:, |\.)', node_and_edges[1])[:-1]
    edges = [(edge.split(maxsplit=1)[0], edge.split(maxsplit=1)[1]) for edge in edges]
    return node, edges


if __name__ == '__main__':
    solve_part_two('day_7_input.txt')
