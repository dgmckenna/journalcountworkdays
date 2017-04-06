# journalcountworkdays
Count the number of days a journal has entries in it.

This is a basic python script which accepts input from the clipboard and outputs the number of days that you did an entry.

Each journal day entry must have a text in the following form to be counted:

{YYYY-MM-DD, Duration, optional tag1, optional tag2, optional tag3}

If you have journal entries sorted newest to oldest, putting the above example at the start of your journal document and then copy pasting it each time helps implement this. You can edit the template above with actual tags as you use them, and when you copy paste it, delete the tags that don't apply.

For example the journal might have:

{YYYY-MM-DD, on train, at home, on weekend}

and when you copy it and make an instance of it for when you are working on your journal on the train, not on a weekend you would have:

{2017-04-04, 40, on train}
{2017-04-03, 40, on train}

THe resulting output would be:

Date	Duration	on train
2017-04-04	40	1
2017-04-03	40	1