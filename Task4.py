"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
from itertools import chain

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

num_in_texts = list(chain.from_iterable(
    [(sender, reciever) for sender, reciever, _ in texts]))

texters = set(num_in_texts)

call_sent = set()
call_received = set()

for caller, reciever, _, _ in calls:
    call_sent.add(caller)
    call_received.add(reciever)

# telemarkerters don't text or receive call_sent
telemarkerters = call_sent - (texters | call_received)

print("These numbers could be telemarketers:")

for tel_number in sorted(telemarkerters):
    print(tel_number)