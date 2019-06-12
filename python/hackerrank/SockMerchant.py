#!/bin/python3

import math
import os
import random
import re
import sys


ar = [10, 20, 20, 10, 10, 30, 50, 10, 20 ]

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    pairs_of_socks = 0
    existing_socks = []
    for color in ar:
        if color not in existing_socks:
            existing_socks.append(color)
        else:
            existing_socks.remove(color)
            pairs_of_socks = pairs_of_socks + 1
    return pairs_of_socks

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()