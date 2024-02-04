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

# a dictionary to store the numbers and their call duration for each time the number is seen.
unique_numbers = {}

for record in calls :
    if record[0] in unique_numbers.keys():
        unique_numbers[record[0]] += int(record[3])
    else :
        unique_numbers[record[0]] = int(record[3])

    if record[1] in unique_numbers.keys():
        unique_numbers[record[1]] +=int(record[3])
    else :
        unique_numbers[record[1]] = int(record[3])

longest_time = 0
longest_user = None
for unique_record in unique_numbers.keys() :
    if unique_numbers[unique_record] > longest_time :
        longest_time = unique_numbers[unique_record]
        longest_user = unique_record

print(f"{longest_user} spent the longest time, {longest_time} seconds, on the phone during September 2016.")