#!/usr/bin/python3
# lpoDB.py by Barron Stone
# This is an exercise file from Python Code Clinic on lynda.com

from datetime import date, datetime, timedelta
from tkinter import messagebox
import sqlite3
import lpoWeb

__version__ = '0.3.2'

class lpoDB():
    """
    A database to keep track of Wind Speed, Air Temperature,
    and Barometric Pressure for specific dates.
    """

    def __init__(self, **kwargs):       

        self.filename = kwargs.get('filename', 'lpo.db')
        self.table = kwargs.get('table', 'Weather')
        
        self.db = sqlite3.connect(self.filename)
        self.db.row_factory = sqlite3.Row        
        self.db.execute('''CREATE TABLE IF NOT EXISTS {}
                            (Date TEXT, Time TEXT, Status TEXT,
                            Air_Temp FLOAT, Barometric_Press FLOAT,
                            Wind_Speed FLOAT)'''.format(self.table))
                  
    def __iter__(self):
        """
        Return generator object with dicts of entire DB contents
        """
        cursor = self.db.execute('SELECT * FROM {} ORDER BY Date, Time'.format(self.table))
        for row in cursor: yield dict(row)
       
    def get_data_for_range(self, start, end):
        """
        Given a start and end date, return a generator of dicts
        containing all available Air_Temp, Barometric_Press, and Wind_Speed values.
        NOTE - It updates the database as necessary first.
        """
        
        dates_to_update = []
        
        # determine pre-2007 dates to update and append to list
        for year in range(start.year, 2007):
            if list(self._get_status_for_range(date(year,1,12), date(year,1,12))) == []:
                dates_to_update.append(date(year,1,12))
        
        # determine post-2006 dates to update and append to list        
        if (end.year > 2006) and (start >= date(2007,1,1)):
            temp_start = start
        elif (end.year > 2006) and (start < date(2007,1,1)):
            temp_start = date(2007,1,1)
        else: # start and end are both pre-2007
            temp_start = end
        
        # generate a list of dates between temp_start and end
        delta = end - temp_start         
        for d in range(delta.days + 1): # the +1 makes it inclusive
            dates_to_update.append(temp_start + timedelta(days=d))
    
        statuses = list(self._get_status_for_range(temp_start, end))
        
        # remove all dates from dates_to_update that have a completed or partial status
        for entry in statuses:
            if entry['Status'] == 'COMPLETE':
                dates_to_update.remove(datetime.strptime(str(entry['Date']), '%Y%m%d').date())
            elif entry['Status'] == 'PARTIAL':              
                try: # update for any new data first, then remove from dates_to_update list
                    self._update_data_for_date(datetime.strptime(str(entry['Date']), '%Y%m%d').date(), True)
                except:
                    raise
                dates_to_update.remove(datetime.strptime(str(entry['Date']), '%Y%m%d').date())  
            
        # iterate through dates that were non-existent in DB and insert data
        error_dates = []
        for day in dates_to_update:
            try:  
                self._update_data_for_date(day, False)
            except ValueError as e:
                error_dates.append(e)

        if error_dates != []:
            error_message = 'There were problems accessing data for the following dates.  They were not included in the result.\n'
            for day in error_dates:
                error_message += '\n{}'.format(day)
            messagebox.showwarning(title = 'Warning', message = error_message) 
                  
        # get Air_Temp, Barometric_Press, and Wind_Speed data from specified start/end date range
        cursor = self.db.execute('''SELECT Air_Temp, Barometric_Press, Wind_Speed
                                   FROM {} WHERE Date BETWEEN {} AND {}'''.format(self.table,
                                                                                  start.strftime('%Y%m%d'),
                                                                                  end.strftime('%Y%m%d')))
        for row in cursor:
            yield dict(row)
            
    def _get_status_for_range(self, start, end):
        """
        Given a start and end date, return a generator of dicts
        containing all available Date and Status values
        """
        # get Dates/Statuses that already exist in DB
        cursor = self.db.execute('''SELECT DISTINCT Date, Status FROM {}
                                     WHERE Date BETWEEN {} AND {}'''.format(self.table,
                                                                            start.strftime('%Y%m%d'),
                                                                            end.strftime('%Y%m%d')))
        for row in cursor:
            yield dict(row)
    
    def _update_data_for_date(self, date, partial):
        """
        Uses lpoWeb module to retrieve data for specified date
        and inserts into new DB entry
        NOTE - use partial parameter to specify if entry already exists
        """        
        # clear out any partial data for this entry
        if partial:
            self.db.execute('DELETE FROM {} WHERE Date={}'.format(self.table, date.strftime('%Y%m%d')))
            self.db.commit()
        
        try:
            data = lpoWeb.get_data_for_date(date)
        except:
            raise
        
        for entry in data:
            self.db.execute('''INSERT INTO {} (Date, Time, Status, Air_Temp, Barometric_Press, Wind_Speed)
                                VALUES (?, ?, ?, ?, ?, ?)'''.format(self.table), (entry['Date'].replace("_", ""),
                                                                                   entry['Time'],
                                                                                   entry['Status'],
                                                                                   entry['Air_Temp'],
                                                                                   entry['Barometric_Press'],
                                                                                   entry['Wind_Speed']))
        self.db.commit()

    def clear(self):
        """
        Clears out the database by dropping the current table
        """
        self.db.execute('DROP TABLE IF EXISTS {}'.format(self.table))
      
    def close(self):
        """
        Safely close down the database
        """
        self.db.close()
        del self.filename

def test():
    """
    A simple test routine
    """
    # create/clear/close to empty db before testing
    db = lpoDB(filename = 'test.db', table = 'Test')
    db.clear()
    db.close()
    
    # create db for testing
    db = lpoDB(filename = 'test.db', table = 'Test')
    
    # verify the db is empty
    if dict(db) != {}:
        print('Error in lpoDB test(): Database is not empty')

    # add data for current date
    try:
        db.update_data_for_date(date.teoday(), False)        
    except:
        print('ERROR in lpoDB.test(): Could not retrieve data for today\n')
    
    for entry in db:
        print(entry)
    
    db.close()

# if this module is run as main it will execute the test routine    

if __name__ == "__main__": test()