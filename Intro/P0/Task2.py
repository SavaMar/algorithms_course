"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

call_set_1 = set([call[0] for call in calls])
call_set_2 = set([call[1] for call in calls])
uniq_call_set = call_set_1 | call_set_2
marks = {}.fromkeys(uniq_call_set, 0)

for call in calls:
  marks[str(call[0])] += int(call[3])

for call in calls:
    marks[str(call[1])] += int(call[3])

# return [number for number,seconds in list.items() if seconds == total_time]
# total_time = sorted(marks.values())
# phone_number = str([number for number,seconds in marks.iteritems() if seconds == total_time[-1]])

max_key = max(marks, key=lambda i: marks[i])
print(marks.sorted(key=lambda i: marks[i]))

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(max_key, str(marks.get(max_key))))
