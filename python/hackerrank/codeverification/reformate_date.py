#!/bin/python3

import math
import os
import random
import re
import sys



#@author: r33 - r33ngin33r@gmail.com
#@timestamp_creation: 02/18/2019 - 18:44 GMT-3
#
# Complete the 'reformatDate' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY dates as parameter.
#


def reformatDate(dates):
    # Write your code here
    reformatted_dates = [] #List to be returned with the reformatted dates
    months = {'Jan':'01','Feb': '02', 'Mar':'03', 'Apr':'04', 'May':'05', 'Jun':'06', 'Jul':'07', 'Aug':'08', 'Sep':'09', 'Oct':'10','Nov':'11','Dec':'12'}
    date_pattern = "(\d?\d+)(\w+\w+)\s(\w+\w+\w+)\s(\d\d\d\d)"
    for date in dates:
        date_format = re.match(date_pattern,date)
        day = date_format.group(1)
        if len(day) < 2:
            day = '0' + day #Add a left zero in algarisms smaller ten
        month = months[date_format.group(3)] #months[date[-8:-5]]
        year = date_format.group(4) #date[-4:]

        date = year + '-' + month + '-' + day 
        reformatted_dates.append(date)

    return reformatted_dates

if __name__ == '__main__':
    os.environ['OUTPUT_PATH']='/tmp/output.txt'#ADDED
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    dates_count = int(input().strip())

    dates = []

    for _ in range(dates_count):
        dates_item = input()
        dates.append(dates_item)

    print(dates)

    result = reformatDate(dates)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
