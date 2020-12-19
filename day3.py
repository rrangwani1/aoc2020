import numpy as np

with open("day3input.txt") as f:
    content = f.readlines()
content = [list(x.strip()) for x in content]


def part1():
    pos = 0
    trees = 0

    for row in content:
        tree = "#"
        slope = "."

        #print(str(pos))
        if row[pos] == tree:
            trees += 1

        pos += 3
        if pos >= 31:
            pos -= 31

    return trees


def part2():
    movement = [
        [1,1],
        [3,1],
        [5,1],
        [7,1],
        [1,2]
    ]
    tree_list = []

    for traversal in movement:
        right = traversal[0]
        down = traversal[1]
        down_count = len(content)
        down_pos = 0

        pos = 0
        trees = 0
        tree = "#"
        slope = "."

        while down_pos < down_count:
            if content[down_pos][pos] == tree:
                trees += 1

            pos += right
            if pos >= 31:
                pos -= 31

            down_pos += down

        tree_list.append(trees)
    print(tree_list)
    return np.prod(tree_list)




if __name__ == "__main__":
    print(part1())
    print(part2())