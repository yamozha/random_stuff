# Scheduler.py - scheduling python

import datetime
from datetime import date
import calendar
import sys

def what_class_do_i_have_next(current_time):
    dateday = date.today()
    date = calendar.day_name[dateday.weekday()]
    time = (current_time.strftime('%H:%M'))


    # Mon = ("Monday")
    # Tue = ("Tuesday")
    # Wed = ("Wednesday")
    # Thur = ("Thursday")
    # Fri = ("Friday")

    weekdays = {
        "mon": "Monday",
        "tue": "Tuesday",
        "wed": "Wednesday",
        "thur": "Thursday",
        "fri": "Friday",
        "sat": "Saturday",
    }

    if date == weekdays['mon']:
        if time > "8:30" < "10:00":
            return "Next Esp2"
        if time > "10:00" < "11:20":
            return "Next Esp2"
        if time > "12:00" < "12:50":
            return "Next Esp2"
        if time > "12:50" < "13:30":
            return "Next Esp2"
        if time > "" < "":

    elif date == :
        if time > "8:30" < ""
            return "Next Esp2"
        if time > "12:00" < "12:40":
            return "Next Esp2"
        if time > "12:00" < "12:40":
            return "Next Esp2"
        if time > "12:00" < "12:40":
            return "Next Esp2"

    elif date == Wed:
        if time > "8:30" < ""
            return "Next Esp2"
        if time > "12:00" < "12:40":
            return "Next Esp2"
        if time > "12:00" < "12:40":
            return "Next Esp2"
        if time > "12:00" < "12:40":
            return "Next Esp2"

    elif date == Thur:
        if time > "8:30" < ""
            return "Next Esp2"
        if time > "12:00" < "12:40":
            return "Next Esp2"
        if time > "12:00" < "12:40":
            return "Next Esp2"
        if time > "12:00" < "12:40":
            return "Next Esp2"

    elif date == Fri:
        if time > "8:30" < ""
            return "Next Esp2"
        if time > "12:00" < "12:40":
            return "Next Esp2"
        if time > "12:00" < "12:40":
            return "Next Esp2"
        if time > "12:00" < "12:40":
            return "Next Esp2"

    else:
        return "you are free"


if __name__ == "__main__":
    what_class_do_i_have_next(datetime.datetime.now())
