import re

maps = {}


def get_seeds(input_str):
    match = re.search(r"^seeds: (.*?)$", input_str).group(1)
    return [int(x) for x in match.split(" ")]


def parse_maps(map_block):
    map_entries = []
    map_name = ""
    for i, line in enumerate(map_block.split("\n")):
        line_data = line.split(" ")
        if i == 0:
            map_name = line_data[0]
        else:
            map_entries.append(
                {
                    "start": int(line_data[1]),
                    "end": int(line_data[1]) + int(line_data[2]),
                    "modifier": int(line_data[0]) - int(line_data[1]),
                }
            )

    map_name_split = map_name.split("-to-")
    maps[map_name_split[0]] = {
        "to": map_name_split[1],
        "entries": map_entries,
    }


def follow_map(start, end, cur_val):
    map_name = start

    while map_name != end:
        farm_map = maps[map_name]
        for map_entry in farm_map["entries"]:
            if map_entry["start"] <= cur_val < map_entry["end"]:
                cur_val += map_entry["modifier"]
                break

        map_name = farm_map["to"]

    return cur_val


def part_1(input_str):
    seeds = []
    for i, block in enumerate(input_str.strip().split("\n\n")):
        if i == 0:
            seeds = get_seeds(block)
        else:
            parse_maps(block)

    locations = []
    for seed in seeds:
        locations.append(follow_map("seed", "location", seed))

    return min(locations)


if __name__ == "__main__":
    with open("input") as f:
        text_input = f.read()

    part_1_res = part_1(text_input)
    print(f"Part one result = {part_1_res}")
