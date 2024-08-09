
# weekdays is 7:00
# weekend is 10:00

# vacation weekday is 10:00
# vacation weekend is off

def alarm_clock(day, vacation):
    if not vacation:
        if day == 1 or day == 2 or day == 3 or day == 4 or day == 5:
            return '7:00'
        elif day == 6 or day == 7 or day == 0:
            return '10:00'
    elif vacation:
        if day == 1 or day == 2 or day == 3 or day == 4 or day == 5:
            return '10:00'
        elif day == 6 or day == 7 or day == 0:
            return 'off'
