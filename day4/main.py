from functools import reduce


def format_num_list(num_list):
    return num_list.replace("  ", " ").split(" ")


def find_num_won(line):
    [card_num, numbers] = line.split(": ")
    [winning, chosen] = numbers.strip().split(" | ")
    return len([x for x in format_num_list(chosen) if x in format_num_list(winning)]), card_num.split("d")[1].strip()


def part_1(lines):
    total = 0
    for line in lines:
        num_won = find_num_won(line)[0]
        total += bool(num_won) and 2 ** (num_won - 1)
    return total


def part_2(lines):
    number_of_cards = [1] * len(lines)

    for line in lines:
        [num_won, card_num] = find_num_won(line)

        for i in range(num_won):
            if int(card_num) < len(number_of_cards):
                number_of_cards[int(card_num) + i] += number_of_cards[int(card_num) - 1]

    return reduce(lambda x, y: x + y, number_of_cards)


if __name__ == "__main__":
    with open("input") as f:
        line_array = f.readlines()
    part_one_total = part_1(line_array)
    print(f"Part 1 total = {part_one_total}")

    part_two_total = part_2(line_array)
    print(f"Part 2 total = {part_two_total}")
