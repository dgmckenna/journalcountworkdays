import re
import pyperclip

# Develop a regex to look for dates in the form YYYY-MM-DD
dateRegex = re.compile(r'{\d\d\d\d-\d\d-\d\d.*}')

# Load the input from the clipboard
clipboard = pyperclip.paste()

# Search for all YYYY-MM-DD's
days_list = dateRegex.findall(clipboard)

# Output the results the console and search for duplicates
print (days_list)
print ('Number of days', len(days_list))

single_inst_list = []

for item in days_list:
    count_item = 0
    for item2 in days_list:
        if item == item2:
            count_item +=1

    if count_item == 1:
        single_inst_list.append(item)

print (single_inst_list)
print ('Excluding duplicates', len(single_inst_list))
