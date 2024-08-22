
import math
import os
import random
import re
import sys

#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#
ans=1
def extraLongFactorials(n):
    global ans
    if(n>0):
        ans=ans*n
        extraLongFactorials(n-1)
    else:
        print(ans)
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())
    extraLongFactorials(n)
