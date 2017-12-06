#!/usr/bin/python3
# lpoWeb.py by Barron Stone
# This is an exercise file from Python Code Clinic on lynda.com

from datetime import date
from urllib import request

__version__ = '0.3.2'

BASE_URL = 'http://lpo.dt.navy.mil/data/DM'       
             
def get_data_for_date(date):
    """
    Returns an generator object of data for the specified date.
    Output data is formatted as a dict.
    """
          
    # use correct accessor methods based on date
    if date.year < 2007:
        return _get_data_pre2007(date)
    else:
        return _get_data_post2006(date)
       
def _get_data_pre2007(date):
    """
    Access the LPO website to retrieve data for the specified date.
    For dates from 2002 to 2006, data is downloaded for the full year.
    The method operates as a generator object containing dictionaries
    with result data.
    """      
    
    # build the url based on year
    url = '{}/Environmental_Data_{}.txt'.format(BASE_URL, date.year)
    print('Fetching online data for {} (full year)'.format(date.year))
    
    try:
        year_data = request.urlopen(url).read().decode(encoding='utf_8').split('\n')            
    except:
        raise ValueError(date) # error accessing website
    else:
        year_data.pop(0) # remove first item which contain column header info
    
    for line in year_data:
        
        elements = line.split()
        yield dict(Date = elements[0],
           Time = elements[1],
           Status = 'COMPLETE', # all data from pre2007 will be complete
           Air_Temp = elements[5],
           Barometric_Press = elements[7],
           Wind_Speed = elements[2]) 

def _get_data_post2006(date):
    """
    Access the LPO website to retrieve data for the specified date.
    For dates after 2006, data is downloaded by individual days.
    The method operates as a generator object containing dictionaries
    with result data.
    """
    
    # build the url based on date & create data container
    url = '{}/{}/{}/'.format(BASE_URL, date.year, str(date).replace('-','_'))
    data = dict(Air_Temp = [], Barometric_Press = [], Wind_Speed = [])

    print('Fetching online data for {}'.format(date)) 
    for key in data.keys():
        try:
            data[key] = request.urlopen('{}{}'.format(url, key)).read().decode(encoding='utf_8').split('\r\n')
        except:
            raise ValueError(date) # error accessing website
        else:
            data[key].pop()  # remove last item which will be an empty string              

    # verify lengths of 3 files are equal
    lengths = []
    for k in data.keys():
        lengths.append(len(data[k]))
    if lengths[1:] != lengths[:-1]:
        raise ValueError(date) # file lengths do not match
            
    for i in range(len(data['Air_Temp'])):
        
        # verify timestamps are equal for every related entry in 3 files
        timestamps = []
        for k in data.keys():
            timestamps.append(data[k][i].split()[1])
        if timestamps[1:] != timestamps[:-1]:
            raise ValueError(date) # timestamps for fields do not line up
        
        yield dict(Date = data['Air_Temp'][i].split()[0],
                   Time = data['Air_Temp'][i].split()[1],
                   Status = 'PARTIAL' if date == date.today() else 'COMPLETE', # assume data from today is incomplete
                   Air_Temp = data['Air_Temp'][i].split()[2],
                   Barometric_Press = data['Barometric_Press'][i].split()[2],
                   Wind_Speed = data['Wind_Speed'][i].split()[2])

def _test():
    """
    A simple test routine
    """
    # look at data for today - tests _accessor_post2006
    for data in get_data_for_date(date.today()):
        print(data)
    
    # look at data for 2002 - tests _accessor_pre2007
    for data in get_data_for_date(date(2002,1,1)):
        print(data)
    
if __name__ == "__main__": _test()