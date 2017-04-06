import re
import pyperclip

# Develop a regex to look for dates in the form YYYY-MM-DD
dateRegex = re.compile(r'{\d\d\d\d-\d\d-\d\d.*}')

# Load the input from the clipboard
clipboard = pyperclip.paste()

# Search for all YYYY-MM-DD's
regex_days_list = dateRegex.findall(clipboard)

# Output to the console the number of journal entries found
# helps the user identify if they don't have the right stuff
# in the clipboard or not
print (regex_days_list)
print ('Number of Journal Entries: ', len(regex_days_list))

wide_output_list = []
master_tag_list = []

# For each item where we found the regex of the form {YYYY-MM-DD, tag1, tag2}
# remove the brackets and convert it to a list.
for item in regex_days_list:
    s_item = item[1:-1]
    item_list_tmp = s_item.split(',')

    # Perform cleanup on the tags found to remove any leading or ending spaces
    for tag in item_list_tmp[1:]:
        s_tag = tag.strip()

        # Add the tag to the master tag list, this is used to build the
        # wide format necessary for pivot table viewing where
        # each tag is it's own column and you can "count" on instances
        # of that column
        if s_tag not in master_tag_list:
            master_tag_list.append(s_tag)

# Create a list which represents all the non-tag items we put in the header row
# this is used so we can track how many columns to the right to go before
# you start putting the tag columns
header_non_tags = ['Date']        
header_row = header_non_tags + master_tag_list
output_string = '\t'.join(header_row)
wide_output_list.append(header_row)

for item in regex_days_list:
    s_item = item[1:-1]
    item_list_tmp = s_item.split(',')
    
    wide_row = [[]] * len(header_row)
    
    # Perform cleanup on the item list to remove any leading or ending spaces
    date_col_val = item_list_tmp[0]
    wide_row[0] = date_col_val
    for tag in item_list_tmp[1:]:
        s_tag = tag.strip()
        wide_row[master_tag_list.index(s_tag) + len(header_non_tags)] = 1
    wide_output_list.append(wide_row)
    output_string = output_string + '\n' + '\t'.join(str(x) for x in wide_row)

# Put the tab separated, newline separated data into the clipboard for pasting
# into excel or other spreadsheet software
pyperclip.copy(output_string)
    
        
        
