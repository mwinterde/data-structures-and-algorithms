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

total_times = dict()

for call in calls:
    total_times[call[0]] = total_times.get(call[0], 0) + int(call[3])
    total_times[call[1]] = total_times.get(call[1], 0) + int(call[3])

max_telephone_number = 0
max_total_time = 0

for telephone_number, total_time in total_times.items():
    if total_time > max_total_time:
        max_telephone_number, max_total_time = telephone_number, total_time

print(f"{max_telephone_number} spent the longest time, {max_total_time} "
      f"seconds, on the phone during September 2016.")


