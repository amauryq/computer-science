#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    see_level = 0
    valley = 0
    for step in s:
        if step == 'U':
            see_level = see_level + 1
            if see_level == 0:
                valley = valley + 1
        elif step == 'D':
            see_level = see_level - 1
    return valley
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
