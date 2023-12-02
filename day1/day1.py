#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
On each line, the calibration value can be found by combining the first digit and the last digit (in that order) 
to form a single two-digit number.
"""

import re

line = 'nkzjrdqrmpztpqninetwofour1znnkd'

total = 0
with open('day1.txt') as file:
    for line in file.readlines():
        numbers = re.findall(r'\d', line)
        total += int(numbers[0] + numbers[-1])
print (total)
