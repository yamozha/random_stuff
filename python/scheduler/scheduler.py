# Scheduler.py - scheduling python

import datetime
from datetime import date
import calendar
import sys
import time

# def what_class_do_i_have_next(current_time):
dateday = date.today()
date = calendar.day_name[dateday.weekday()]
time = (time.strftime('%H:%M'))


mon = ("Monday")
tue = ("Tuesday")
wed = ("Wednesday")
thur = ("Thursday")
fri = ("Friday")

    # weekdays = {
    #     "mon": "Monday",
    #     "tue": "Tuesday",
    #     "wed": "Wednesday",
    #     "thur": "Thursday",
    #     "fri": "Friday",
    #     "sat": "Saturday",
    # }

if date == mon:
    if time > "8:30" < "10:00":
        print("Business")
    if time > "10:00" < "11:20":
        print("History")
    if time > "12:00" < "12:50":
        print("IT")
    if time > "12:50" < "13:30":
        print("IT")
    if time > "13:40" < "14:20":
        print("Art")


    elif date == tue:
        if time > "8:30" < "10:00":
            print("BG")
        if time > "10:00" < "11:20":
            print("Spanish")
        if time > "12:00" < "12:50":
            print("English")
        if time > "12:50" < "13:30":
            print("English")
        if time > "13:40" < "14:20":
            print("Math")

    elif date == wed:
        if time > "8:30" < "10:00":
            print("Chem")
        if time > "10:00" < "11:20":
            print("History")
        if time > "12:00" < "12:50":
            print("BG")
        if time > "12:50" < "13:30":
            print("Spanish")
        if time > "13:40" < "14:20":
            print("Spanish")

    elif date == thur:
        if time > "8:30" < "9:50":
            print("Phys")
        if time > "10:00" < "11:20":
            print("Maths")
        if time > "12:00" < "12:50":
            print("Chem")
        if time > "12:50" < "13:30":
            print("English")
        if time > "13:40" < "14:20":
            print("English")

    elif date == fri:
        if time > "8:30" < "10:00":
            print("Geography")
        if time > "10:00" < "11:20":
            print("PE")
        if time > "12:00" < "12:50":
            print("Biology")
        if time > "12:50" < "13:30":
            print("Biology")
        if time > "13:40" < "14:20":
            print("none yeet")

    else:
        print("you are free")


# if __name__ == "__main__":
#     what_class_do_i_have_next(datetime.datetime.now())
