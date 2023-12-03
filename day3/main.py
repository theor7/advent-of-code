from functools import reduce


def find_whole_number(row, col, data):
    # search backwards
    while col > 0 and data[row][col].isnumeric():
        col -= 1

    digits = []
    col += not data[row][col].isnumeric()
    while col < len(data[row]) and data[row][col].isnumeric():
        digits.append(data[row][col])
        col += 1

    return int("".join(digits)), col


def search_around(row, col, data):
    matches = []

    for x in [row - 1, row, row + 1]:
        new_y = 0
        for y in [col - 1, col, col + 1]:
            if data[x][y].isnumeric() and y >= new_y:
                # we've found a number. we now need to find where it starts and ends
                # also bump the col number up so that we don't find the same number again
                found_num, new_y = find_whole_number(x, y, data)
                matches.append(found_num)
    return matches


def part_1(lines):
    total = 0
    for line_index, line in enumerate(lines):
        for char_index, char in enumerate(line):
            if char in ["!", "$", "%", "^", "&", "*", "=", "#", "/", "+", "-", "@"]:
                numbers_around = search_around(line_index, char_index, lines)
                total += reduce(lambda x, y: x + y, numbers_around)
    return total


if __name__ == "__main__":
    with open("input") as f:
        line_array = f.readlines()

    part1_total = part_1(line_array)
    print(f"Part 1 total = {part1_total}")
