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


# combining the text and call records
total_records = texts + calls 
# a dictionary to store the numbers and their occurences.
unique_numbers = {}

for record in total_records :
    if record[0] in unique_numbers.keys():
        unique_numbers[record[0]] +=1
    else :
        unique_numbers[record[0]] = 1

    if record[1] in unique_numbers.keys():
        unique_numbers[record[1]] +=1
    else :
        unique_numbers[record[1]] = 1

count_unique_numbers = len(unique_numbers.keys())
print(f"There are {count_unique_numbers} different telephone numbers in the records.")


