#!/bin/python3

import math
import os
import random
import re
# Given a time in -hour AM/PM format, convert it to military (24-hour) time.

# Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
# - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

import sys

# *********************************** #

def timeConversion(s):
    # Write your code here
    # 07:05:45PM last second index is 'PM'
    ampm = s[-2:]
    if ampm == 'PM':
        # 07:05:45PM index from starting to second '07'
        if s[:2] == '12':
            return s[:8]
        return f"{int(s[:2]) + 12}{s[2:8]}"
    
    if ampm == 'AM':
        if s[:2] != '12':
            return s[:8]
        return f"{int(s[:2]) - 12:02d}{s[2:8]}"

#  *************************************** #

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
