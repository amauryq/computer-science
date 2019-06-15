#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jumps = 0
    i = 0
    l = len(c)
    while i < l:
      if (i + 2 < l) and (c[i + 2] == 0):
        i = i + 2
        jumps = jumps + 1
      else:
        if (i + 1 < l) and (c[i + 1] == 0):
          i = i + 1
          jumps = jumps + 1
        else:
          i = i + 1
    return jumps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
