#!/usr/bin/python3
# lpoApp.py by Barron Stone
# This is an exercise file from Python Code Clinic on lynda.com

from tkinter import *
from tkinter import ttk, messagebox
from statistics import mean, median 
from datetime import date
import lpoDB

__version__ = '0.3.2'

class lpoApp:
    """
    This is the top-level module for the Lake Pend Oreille
    statistics challenge.  It manages the GUI and makes calls
    to the lpoDB module to retrieve data for date ranges.   
    The Python statistics module (introduced in Python 3.4)
    is used to calculate the mean and median values.
    """ 
      
    def __init__(self, master):
             
        self.master = master      
        self._createGUI()                    
        self.database = lpoDB.lpoDB()
        self.master.protocol("WM_DELETE_WINDOW", self._safe_close)
        
    def _createGUI(self):
        
        # configure style of the GUI
        bgcolor = '#CCCCFF'
        self.master.configure(background = bgcolor)        
        self.master.title('Lake Pend Oreille')
        self.master.resizable(False, False)      
        self.style = ttk.Style()
        self.style.configure('TFrame', background = bgcolor)
        self.style.configure('TButton', background = bgcolor, font = ('Arial Black', 10))
        self.style.configure('TLabel', background = bgcolor, font = ('Arial Black', 10))
        self.style.configure('Status.TLabel', background = bgcolor, font = ('Arial', 10))
        self.style.configure('Result.TLabel', background = bgcolor, font = ('Courier', 10))
        
        # create and display header frame with image
        self.frame_header = ttk.Frame(self.master)
        self.frame_header.pack(side = TOP)
        self.logo = PhotoImage(file='lpo_logo.gif')
        ttk.Label(self.frame_header, image = self.logo).pack()
        
        # create and display frame to hold user input widgets
        self.frame_input = ttk.Frame(self.master)
        self.frame_input.pack(side = TOP)
               
        ttk.Label(self.frame_input, text = 'Start Date:').grid(row = 0, column = 1, columnspan = 3, sticky = 'sw')
        ttk.Label(self.frame_input, text = 'End Date:').grid(row = 0, column = 5, columnspan = 3, sticky = 'sw')
        
        self.start_day = StringVar()
        self.start_month = StringVar()
        self.start_year = StringVar()
        self.end_day = StringVar()
        self.end_month = StringVar()
        self.end_year = StringVar()      

        self.months = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                       'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
            
        # create a Spinbox for each day/month/year of start/end
        Spinbox(self.frame_input, from_ = 1, to = 31,
                textvariable = self.start_day, width = 2,
                font = 'Courier 12').grid(row = 1, column = 1)
        Spinbox(self.frame_input, values = self.months,
                textvariable = self.start_month, width = 3,
                font = 'Courier 12').grid(row = 1, column = 2)
        Spinbox(self.frame_input, from_ = 2001, to = date.today().year,
                textvariable = self.start_year, width = 4,
                font = 'Courier 12').grid(row = 1, column = 3)
        Spinbox(self.frame_input, from_ = 1, to = 31,
                textvariable = self.end_day, width = 2,
                font = 'Courier 12').grid(row = 1, column = 5)
        Spinbox(self.frame_input, values = self.months,
                textvariable = self.end_month, width = 3,
                font = 'Courier 12').grid(row = 1, column = 6)
        Spinbox(self.frame_input, from_ = 2001, to = date.today().year,
                textvariable = self.end_year, width = 4,
                font = 'Courier 12').grid(row = 1, column = 7)
               
        # set default start and end dates to today
        self.start_day.set(date.today().day)
        self.start_month.set(self.months[date.today().month-1])
        self.start_year.set(date.today().year)
        self.end_day.set(date.today().day)
        self.end_month.set(self.months[date.today().month-1])
        self.end_year.set(date.today().year)
        
        # these labels are for padding purposes
        ttk.Label(self.frame_input).grid(row = 1, column = 0, padx = 5)
        ttk.Label(self.frame_input).grid(row = 1, column = 4, padx = 5)
        ttk.Label(self.frame_input).grid(row = 1, column = 8, padx = 5)

        ttk.Button(self.frame_input, text = 'Submit',
                   command = self._submit_callback).grid(row = 2, column = 0, columnspan = 9, pady = 5)
  
        # create a frame to display results, but do not show it yet
        self.frame_result = ttk.Frame(self.master)

        ttk.Label(self.frame_result, text = 'Mean:').grid(row = 1, column = 0, padx = 5)
        ttk.Label(self.frame_result, text = 'Median:').grid(row = 2, column = 0, padx = 5)
        
        ttk.Label(self.frame_result, text = 'Air\nTemp:',
                  justify = CENTER).grid(row = 0, column = 2, sticky = 'e', padx = 5)
        ttk.Label(self.frame_result, text = 'Barometric\nPressure:',
                  justify = CENTER).grid(row = 0, column = 3, sticky = 'e', padx = 5)
        ttk.Label(self.frame_result, text = 'Wind\nSpeed:',
                  justify = CENTER).grid(row = 0, column = 1, sticky = 'e', padx = 5)

        self.air_temp_mean = StringVar()
        self.air_temp_median = StringVar()
        self.barometric_press_mean = StringVar()
        self.barometric_press_median = StringVar()
        self.wind_speed_mean = StringVar()
        self.wind_speed_median = StringVar()
        
        ttk.Label(self.frame_result, textvariable = self.air_temp_mean,
                  style = 'Result.TLabel').grid(row = 1, column = 2)
        ttk.Label(self.frame_result, textvariable = self.air_temp_median,
                  style = 'Result.TLabel').grid(row = 2, column = 2)
        ttk.Label(self.frame_result, textvariable = self.barometric_press_mean,
                  style = 'Result.TLabel').grid(row = 1, column = 3)
        ttk.Label(self.frame_result, textvariable = self.barometric_press_median,
                  style = 'Result.TLabel').grid(row = 2, column = 3)
        ttk.Label(self.frame_result, textvariable = self.wind_speed_mean,
                  style = 'Result.TLabel').grid(row = 1, column = 1)
        ttk.Label(self.frame_result, textvariable = self.wind_speed_mean,
                  style = 'Result.TLabel').grid(row = 2, column = 1) 
        
    def _submit_callback(self):
        
        # check that the input values are a real, legitimate date
        try:       
            start = date(int(self.start_year.get()),
                         self.months.index(self.start_month.get()) + 1,
                         int(self.start_day.get()))
            
            end = date(int(self.end_year.get()),
                         self.months.index(self.end_month.get()) + 1,
                         int(self.end_day.get()))
            
        except ValueError as e:
            messagebox.showerror(title = 'ValueError',
                                 message = ('INVALID DATE\n'
                                            'Correct format is "DD Mon YYYY"'))
            # reset default start and end dates to today
            self.start_day.set(date.today().day)
            self.start_month.set(self.months[date.today().month-1])
            self.start_year.set(date.today().year)
            self.end_day.set(date.today().day)
            self.end_month.set(self.months[date.today().month-1])
            self.end_year.set(date.today().year)
            return        
        
        # check that date range is valid
        if (start < date(2001, 1, 12)) or (end > date.today()) or (start > end):
            messagebox.showerror(title = 'ValueError',
                                 message = ('INVALID DATE RANGE\nStart Date: {}\nEnd Date: {}\n'
                                            'Dates must be between 2001-1-12 and {}.\n'
                                            'Start Date must be <= End Date.').format(start, end, date.today()))
            return        

        data = list(self.database.get_data_for_range(start, end))

        if data != []:            
            
            # the lists will hold all values from date range for each weather parameter
            dict_of_lists = dict(Air_Temp = [], Barometric_Press = [], Wind_Speed = [])
            
            for entry in data:
                    for key in dict_of_lists.keys():
                        dict_of_lists[key].append(entry[key])
                        
            # calculate the mean & median for each type of data; store result in dictionaries
            result = {}
            for key in dict_of_lists.keys():
                result[key] = dict(mean = mean(dict_of_lists[key]),
                                   median = median(dict_of_lists[key]))
            
            # set StringVars associated with results labels
            self.air_temp_mean.set('{0:.2f}'.format(result['Air_Temp']['mean']))
            self.air_temp_median.set('{0:.2f}'.format(result['Air_Temp']['median']))
            self.barometric_press_mean.set('{0:.2f}'.format(result['Barometric_Press']['mean']))
            self.barometric_press_median.set('{0:.2f}'.format(result['Barometric_Press']['median']))
            self.wind_speed_mean.set('{0:.2f}'.format(result['Wind_Speed']['mean']))
            self.wind_speed_median.set('{0:.2f}'.format(result['Wind_Speed']['median']))
            
            # display the results frame
            self.frame_result.pack(side = TOP)

        else:
            # if this request did not produce results, hide the results frame
            self.frame_result.forget()           

    def _safe_close(self):
        """
        This is called when the user closes the GUI.  It ensures the
        database is properly shut down first.
        """
        self.database.close()
        self.master.destroy()
        
def main():
    
    root = Tk()
    app = lpoApp(root)
    root.mainloop()
    
if __name__ == "__main__": main()
