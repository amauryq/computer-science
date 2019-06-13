#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    count_a = 0
    for a in s:
        if a == 'a':
            count_a = count_a + 1
    num, den = divmod(n, len(s))
    num = num * count_a
    new_s = a[0:den]
    new_count_a = 0
    for a in new_s:
        if a == 'a':
            new_count_a = new_count_a + 1

    return num + new_count_a

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
