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


telemarketer_numbers = []

call_makers = []
call_receivers = []
for call in calls:
    call_makers.append(call[0])
    call_receivers.append(call[1])

text_senders = []
text_receivers = []
for text in texts:
    text_senders.append(text[0])
    text_receivers.append(text[1])

for call_maker in call_makers:
    if (
        call_maker not in call_receivers
        and call_maker not in text_senders
        and call_maker not in text_receivers
        and call_maker not in telemarketer_numbers
       ):
        telemarketer_numbers.append(call_maker)

print("These numbers could be telemarketers:")
for telemarketer_number in sorted(telemarketer_numbers):
    print(telemarketer_number)
