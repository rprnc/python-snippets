# datechecker.py - Checks date string formats

import pyperclip
import re

# Phone Number Regex
phoneRegex = re.compile(r'''(
    (\d{2})                           # DD
    (\s/)                               # separator
    (\d{2})                           # MM
    (\s|-|\.)                         # separator
    (\d{4})                           # YYYY
    )''', re.VERBOSE)


text = '''
20/2/17	03:22:56 Then store these strings into variables named month, 
20/2/17	04:10:57 years range from 1000 to 2
20/2/17	04:10:57 ill accept nonexistent dates like 31/02/2020 or 31/04/2021. Then store these strings into variab
20/2/17	04:10:57 Then store these strings into
20/2/17	04:10:57 expression doesn’t have to detect
20/2/17	05:03:03 Then store these strings into
'''


# Write a regular expression that can detect dates in the DD/MM/YYYY format. Assume that the days range from 01 to 31, the months range from 01 to 12, and the years range from 1000 to 2999. Note that if the day or month is a single digit, it’ll have a leading zero. The regular expression doesn’t have to detect correct days for each month or for leap years; it will accept nonexistent dates like 31/02/2020 or 31/04/2021. Then store these strings into variables named month, day, and year, and write additional code that can detect if it is a valid date. April, June, September, and November have 30 days, February has 28 days, and the rest of the months have 31 days. February has 29 days in leap years. Leap years are every year evenly divisible by 4, except for years evenly divisible by 100, unless the year is also evenly divisible by 400. Note how this calculation makes it impossible to make a reasonably sized regular expression that can detect a valid date.
