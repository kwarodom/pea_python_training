#!/usr/bin/python3
# lpoWeb.py by Barron Stone
# This is an exercise file from Python Code Clinic on lynda.com

from datetime import date
from urllib import request
import csv
import sys

__version__ = '0.3.2'

BASE_URL = 'http://lpo.dt.navy.mil/data/DM'       
             
def get_data_for_date(date):
    """
    Returns an generator object of data for the specified date.
    Output data is formatted as a dict.
    """
          
    # use correct accessor methods based on date
    if date.year < 2007:
        print('_get_data_pre2007(date)')
        return _get_data_pre2007(date)
    else:
        print('_get_data_post2006(date)')
        return _get_data_post2006(date)
       
def _get_data_pre2007(date):
    """
    Access the LPO website to retrieve data for the specified date.
    For dates from 2002 to 2006, data is downloaded for the full year.
    The method operates as a generator object containing dictionaries
    with result data.
    """

    f = open('data/Environmental_Data_Deep_Moor_2012.csv', 'r')
    reader = csv.reader(f)
    timestamp = []
    air_temp = []
    barometric_press = []
    dew_point = []
    relative_humidity = []
    wind_dir = []
    wind_gust = []
    wind_speed = []
    for row in reader:
        timestamp.append(row[0])
        air_temp.append(row[1])
        barometric_press.append(row[2])
        dew_point.append(row[3])
        relative_humidity.append(row[4])
        wind_dir.append(row[5])
        wind_gust.append(row[6])
        wind_speed.append(row[7])

    for i in range(len(timestamp)):
        # verify timestamps are equal for every related entry in 3 files
        time = timestamp[i].split(' ')[0].split('_')
        s = "-"
        seq = (time[0], time[1], time[2])  # This is sequence of strings.
        if (s.join(seq) == str(date)):
            yield dict(Date=timestamp[i].split(' ')[0],
                       Time=timestamp[i].split(' ')[1],
                       Status='COMPLETE',  # assume data from today is incomplete
                       Air_Temp=air_temp[i],
                       Barometric_Press=barometric_press[i],
                       Wind_Speed=wind_speed[i])

def _get_data_post2006(date):
    """
    Access the LPO website to retrieve data for the specified date.
    For dates after 2006, data is downloaded by individual days.
    The method operates as a generator object containing dictionaries
    with result data.
    """
    f = open('data/Environmental_Data_Deep_Moor_2012.csv', 'r')
    reader = csv.reader(f)
    timestamp = []
    air_temp = []
    barometric_press = []
    dew_point = []
    relative_humidity = []
    wind_dir = []
    wind_gust = []
    wind_speed = []
    for row in reader:
        timestamp.append(row[0])
        air_temp.append(row[1])
        barometric_press.append(row[2])
        dew_point.append(row[3])
        relative_humidity.append(row[4])
        wind_dir.append(row[5])
        wind_gust.append(row[6])
        wind_speed.append(row[7])

    for i in range(len(timestamp)):
        # verify timestamps are equal for every related entry in 3 files
        time = timestamp[i].split(' ')[0].split('_')
        s = "-"
        seq = (time[0], time[1], time[2])  # This is sequence of strings.
        if (s.join(seq) == str(date)):
            yield dict(Date=timestamp[i].split(' ')[0],
                       Time=timestamp[i].split(' ')[1],
                       Status='COMPLETE',  # assume data from today is incomplete
                       Air_Temp=air_temp[i],
                       Barometric_Press=barometric_press[i],
                       Wind_Speed=wind_speed[i])

def _test():
    """
    A simple test routine
    """
    # look at data for today - tests _accessor_post2006
    # for data in get_data_for_date(date.today()):
    #     print(data)
    
    # look at data for 2002 - tests _accessor_pre2007
    for data in get_data_for_date(date(2012,1,1)):
        print(data)
    
if __name__ == "__main__": _test()