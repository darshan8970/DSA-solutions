import math
import os
import random
import re
import sys
from datetime import datetime #required to use strptime
# Complete the time_delta function below.
def time_delta(t1, t2):

    time_format = "%a %d %b %Y %H:%M:%S %z" #formats for day, date, month & so on

    t1_val = datetime.strptime(t1, time_format) #Stores time in valid format
    t2_val = datetime.strptime(t2, time_format)

    diff_seconds = str(int(abs(t1_val-t2_val).total_seconds())) #Calculates difference
    
    return diff_seconds
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
