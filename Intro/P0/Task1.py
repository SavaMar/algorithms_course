"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
# unic_array = []
# for i in texts:
#     if i[0] not in unic_array:
#         unic_array.append(i)
#     if i[1] not in unic_array:
#         unic_array.append(i)

# for i in texts:
#     if i not in unic_array:
#         unic_array.append(i)

text_set_1 = set([text[0] for text in texts])
text_set_2 = set([text[0] for text in texts])
uniq_text_set = text_set_1 | text_set_2

call_set_1 = set([call[0] for call in calls])
call_set_2 = set([call[0] for call in calls])
uniq_call_set = call_set_1 | call_set_2


print("There are {} different telephone numbers in the records.".format(set(uniq_text_set | uniq_call_set).__len__()))