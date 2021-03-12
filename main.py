import re

# phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
# matchObject = phoneNumRegex.search('My phone number is (415) 555-4242.')
# print('Phone number found: ' + matchObject.group())
# print('Phone number found: ' + matchObject.group(1))
# print('Phone number found: ' + matchObject.group(2))
# print('Phone number found: ' + matchObject.group(0))


# Splitting Regex onto multiple lines
# phoneRegex = re.compile(r'''(
#     (\d{3}|\(\d{3}\))?            # area code
#     (\s|-|\.)?                    # separator
#     \d{3}                         # first 3 digits
#     (\s|-|\.)                     # separator
#     \d{4}                         # last 4 digits
#     (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
#     )''', re.VERBOSE)


# areaCode, mainNumber = matchObject.groups()
# print(areaCode, mainNumber)


# batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
# mo = batRegex.search('Batmobile lost a wheel')
# print(mo.group())
# print(mo.group(1))


# batRegex = re.compile(r'Bat(wo)?man')
# mo1 = batRegex.search('The Adventures of Batman')
# print(mo1.group())
# mo2 = batRegex.search('The Adventures of Batwoman')
# print(mo2.group())


phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')  # has no groups
mo = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(mo)
