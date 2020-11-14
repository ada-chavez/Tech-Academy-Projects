##  Python version:     3.9.0
##
##  Author:             Ada Chavez
##
##  Description:        Program that can tell if the store branch is open
##                      in New York, London, and Portland with the store hours
##                      9AM - 5PM in their respective time zones.

import pytz
# getting datatime class from datetime module
from datetime import datetime
from pytz import timezone


portland_tz = pytz.timezone('US/Pacific')
portland_current_time = datetime.strftime(datetime.now(portland_tz),"%H:%M:%S")

london_tz = pytz.timezone('Europe/London')
london_current_time = datetime.strftime(datetime.now(london_tz),"%H:%M:%S")


newyork_tz = pytz.timezone('America/New_York')
newyork_current_time = datetime.strftime(datetime.now(newyork_tz),"%H:%M:%S")


open_time = "09:00:00"
close_time = "17:0:0"


if portland_current_time > open_time and portland_current_time < close_time:
    print("The time in Portland is: {} and the store is OPEN".format(portland_current_time))

else:
 print("The time in Portland is: {} and the store is CLOSED".format(portland_current_time))

 
if london_current_time > open_time and london_current_time < close_time:
    print("The time in London is: {} and the store is OPEN".format(london_current_time))

else:
 print("The time in London is: {} and the store is CLOSED".format(london_current_time))

 
if newyork_current_time > open_time and newyork_current_time < close_time:
    print("The time in New York is: {} and the store is OPEN".format(newyork_current_time))

else:
 print("The time in New York is: {} and the store is CLOSED".format(newyork_current_time))
