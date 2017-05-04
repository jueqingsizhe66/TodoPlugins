#!/usr/bin/env python
"""
due.py
Python 2 script for todo.txt add-on
Created by Rebecca Morgan 2017-03-10
Copyright (c) 2017 Rebecca Morgan. All rights reserved.
"""

import os
import sys
from datetime import datetime, timedelta
import re

def main(todo_dir, future_days = 0):
    # Prepare lists to store tasks
    overdue = list()
    due_today = list()
    due_future = list()

    # Open todo.txt file
    with open(os.path.join(todo_dir,'todo.txt'), 'r') as f:
        content = f.readlines()
        date = datetime.today()

        # Loop through content and look for due dates, assuming the key due: is used and standard date format
        for i, task in enumerate(content):
            #match = re.search(r'due:\d{4}.\d{2}.\d{2}', task)
            match = re.search(r'\{(\d{4}).(\d{2}).(\d{2})\}', task)
#            if match.group(3) == '00':
#                match.group(3) =='01'
#            if match.group(2) == '00':
#                match.group(2) == '01'
            if match is not None:
                if match.group(3) == '00':
#                    match.group(3) ='01'
                    matchUpdate=match.group(1)+"."+match.group(2)+"."+"01"
               #     print matchUpdate
               #     print 'hello'
                    if match.group(2) == '00':
                        #match.group(2) = '01'
                        matchUpdate=match.group(1)+"."+"01"+"."+"01"
               #         print matchUpdate
                else:
                    matchUpdate=match.group(1)+"."+match.group(2)+"."+match.group(3)

#                print match.group()
#                print match.group(2)
#                print match.group(1)
                #date = datetime.strptime(match.group()[4:], '%Y.%m.%d').date()
                #date = datetime.strptime(match.group()[1:len(match.group())-1], '%Y.%m.%d').date()
                date = datetime.strptime(matchUpdate, '%Y.%m.%d').date()

                # Add matching tasks to list with line number
                if date < datetime.today().date():
                    overdue.append(str(i+1).zfill(2) + " " + task)
                elif date == datetime.today().date():
                    due_today.append(str(i+1).zfill(2) + " " + task)
                elif date < datetime.today().date() + timedelta(days=future_days+1):
                    due_future.append(str(i+1).zfill(2) + " " + task)

    # Print to console
    if len(overdue) > 0:
        print "==============================="
        print "Overdue tasks:"
        print "==============================="
        for task in overdue:
            print task,
    if len(due_today) > 0:
        print "==============================="
        print "Tasks due today:"
        print "==============================="
        for task in due_today:
            print task,
    if len(due_future) > 0:
        print "==============================="
        print "Tasks due in the next " + str(future_days) + " days:"
        print "==============================="
        for task in due_future:
            print task,

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "Usage: due.py [TODO_DIR] <future_days>"
        sys.exit(1)

    if os.path.isdir(sys.argv[1]):
        if len(sys.argv) is 3:
            main(sys.argv[1], int(sys.argv[2]))
        else:
            main(sys.argv[1])
    else:
        print "Error: %s is not a directory" % sys.argv[1]
        sys.exit(1)
