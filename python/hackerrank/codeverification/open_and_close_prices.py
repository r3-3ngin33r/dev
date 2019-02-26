#!/bin/python3

import sys
import os
from urllib.request import Request
from urllib.request import urlopen
from urllib.error import URLError
import json


'''
@author: r33 - r33ngin33r@gmail.com
@timestamp_creation: 02/19/2019 - 12:34 GMT-3
'''

# Complete the function below.
def  openAndClosePrices(firstDate, lastDate, weekDay):
    '''
    I 've chosen to write a function, even knowing there is a python built in package to deal with dates 
    and time, because the suggested packages imported in the template not include the aforementioned packages:
    date and datetime.
    '''
    def day_of_week(month, day, c_year):
        '''
        Calculate the day of the week for Gregorian calendar years. 
    
        Generic function that avoids leap year verifications and
        considers March 1st  as the first day of a Gregorian calendar year.
        (I assumed that it is not expected there be stock prices in the Julian calendar - 
        prior to 1752 in Great Britains and its domains or prior 1582 in other European territories.)
        source: https://cs.uwaterloo.ca/~alopez-o/math-faq/node73.html
    
        Args: 
        int: month
        int: day
        int: calendar_year
    
        Returns: 
        int: A value corresponding to the day of the week (0-6)
        '''
        if month > 2:
            month -= 2 #March will be treated as the fisrt month of the current Gregorian calendar year
        else:
            month += 10 #January and February will be treated like months of the last Gregorian calendar year
            c_year -= 1

        century = int(c_year / 100) #get the century from the calendar year
        year = c_year % 100 #get the last two algarisms of a year

        weekday = (day + int(month*2.6 - 0.2) - 2*century + year + int(year/4) + int(century/4)) % 7
        return weekday

    urlbase = 'https://jsonmock.hackerrank.com/api/stocks'
    weekdays = {0:'Sunday',1:'Monday', 2:'Tuesday', 3:'Wednesday',4:'Thursday',5:'Friday',6:'Saturday'}
    months = {'January':1,'February': 2, 'March':3, 'April':4, 'May':5, 'June':6, 'July':7, 'August':8,\
     'September':9, 'October':10,'November':11,'December':12}

    #Split the firstDate for comparisons
    year_firstDate = firstDate[-4:]
    month_firstDate = firstDate[(firstDate.find('-')+1):-5]
    day_firstDate = int(firstDate[:firstDate.find('-')])
    
    #Split the lastDate for comparisons
    year_lastDate = lastDate[-4:]
    month_lastDate = lastDate[(lastDate.find('-')+1):-5]
    day_lastDate = int(lastDate[:lastDate.find('-')])

    #Get the base number for the request list length: the difference, if it exists, between the years 
    years_diff = int(year_lastDate) - int(year_firstDate) 
    requests_list = [] # List of requests
    #Populate the list of HTTP requests
    for i in range(0, years_diff + 1):
        req = Request(urlbase + '/search?date='+ str(int(year_firstDate) + i))
        requests_list.append(req)

    responses_list = [] #List of responses
    #Populate a list of responses based on the list of HTTP requests
    for req in requests_list:
        res = urlopen(req)
        responses_list.append(res)

    json_list = [] #A JSON list with the data of each response
    #Populate the JSON list with the responses data
    for response in responses_list:
        data = response.read()
        encoding = response.info().get_content_charset('utf-8')
        load_decoded = json.loads(data.decode(encoding))
        json_list.append(load_decoded)

    #Iterate over the JSON data list
    for i in range(0, len(json_list)):
        for d in json_list[i]['data']:
            year = int(d['date'][-4:])
            month = months[d['date'][(d['date'].find('-')+1):-5]]
            day = int(d['date'][:d['date'].find('-')])
            
            #Check the boundaries of the firstDate
            if(year == int(year_firstDate)):
                #Check if a month in the year of firstDate deserves to be ignored
                if(month < months[month_firstDate]):
                    continue
                #Check if a day in the month of firstDate deserves to be ignored
                if(month == months[month_firstDate]) and (day < day_firstDate):
                    continue
            #Check the boundaries of the lastDate        
            if(year == int(year_lastDate)):
                #Check if a month in the year of lastDate deserves to be ignored
                if(month > months[month_lastDate]):
                    continue
                #Check if a day in the month of lastDate deserves to be ignored
                if(month == months[month_lastDate]) and (day > day_lastDate):
                    continue
            #Check the main constraint about the day of the week
            if(  (weekdays[day_of_week(month,day,year)] == weekDay) ):
                print("{} {} {}".format(d['date'], d['open'], d['close']))

'''
try:
    _firstDate = str(input())
except:
    _firstDate = None


try:
    _lastDate = str(input())
except:
    _lastDate = None


try:
    _weekDay = str(input())
except:
    _weekDay = None
'''
if __name__ == "__main__":
    #"1-January-2000", "22-February-2000", "Monday"
    #
    #"26-March-2001","15-August-2001","Wednesday"
    openAndClosePrices("26-May-2001", "15-February-2003","Tuesday")
