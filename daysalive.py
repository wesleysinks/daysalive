import sys
import os
import datetime

def clearscreen():
    if 'nt' in sys.platform.lower():
        os.system('cls')
    else:
        os.system('clear')

def intinput(inputstring):
    while True:
        try:
            return int(input(inputstring))
            break
        except ValueError:
            print("You must enter a number value!")
        
while True:
    if input("Press ENTER to start, press 'q' to Quit ").lower() == 'q':
        sys.exit()
    else:
        clearscreen()
        y = intinput("What year were you born? (YYYY) ")
        m = intinput("What month were you born? (number pls) ")
        while m > 12 or m < 1:
            m = intinput("There are 12 months in a year. Enter values 1-12 ")
        d = intinput("What calendar day were you born? (DD) ")
        while d > 31 or d < 1:
            d = intinput("Months cant have days less than 1 or more than 31! ")

        birthday = datetime.date(y, m, d)
        daysalive = (datetime.date.today() - birthday).days
        tenthousand = birthday + datetime.timedelta(days=10000)

        clearscreen()
        print("You've been alive {} days.".format(daysalive))
        print("Your 10,000th day alive will be {}.\n\n\n".format(tenthousand))
