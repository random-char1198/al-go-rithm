#!/bin/python3

import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    x = 0
    y = 0
    length = len(arr)# This will return the length of the array
    for i in range(length):
        x += arr[i][i]#(0,0),(1,1),(2,2)...
        y += arr[i][length-1]#(0,2),(1,1),(2,0)
        length -=1
    return(abs(x-y))
