#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
On each line, the calibration value can be found by combining the first digit and the last digit (in that order) 
to form a single two-digit number.
"""

import re

# Part 1
total = 0
with open("day1.txt") as file:
    for line in file.readlines():
        numbers = re.findall(r"\d", line)
        total += int(numbers[0] + numbers[-1])

print(f"Part 1 calibration value = {total}")

# Part 2
total = 0
number_map = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

with open("day1.txt") as file:
    for line in file.readlines():
        # use lookahead to allow for overlaps
        numbers = re.findall(
            r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))", line
        )
        for i, number in enumerate([numbers[0], numbers[-1]]):
            if not number.isnumeric():
                numbers[i * -1] = number_map[number]
        total += int(numbers[0] + numbers[-1])

print(f"Part 2 calibration value = {total}")
