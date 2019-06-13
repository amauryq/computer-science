#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    asn = 0
    for a in s[0:n]:
        if a == 'a':
            asn = asn + 1
    num, den = divmod(n, len(s))
    num = num * asn
    new_asn = 0
    for a in s[0:den]:
        if a == 'a':
            new_asn = new_asn + 1

    return num + new_asn

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
