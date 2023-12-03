from functools import reduce

max_cubes = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def part_1(file):
    total = 0
    for line in file.readlines():
        [game_id, data] = line.split(": ")
        sets = data.split("; ")
        game_id = int(game_id.split(" ")[1])

        for colour_set in sets:
            colours = colour_set.split(", ")
            for colour_data in colours:
                [number, colour] = colour_data.strip().split(" ")

                if int(number) > max_cubes[colour]:
                    game_id = 0  # game invalidated

        total += game_id
    return total


def part_1_v2(file):
    # let's have a bit of fun with list comprehension
    total = 0
    for line in file.readlines():
        # sorry if you wanted to read this
        total += (not [x for y in [z.split(", ") for z in line.split(": ")[1].split("; ")] for x in y if int(x.split(" ")[0]) > max_cubes[x.strip().split(" ")[1]]]) * int(line.split(": ")[0].split(" ")[1])
    return total


def part_2(file):
    total = 0
    for line in file.readlines():
        high = {"red": 0, "blue": 0, "green": 0}
        sets = line.split(": ")[1].split("; ")
        for colour_set in sets:
            colours = colour_set.split(", ")
            for colour_data in colours:
                [number, colour] = colour_data.strip().split(" ")

                if int(number) > high[colour]:
                    high[colour] = int(number)

        total += reduce(lambda x, y: x * y, high.values())
    return total


if __name__ == "__main__":
    with open("input") as f:
        part1_total = part_1(f)
        print(f"Part 1 total = {part1_total}")

        f.seek(0)
        part_1_v2_total = part_1_v2(f)
        print(f"Part 1 v2 total = {part_1_v2_total}")

        f.seek(0)
        part_2_total = part_2(f)
        print(f"Part 2 total = {part_2_total}")
