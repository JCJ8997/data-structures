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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

outgoing_calls = set()
incoming_calls = set()
for record in calls :
    outgoing_calls.add(record[0])
    incoming_calls.add(record[1])


outgoing_texts = set()
incoming_texts = set()
for record in texts:
    outgoing_texts.add(record[0])
    incoming_texts.add(record[1])


possible_telemarketers = set()
for number in outgoing_calls :
    if number not in incoming_calls and number not in outgoing_texts and number not in incoming_texts :
        possible_telemarketers.add(number)
        
possible_telemarketers = sorted(possible_telemarketers)

print("These numbers could be telemarketers: ")
for sorted_number in possible_telemarketers:
    print(sorted_number)
