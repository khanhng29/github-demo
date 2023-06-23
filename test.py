
import math
import os
import random
import re
import sys


def diagonalDifference(arr):
    # Write your code here
    n = len(arr)
    difference = 0
    i = 0
    lr = 0
    rl = 0
    while i < len(arr):
        lr += arr[i][i]
        rl += arr[i][n-1]
        i += 1
        n -= 1

    difference = abs(lr-rl)
    return difference


if __name__ == '__main__':

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    print(result)
