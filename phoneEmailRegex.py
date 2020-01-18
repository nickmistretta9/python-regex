#! python3

import re, pyperclip

# Phone Numbers
phoneRegex = re.compile(r'''
(
    ((\d\d\d)|(\(\d\d\d\)))? # area code (optional)
    (\s|-) # separator
    \d\d\d # first 3 digits
    - # separator
    \d\d\d\d # last 4 digits
    (((ext(\.)?\s)|x) (\d{2,5}))? # extension (optional)
)
''', re.VERBOSE)

# Email Addresses
emailRegex = re.compile(r'''
[a-ZA-Z0-9_.+]+ # name part
@ # @ symbol
[a-ZA-Z0-9_.+]+ # domain name part
''', re.VERBOSE)

text = pyperclip.paste()

phoneNumbers = phoneRegex.findall(text)
emailAddresses = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in phoneNumbers:
    allPhoneNumbers.append(phoneNumber[0])

results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(emailAddresses)
pyperclip.copy(results)